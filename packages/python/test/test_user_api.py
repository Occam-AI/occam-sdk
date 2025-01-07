# coding: utf-8

"""
    Occam AI's public API

    API exposing Occam AI's planning, execution and supervision capabilities.

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from occam_sdk.api.user_api import UserApi


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()

    def tearDown(self) -> None:
        pass

    def test_delete_current_user_users_me_delete(self) -> None:
        """Test case for delete_current_user_users_me_delete

        Delete Current User
        """
        pass

    def test_get_connector_schemas_connectors_schemas_get(self) -> None:
        """Test case for get_connector_schemas_connectors_schemas_get

        Get Connector Schemas
        """
        pass

    def test_google_oauth_end_integrations_oauth_google_end_get(self) -> None:
        """Test case for google_oauth_end_integrations_oauth_google_end_get

        Google Oauth End
        """
        pass

    def test_isolated_oauth_end_integrations_oauth_isolated_end_get(self) -> None:
        """Test case for isolated_oauth_end_integrations_oauth_isolated_end_get

        Isolated Oauth End
        """
        pass

    def test_merge_confirm_integrations_merge_confirm_post(self) -> None:
        """Test case for merge_confirm_integrations_merge_confirm_post

        Merge Confirm
        """
        pass

    def test_merge_link_token_integrations_merge_link_token_get(self) -> None:
        """Test case for merge_link_token_integrations_merge_link_token_get

        Merge Link Token
        """
        pass

    def test_oauth_end_integrations_oauth_end_get(self) -> None:
        """Test case for oauth_end_integrations_oauth_end_get

        Oauth End
        """
        pass

    def test_oauth_start_integrations_oauth_start_get(self) -> None:
        """Test case for oauth_start_integrations_oauth_start_get

        Oauth Start
        """
        pass

    def test_read_current_user_users_me_get(self) -> None:
        """Test case for read_current_user_users_me_get

        Read Current User
        """
        pass

    def test_register_new_user_users_register_post(self) -> None:
        """Test case for register_new_user_users_register_post

        Register New User
        """
        pass

    def test_reset_current_user_password_users_reset_password_post(self) -> None:
        """Test case for reset_current_user_password_users_reset_password_post

        Reset Current User Password
        """
        pass

    def test_update_current_user_announcement_users_update_active_announcement_post(self) -> None:
        """Test case for update_current_user_announcement_users_update_active_announcement_post

        Update Current User Announcement
        """
        pass

    def test_update_current_user_membership_type_users_update_membership_type_post(self) -> None:
        """Test case for update_current_user_membership_type_users_update_membership_type_post

        Update Current User Membership Type
        """
        pass


if __name__ == '__main__':
    unittest.main()
