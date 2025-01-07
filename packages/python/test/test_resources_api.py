# coding: utf-8

"""
    Occam AI's public API

    API exposing Occam AI's planning, execution and supervision capabilities.

    The version of the OpenAPI document: 6.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from occam_sdk.api.resources_api import ResourcesApi


class TestResourcesApi(unittest.TestCase):
    """ResourcesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ResourcesApi()

    def tearDown(self) -> None:
        pass

    def test_add_credential_credentials_post(self) -> None:
        """Test case for add_credential_credentials_post

        Add Credential
        """
        pass

    def test_add_dataset_resources_source_uuid_dataset_post(self) -> None:
        """Test case for add_dataset_resources_source_uuid_dataset_post

        Add Dataset
        """
        pass

    def test_dataset_allowed_schemas(self) -> None:
        """Test case for dataset_allowed_schemas

        Get Datasource Dataset Schemas
        """
        pass

    def test_dataset_batch_add(self) -> None:
        """Test case for dataset_batch_add

        Batch Add Dataset
        """
        pass

    def test_dataset_delete(self) -> None:
        """Test case for dataset_delete

        Delete Dataset
        """
        pass

    def test_dataset_edit(self) -> None:
        """Test case for dataset_edit

        Edit Dataset
        """
        pass

    def test_dataset_get(self) -> None:
        """Test case for dataset_get

        Get Dataset
        """
        pass

    def test_dataset_list(self) -> None:
        """Test case for dataset_list

        Get Datasets
        """
        pass

    def test_delete_credential_credentials_uuid_delete(self) -> None:
        """Test case for delete_credential_credentials_uuid_delete

        Delete Credential
        """
        pass

    def test_resource_add_datasource(self) -> None:
        """Test case for resource_add_datasource

        Add Resource
        """
        pass

    def test_resource_connect(self) -> None:
        """Test case for resource_connect

        Update User Resource Connection
        """
        pass

    def test_resource_datasource_schemas(self) -> None:
        """Test case for resource_datasource_schemas

        Get Datasources Schemas
        """
        pass

    def test_resource_delete_connection(self) -> None:
        """Test case for resource_delete_connection

        Delete Connection
        """
        pass

    def test_resource_get(self) -> None:
        """Test case for resource_get

        Get Resource
        """
        pass

    def test_resource_get_files(self) -> None:
        """Test case for resource_get_files

        Get Resource Files
        """
        pass

    def test_resource_list(self) -> None:
        """Test case for resource_list

        Get Resources
        """
        pass

    def test_resource_refresh(self) -> None:
        """Test case for resource_refresh

        Refresh Resources
        """
        pass

    def test_resource_schema(self) -> None:
        """Test case for resource_schema

        Get Resource Schema
        """
        pass

    def test_resource_schemas(self) -> None:
        """Test case for resource_schemas

        Get Datasources Schemas
        """
        pass

    def test_resource_tools_schemas(self) -> None:
        """Test case for resource_tools_schemas

        Get Tools Schemas
        """
        pass

    def test_resource_update(self) -> None:
        """Test case for resource_update

        Update User Resource
        """
        pass

    def test_upload_file_credentials_fileupload_post(self) -> None:
        """Test case for upload_file_credentials_fileupload_post

        Upload File
        """
        pass


if __name__ == '__main__':
    unittest.main()
