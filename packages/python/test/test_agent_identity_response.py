# coding: utf-8

"""
    Occam AI's public API

    API exposing Occam AI's planning, execution and supervision capabilities.

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from occam_sdk.models.agent_identity_response import AgentIdentityResponse

class TestAgentIdentityResponse(unittest.TestCase):
    """AgentIdentityResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgentIdentityResponse:
        """Test AgentIdentityResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgentIdentityResponse`
        """
        model = AgentIdentityResponse()
        if include_optional:
            return AgentIdentityResponse(
                name = '',
                first_name = '',
                last_name = '',
                base_agent = None,
                type = 'OCCAM_AGENT',
                role = 'general',
                role_embedding_vector = [
                    1.337
                    ],
                short_role_description = '',
                long_role_description = '',
                email = '',
                slack_handle = '',
                user_id = 56,
                prompt = '',
                params = {
                    'key' : null
                    },
                dynamic_spec = None,
                is_base_agent = True,
                params_model_schema = occam_sdk.models.params_model_schema.Params Model Schema(),
                inputs_model_schema = occam_sdk.models.inputs_model_schema.Inputs Model Schema(),
                outputs_model_schema = occam_sdk.models.outputs_model_schema.Outputs Model Schema()
            )
        else:
            return AgentIdentityResponse(
                name = '',
                base_agent = None,
                type = 'OCCAM_AGENT',
                role = 'general',
                params_model_schema = occam_sdk.models.params_model_schema.Params Model Schema(),
                inputs_model_schema = occam_sdk.models.inputs_model_schema.Inputs Model Schema(),
                outputs_model_schema = occam_sdk.models.outputs_model_schema.Outputs Model Schema(),
        )
        """

    def testAgentIdentityResponse(self):
        """Test AgentIdentityResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
