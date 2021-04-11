# ObjectREST
[![PyPi](https://static.pepy.tech/personalized-badge/objectrest?period=total&units=international_system&left_color=grey&right_color=green&left_text=Downloads)](https://pypi.org/project/objectrest)
[![License](https://img.shields.io/pypi/l/tautulli?color=orange&style=flat-square)](https://github.com/nwithan8/objectrest/blob/master/LICENSE)

[![Open Issues](https://img.shields.io/github/issues-raw/nwithan8/objectrest?color=gold&style=flat-square)](https://github.com/nwithan8/objectrest/issues?q=is%3Aopen+is%3Aissue)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/nwithan8/objectrest?color=black&style=flat-square)](https://github.com/nwithan8/objectrest/issues?q=is%3Aissue+is%3Aclosed)
[![Latest Release](https://img.shields.io/github/v/release/nwithan8/objectrest?color=red&label=latest%20release&logo=github&style=flat-square)](https://github.com/nwithan8/objectrest/releases)

[![Discord](https://img.shields.io/discord/472537215457689601?color=blue&logo=discord&style=flat-square)](https://discord.gg/7jGbCJQ)
[![Twitter](https://img.shields.io/twitter/follow/nwithan8?label=%40nwithan8&logo=twitter&style=flat-square)](https://twitter.com/nwithan8)

A Python package to handle REST API requests, JSON parsing, and pydantic object generation.

# Installation
From PyPi: ``python -m pip install objectrest``

From GitHub ``python -m pip install git+https://github.com/nwithan8/objectrest.git``

# Usage
This package acts as a middle-man between the user and the Requests library.

Users can call to methods directly, or use the RequestHandler class to set universal parameters (i.e. API tokens), universal headers and/or a universal base URL for all requests

Users can retrieve the raw request, the JSON data from a request, or have the JSON data automatically parsed into a Pydantic model.

Example:
```python
from objectrest import requests

requests = requests.RequestHandler(base_url="http://rootoftheapi", universal_parameters={'api_key': "thisisanapikey"})

my_object = requests.get_object(url="/object", model=MyObjectClass, params={"limit": 10})
```

# Documentation

Documentation available on [ReadTheDocs](https://objectrest.readthedocs.io/en/latest/documentation.html)