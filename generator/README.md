# Occam SDK

This SDK is generated from the OpenAPI spec of the Occam API.

## Generating the SDK

To generate the SDK, run the following command:

```python generate-sdk.py```

The folder contains a copy of the python "templates", which specify how to generate the SDK.
The original templates are [available on the repository](https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/python)

This will create a folder called `occam_sdk` which contains all the SDKs, and you can then install it with:
```
poetry add build_sdk/python
```

# What are the changes
## Added OccamClient
By default, the generator creates different clients for each service type, e.g.
```
from ... import ApiClient, AuthApi, ResourcesApi
client = ApiClient(..)

auth_client = AuthApi(client)
auth_client.login(..)

resources_client = ResourcesApi(client)
resources_api.list(..)
```
which is not very convenient. In generate_sdk.py, we add a piece of code (called OccamClient) that allows us to access all the services via a single client, e.g.
```
from ... import OccamClient
client = OccamClient(..)

client.auth().login(..)
client.resources().list(..)
```
Furthermore, in client.mustache, we add a `@auto_fill_args` decorator. This decorator automatically fills in the arguments for the function if they are defined in the OccamClient. This allows behaviour such as 
```
# set the uuid once
resources = client.resources(uuid="123")
# no need to specify uuid again
resources.get()
resources.get_datasets()
resources.delete()
```

## Changed naming convention
In api.mustache, we change the naming convention by adding a prefix `operation_id_`. This allows us to easily identify the functions that need to be renamed (in the post-processing step).
This is better explain in the next section.

# Function naming and postprocessing

By default, the generator creates functions based on the operationId, so the names are very long and hard to read e.g. `login_access_token_auth_access_token_post`. 
In order to solve this, we make use of a postprocessing script, which is run after the SDK is generated.

## Overwriting the operationId in FastAPI
You must manually set the operation_id variable in fastapi. Note that it has to be unique, so in order to ensure uniqueness without affecting the readability, we use remove the first part of the operationId.
For example:
```
@router.post(
    "/access-token",
    response_model=AccessTokenResponse,
    responses=ACCESS_TOKEN_RESPONSES,
    description="OAuth2 compatible token, get an access token for future requests using username and password",
    operation_id="auth_login",
)
```
the postprocessing script takes care of removing the first part of the operationId, so `auth_login` becomes `login`, and is therefore accessible via AuthClient.login(), rather than AuthClient.auth_login().

## Why is the postprocessing in bash?
Because bash is the only universal enough language present on the docker image. Perl is missing required libraries (Slurp), and python is simply not installed. I know, bash sucks.