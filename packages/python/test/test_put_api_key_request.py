# coding: utf-8

"""
    Occam AI's public API

    API exposing Occam AI's planning, execution and supervision capabilities.

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from occam_sdk.models.put_api_key_request import PutAPIKeyRequest

class TestPutAPIKeyRequest(unittest.TestCase):
    """PutAPIKeyRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PutAPIKeyRequest:
        """Test PutAPIKeyRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PutAPIKeyRequest`
        """
        model = PutAPIKeyRequest()
        if include_optional:
            return PutAPIKeyRequest(
                name = ''
            )
        else:
            return PutAPIKeyRequest(
                name = '',
        )
        """

    def testPutAPIKeyRequest(self):
        """Test PutAPIKeyRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
