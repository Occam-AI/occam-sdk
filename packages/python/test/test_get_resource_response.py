# coding: utf-8

"""
    Occam AI's public API

    API exposing Occam AI's planning, execution and supervision capabilities.

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from occam_sdk.models.get_resource_response import GetResourceResponse

class TestGetResourceResponse(unittest.TestCase):
    """GetResourceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetResourceResponse:
        """Test GetResourceResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetResourceResponse`
        """
        model = GetResourceResponse()
        if include_optional:
            return GetResourceResponse(
                uuid = '',
                kind = '',
                kind_display_name = '',
                instance_display_name = '',
                short_description = '',
                long_description = '',
                icon = '',
                category = '',
                category_rank = 56,
                address = occam_sdk.models.address.Address(),
                needs_credentials = True,
                is_datasource = True,
                strictness = '0',
                is_connected = True,
                connection_status = 'is_template',
                subtool_kinds = [
                    ''
                    ],
                connection_uuid = '',
                is_template = True,
                is_scannable = True,
                is_template_instance = True,
                credential_uuid = '',
                datasets = [
                    occam_sdk.models.get_dataset_response.GetDatasetResponse(
                        uuid = '', 
                        name = '', 
                        content = occam_sdk.models.content.Content(), 
                        address_summary = '/temporary/placeholder', 
                        connection_status = 'is_template', 
                        is_root = True, )
                    ],
                input_fields = [
                    occam_sdk.models.basic_field_info.BasicFieldInfo(
                        name = '', 
                        required = True, )
                    ],
                params_model = None,
                output_fields = [
                    occam_sdk.models.basic_field_info.BasicFieldInfo(
                        name = '', 
                        required = True, )
                    ]
            )
        else:
            return GetResourceResponse(
                uuid = '',
                kind = '',
                kind_display_name = '',
                short_description = '',
                long_description = '',
                icon = '',
                category = '',
                category_rank = 56,
                address = occam_sdk.models.address.Address(),
                needs_credentials = True,
                is_datasource = True,
                strictness = '0',
                is_connected = True,
                connection_status = 'is_template',
        )
        """

    def testGetResourceResponse(self):
        """Test GetResourceResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
