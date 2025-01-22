# Occam SDK

This repository contains the Occam SDK generator for multiple languages.

## Installation

```
# poetry
poetry add occam_sdk

# pip
pip install occam_sdk
```

## Generating the SDK

The SDK is generated using [OpenAPI Generator](https://openapi-generator.tech/) docker container.
The final client is slightly customized, so in order to simplify the process, a utility script is used to generate the SDK.

### Prerequisites
- have docker installed
- have the occam api running locally at `http://127.0.0.1:8000`

### Running the script

```bash
python generator/generate_sdk.py
```

## Publishing the Python SDK to Pypi

### Prerequisites
- have a pypi account set up:
```bash
poetry config pypi-token.pypi <your-pypi-token>
```
- have poetry installed

### Publishing

```bash
cd packages/python
poetry config pypi-token.pypi <your-pypi-token>
poetry build
poetry publish
```


