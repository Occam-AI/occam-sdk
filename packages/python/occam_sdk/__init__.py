# coding: utf-8

# flake8: noqa

"""
    Occam AI's public API

    API exposing Occam AI's planning, execution and supervision capabilities.

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from occam_sdk.api.agents_api import AgentsApi
from occam_sdk.api.auth_api import AuthApi
from occam_sdk.api.default_api import DefaultApi
from occam_sdk.api.demo_api import DemoApi
from occam_sdk.api.integration_api import IntegrationApi
from occam_sdk.api.key_api import KeyApi
from occam_sdk.api.payment_api import PaymentApi
from occam_sdk.api.plan_api import PlanApi
from occam_sdk.api.resources_api import ResourcesApi
from occam_sdk.api.user_api import UserApi

# import ApiClient
from occam_sdk.api_response import ApiResponse
from occam_sdk.api_client import ApiClient
from occam_sdk.configuration import Configuration
from occam_sdk.exceptions import OpenApiException
from occam_sdk.exceptions import ApiTypeError
from occam_sdk.exceptions import ApiValueError
from occam_sdk.exceptions import ApiKeyError
from occam_sdk.exceptions import ApiAttributeError
from occam_sdk.exceptions import ApiException

# import models into sdk package
from occam_sdk.models.api_key_usage_response import APIKeyUsageResponse
from occam_sdk.models.access_and_refresh_token_response import AccessAndRefreshTokenResponse
from occam_sdk.models.access_token_response import AccessTokenResponse
from occam_sdk.models.adapter_query import AdapterQuery
from occam_sdk.models.add_data_source_request import AddDataSourceRequest
from occam_sdk.models.add_data_source_response import AddDataSourceResponse
from occam_sdk.models.add_dataset_plan_node import AddDatasetPlanNode
from occam_sdk.models.add_dataset_request import AddDatasetRequest
from occam_sdk.models.add_dataset_response import AddDatasetResponse
from occam_sdk.models.add_field_mapping import AddFieldMapping
from occam_sdk.models.add_tool_plan_node import AddToolPlanNode
from occam_sdk.models.add_user_to_resource_request import AddUserToResourceRequest
from occam_sdk.models.agent_identity_response import AgentIdentityResponse
from occam_sdk.models.agent_role import AgentRole
from occam_sdk.models.agent_run_status import AgentRunStatus
from occam_sdk.models.agent_type import AgentType
from occam_sdk.models.basic_field_info import BasicFieldInfo
from occam_sdk.models.connection_status import ConnectionStatus
from occam_sdk.models.connector_schema import ConnectorSchema
from occam_sdk.models.content import Content
from occam_sdk.models.create_agent_request import CreateAgentRequest
from occam_sdk.models.create_agent_response import CreateAgentResponse
from occam_sdk.models.create_payment_checkout_session_request import CreatePaymentCheckoutSessionRequest
from occam_sdk.models.create_payment_checkout_session_response import CreatePaymentCheckoutSessionResponse
from occam_sdk.models.credentials_data_partial_request import CredentialsDataPartialRequest
from occam_sdk.models.edit_dataset_request import EditDatasetRequest
from occam_sdk.models.edit_dataset_response import EditDatasetResponse
from occam_sdk.models.edit_node import EditNode
from occam_sdk.models.file_upload_response import FileUploadResponse
from occam_sdk.models.get_agent_run_status_response import GetAgentRunStatusResponse
from occam_sdk.models.get_dataset_response import GetDatasetResponse
from occam_sdk.models.get_organization_response import GetOrganizationResponse
from occam_sdk.models.get_resource_response import GetResourceResponse
from occam_sdk.models.get_resource_schema_response import GetResourceSchemaResponse
from occam_sdk.models.get_resources_response import GetResourcesResponse
from occam_sdk.models.get_user_payment_details_response import GetUserPaymentDetailsResponse
from occam_sdk.models.get_user_plan_response import GetUserPlanResponse
from occam_sdk.models.http_validation_error import HTTPValidationError
from occam_sdk.models.hidden_api_key_response import HiddenAPIKeyResponse
from occam_sdk.models.llm_role import LLMRole
from occam_sdk.models.listed_key import ListedKey
from occam_sdk.models.manage_payment_method_response import ManagePaymentMethodResponse
from occam_sdk.models.membership_type import MembershipType
from occam_sdk.models.merge_link_token_response import MergeLinkTokenResponse
from occam_sdk.models.merge_public_token_request import MergePublicTokenRequest
from occam_sdk.models.modifications_batch import ModificationsBatch
from occam_sdk.models.modifications_batch_modifications_inner import ModificationsBatchModificationsInner
from occam_sdk.models.o_auth_config import OAuthConfig
from occam_sdk.models.occam_llm_message import OccamLLMMessage
from occam_sdk.models.plan_element_type import PlanElementType
from occam_sdk.models.plan_field_mapping import PlanFieldMapping
from occam_sdk.models.plan_goal import PlanGoal
from occam_sdk.models.plan_modifier_type import PlanModifierType
from occam_sdk.models.put_api_key_request import PutAPIKeyRequest
from occam_sdk.models.redirect_to_response import RedirectToResponse
from occam_sdk.models.refresh_entry_point import RefreshEntryPoint
from occam_sdk.models.refresh_resources_request import RefreshResourcesRequest
from occam_sdk.models.refresh_token_request import RefreshTokenRequest
from occam_sdk.models.remove_field_mapping import RemoveFieldMapping
from occam_sdk.models.remove_node import RemoveNode
from occam_sdk.models.request_agent_modifications_model import RequestAgentModificationsModel
from occam_sdk.models.request_demo_content_response import RequestDemoContentResponse
from occam_sdk.models.request_demo_create_request import RequestDemoCreateRequest
from occam_sdk.models.request_demo_response import RequestDemoResponse
from occam_sdk.models.resource_connection_deletion_request import ResourceConnectionDeletionRequest
from occam_sdk.models.resource_strictness import ResourceStrictness
from occam_sdk.models.response_batch_add_dataset import ResponseBatchAddDataset
from occam_sdk.models.response_datasource_dataset_schemas import ResponseDatasourceDatasetSchemas
from occam_sdk.models.response_resource_info import ResponseResourceInfo
from occam_sdk.models.run_agent_request import RunAgentRequest
from occam_sdk.models.run_agent_response import RunAgentResponse
from occam_sdk.models.run_metrics import RunMetrics
from occam_sdk.models.setup_auto_recharge_request import SetupAutoRechargeRequest
from occam_sdk.models.uuid_response import UUIDResponse
from occam_sdk.models.update_membership_type_request import UpdateMembershipTypeRequest
from occam_sdk.models.update_user_active_announcement_request import UpdateUserActiveAnnouncementRequest
from occam_sdk.models.update_user_resource_request import UpdateUserResourceRequest
from occam_sdk.models.user_create_request import UserCreateRequest
from occam_sdk.models.user_message_model import UserMessageModel
from occam_sdk.models.user_response import UserResponse
from occam_sdk.models.user_stripe_payment_methods_response import UserStripePaymentMethodsResponse
from occam_sdk.models.user_update_password_request import UserUpdatePasswordRequest
from occam_sdk.models.validation_error import ValidationError
from occam_sdk.models.validation_error_loc_inner import ValidationErrorLocInner
from occam_sdk.models.visible_api_key_response import VisibleAPIKeyResponse





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

