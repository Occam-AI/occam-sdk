import shutil
import subprocess
from pathlib import Path

occam_client_definition = """



class OccamClient:
    _auth: AuthApi = None
    _default: DefaultApi = None
    _integration: IntegrationApi = None
    _key: KeyApi = None
    _plan: PlanApi = None
    _resources: ResourcesApi = None
    _user: UserApi = None
    _api_client: ApiClient = None
    _agents: AgentsApi = None
    #_datasets: DatasetsApi = None

    def __init__(self, api_key: str, base_url: str = 'https://api.occam.ai'):
        self.api_key = api_key
        self.base_url = base_url

    def refresh_token(self):
        response = AuthApi(self._api_client).token_from_key(key=self.api_key)

        # set the access token in the api client as Authorization Bearer
        self._api_client.set_default_header("Authorization", f"Bearer {response.access_token}")

    
    @property
    def api_client(self) -> ApiClient:
        # todo: handle refresh on expired access token
        if self._api_client is None:
            config = Configuration(host=self.base_url)
            self._api_client = ApiClient(config)
            self.refresh_token()

            # setup the callback to refresh the token on expired access token
            def refresh_on_expired_token(e: Exception, internal_call):
                if isinstance(e, ApiException) and e.status == 401 and 'Token expired' in e.body:
                    print("Refreshing token...")
                    self.refresh_token() 
                    return internal_call()
                else:
                    raise e
                
            self._api_client.callback_on_exception = refresh_on_expired_token
        return self._api_client

    def auth(self, **kwargs) -> AuthApi:
        if self._auth is None:
            self._auth = AuthApi(self.api_client, **kwargs)
        elif kwargs:
            self._auth._parameters = kwargs
        return self._auth

    def default(self, **kwargs) -> DefaultApi:
        if self._default is None:
            self._default = DefaultApi(self.api_client, **kwargs)
        elif kwargs:
            self._default._parameters = kwargs
        return self._default

    def integration(self, **kwargs) -> IntegrationApi:
        if self._integration is None:
            self._integration = IntegrationApi(self.api_client, **kwargs)
        elif kwargs:
            self._integration._parameters = kwargs
        return self._integration

    def key(self, **kwargs) -> KeyApi:
        if self._key is None:
            self._key = KeyApi(self.api_client, **kwargs)
        elif kwargs:
            self._key._parameters = kwargs
        return self._key

    def plan(self, **kwargs) -> PlanApi:
        if self._plan is None:
            self._plan = PlanApi(self.api_client, **kwargs)
        elif kwargs:
            self._plan._parameters = kwargs
        return self._plan

    def resources(self, resource_uuid: str | None = None, **kwargs) -> ResourcesApi:
        # resource_uuid is added only for type-hinting purposes (since kwargs gives no info)
        if resource_uuid is not None:
            kwargs['resource_uuid'] = resource_uuid

        # on top of the normal resources, we add a "method" to access the datasets via short-hand,
        # since this will likely be the most common use-case e.g. occam.resources(resource_uuid='...').datasets().list()
        if self._resources is None:
            self._resources = ResourcesApi(self.api_client, **kwargs)
            self._resources.datasets = lambda *largs, **lkwargs: self.datasets(*largs, **{**lkwargs, **self._resources._parameters})
        elif kwargs:
            self._resources._parameters = kwargs
            self._resources.datasets = lambda *largs, **lkwargs: self.datasets(*largs, **{**lkwargs, **self._resources._parameters})

        return self._resources

    def user(self, **kwargs) -> UserApi:
        if self._user is None:
            self._user = UserApi(self.api_client, **kwargs)
        elif kwargs:
            self._user._parameters = kwargs
        return self._user

    def agents(self, **kwargs) -> AgentsApi:
        if self._agents is None:
            self._agents = AgentsApi(self.api_client, **kwargs)
        elif kwargs:
            self._agents._parameters = kwargs
        return self._agents

    # def datasets(self, resource_uuid: str | None = None, **kwargs) -> DatasetsApi:
    #     # resource_uuid is added only for type-hinting purposes (since kwargs gives no info)
    #     if resource_uuid is not None:
    #         kwargs['resource_uuid'] = resource_uuid
    #     if self._datasets is None:
    #         self._datasets = DatasetsApi(self.api_client, **kwargs)
    #     elif kwargs:
    #         self._datasets._parameters = kwargs
    #     return self._datasets

"""

def main():
    current_dir = Path(__file__).parent
    root = current_dir.parent
    root_str = str(root)

    if root.joinpath('packages').exists():
        # delete previous build
        shutil.rmtree(root.joinpath('packages'))

    # checkout to the version used in the occam-api repo
    # Define the Docker command
    docker_command = [
    "docker", "run", "--rm",
        "-v", f"{root_str}:/local",
        "-v", f"{root_str}/generator/mounted:/mounted",  # Mount templates directory
        "-p", "8000:8000",
        "-e", "PYTHON_POST_PROCESS_FILE=/mounted/postprocess.sh",
        "openapitools/openapi-generator-cli", "generate",
        "-i", "http://host.docker.internal:8000/openapi.json",
        "-g", "python",
        "-o", "/local/packages/python",
        "--enable-post-process-file",
        "--package-name", "occam_sdk",
        "-c", "/mounted/spec.yaml"
    ]
    print(f"Running {' '.join(docker_command)}")

    # Run the Docker command
    try:
        subprocess.run(docker_command, check=True)
        # Add the occam_client at the end of the base __init__.py file
        with open(root.joinpath("packages").joinpath("python").joinpath("occam_sdk").joinpath("__init__.py"), "a") as f:
            f.write(occam_client_definition)

        # copy SDK_README.md to the generated SDK
        with open(root.joinpath("generator").joinpath("SDK_README.md")) as f:
            sdk_readme = f.read()

        with open(root.joinpath("packages").joinpath("python").joinpath("README.md"), "w+") as f:
            f.write(sdk_readme)

        print("SDK generation completed successfully.")
    except subprocess.CalledProcessError:
        print("""
---------------------------ERROR---------------------------------
PLEASE READ ME
Error occurred while generating SDK. Make sure you have the following:
1. The occam-api is running
2. In .env, the value for SECURITY__BACKEND_CORS_ORIGINS includes "http://host.docker.internal:8000"
3. In .env, the value for SECURITY__ALLOWED_HOSTS includes "host.docker.internal"
""")


if __name__ == "__main__":
    main()
