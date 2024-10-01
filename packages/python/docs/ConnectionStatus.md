# ConnectionStatus

Initial connection status is set as follows: - UNCONNECTED: e.g., resources missing credentials. - UNTESTED: e.g., resources with credentials, but not tested yet. - ACTIVE: e.g., resources with credentials, and tested to be active   or resources not needing credentials. - Otherwise, initial connection status is left as null. - For a dataset, default connection status is set to UNCONNECTED. - If a resource changes to untested, inactive, deleted, or failed, we update the dataset's connection status to the same.  Connection status can be updated as follows: - When a resource's status is updated, we update the statuses of its datasets   such that if the resource is not active, none of its datasets are active. - If a resource becomes active, its datasets are set to untested. - Conversely, if a dataset is active, this implies that its resource is active.

## Enum

* `IS_TEMPLATE` (value: `'is_template'`)

* `UNCONNECTED` (value: `'unconnected'`)

* `UNTESTED` (value: `'untested'`)

* `ACTIVE` (value: `'active'`)

* `FAILED` (value: `'failed'`)

* `UNREACHABLE` (value: `'unreachable'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


