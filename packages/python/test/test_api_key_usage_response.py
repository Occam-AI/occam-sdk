# coding: utf-8

"""
    Occam AI's public API

    API exposing Occam AI's planning, execution and supervision capabilities.

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from occam_sdk.models.api_key_usage_response import APIKeyUsageResponse

class TestAPIKeyUsageResponse(unittest.TestCase):
    """APIKeyUsageResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> APIKeyUsageResponse:
        """Test APIKeyUsageResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `APIKeyUsageResponse`
        """
        model = APIKeyUsageResponse()
        if include_optional:
            return APIKeyUsageResponse(
                completed_requests = 56,
                successful_requests = 56,
                failed_requests = 56,
                quota_usage_percentage = 1.337,
                requests_per_day = 1.337
            )
        else:
            return APIKeyUsageResponse(
                completed_requests = 56,
                successful_requests = 56,
                failed_requests = 56,
                quota_usage_percentage = 1.337,
                requests_per_day = 1.337,
        )
        """

    def testAPIKeyUsageResponse(self):
        """Test APIKeyUsageResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
