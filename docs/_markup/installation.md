# Installation

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

You will need to install python 3 in order to use this software

## Installing

Open you Command Prompt (Windows) or Terminal (Mac / Linux) and execute the following command:
`pip install -U butter.mas-api`

## Usage

```python
from butter.mas.api import HttpClient

butterHttpClient = HttpClient('192.168.0.111')  # use you robot ip here

result = butterHttpClient.playAnimation('welcome')
print(result.json())
```
