# Using the Occam SDK

The Occam SDK is generated from the OpenAPI spec of the Occam API.

## Installing the SDK

To install the SDK, run the following command:

```bash
poetry add occam-sdk
```
## Using the SDK

Make sure you have a valid API key, then:
```python
from occam_sdk import OccamClient

occam = OccamClient(api_key='sk-occam-test')

# for development, you can point to a local occam instance like so:
occam_client = OccamClient(api_key='sk-occam-test', base_url='http://127.0.0.1:8000')
```

You will have multiple sub-clients available for different parts of the API.
For example, to list datasets for a resource, but you will most likely only use
the resources client:

```python
# get all resources
resources = occam_client.resources().list()

# get a resource's datasets
datasets = occam_client.resources().datasets(resource_uuid='...').list()
```

when re-using the same resource for multiple operations, you can set the parameter and use
the client directly:
```python
resource_client = occam_client.resources(resource_uuid='...')

# no need to repeat the uuid
resource_client.get()
resource_client.datasets().list()
```
