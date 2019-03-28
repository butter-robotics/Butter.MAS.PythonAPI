# Butter MAS Python API
HTTP client python API for Butter MAS platform.

[![licence](https://img.shields.io/github/license/bennymeg/Butter.MAS.PythonAPI.svg)](https://github.com/bennymeg/Butter.MAS.PythonAPI/blob/master/LICENSE)
[![](https://img.shields.io/pypi/v/butter.mas-api.svg)](https://pypi.org/project/butter.mas-api/)

___
🚧**NOTE:** this repository is still a work in progress.
___

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to install python 3 in order to use this software

### Installing

```
pip install butter.mas-api
```
<!-- NOTE: the PyPi module name is _different_ then the repository name -->

### Usage

```python
from butter.mas.api import Client

butterHttpClient = Client('192.168.0.111')  # use you robot ip here

result = butterHttpClient.playAnimation('welcome')
print(result.json())
```

### Coding style tests

#### Linting

Please use PyLint (Default linter on VS Code) to lint your code before submitting a PR.

#### Tests

Please test your code before submitting a PR.
```
python -m unittest tests/api_test.py
```

## Documentation
- 👨🏼‍💻 [API](https://github.com/bennymeg/Butter.MAS.PythonAPI/blob/master/docs/API.md),  
- 🖋  [Licence](https://github.com/bennymeg/Butter.MAS.PythonAPI/blob/master/LICENSE)
<!-- - 👩🏼‍🏫 [Examples](https://github.com/bennymeg/Butter.MAS.PythonAPI/blob/master/docs/examples),   -->

## Contributing

Please read [CONTRIBUTING.md](https://github.com/bennymeg/Butter.MAS.PythonAPI/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/bennymeg/Butter.MAS.PythonAPI/tags). 

## Authors

**Benny Megidish**

_See also the list of [contributors](https://github.com/bennymeg/Butter.MAS.PythonAPI/contributors) who participated in this project._

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](https://github.com/bennymeg/Butter.MAS.PythonAPI/blob/master/LICENSE) file for details