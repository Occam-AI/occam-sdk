# coding: utf-8

"""
    Occam AI's public API

    API exposing Occam AI's planning, execution and supervision capabilities.

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from occam_sdk.models.update_membership_type_request import UpdateMembershipTypeRequest

class TestUpdateMembershipTypeRequest(unittest.TestCase):
    """UpdateMembershipTypeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateMembershipTypeRequest:
        """Test UpdateMembershipTypeRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateMembershipTypeRequest`
        """
        model = UpdateMembershipTypeRequest()
        if include_optional:
            return UpdateMembershipTypeRequest(
                user_uuid = '',
                membership_type = 'free'
            )
        else:
            return UpdateMembershipTypeRequest(
                user_uuid = '',
                membership_type = 'free',
        )
        """

    def testUpdateMembershipTypeRequest(self):
        """Test UpdateMembershipTypeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
