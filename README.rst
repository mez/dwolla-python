dwolla-python
=========

[![Build Status](https://travis-ci.org/Dwolla/dwolla-python.svg?branch=master)](https://travis-ci.org/Dwolla/dwolla-python)

The new and improved Dwolla library based off of the Python `requests` client. `dwolla-python` includes support for all API endpoints, and is the new library officially supported by Dwolla.

## Version

2.0.0

## Installation

`dwolla-python` is available on [PyPi](https://pypi.python.org/pypi/dwolla), and therefore can be installed automagically via [pip](https://pip.pypa.io/en/latest/installing.html).

**The Python `requests` library is required for `dwolla-python` to operate. It is included as a dependency on this package if your environment does not already have it.**

*To install:*

```
pip install dwolla 
```

*To add to `requirements.txt` and make this a permanent dependency of your package:*

```requirements.txt
YourApp
SomeLibrary==1.2.3
dwolla>=2.0.0
```

```
pip install -r requirements.txt
```

## Quickstart

`dwolla-python` makes it easy for developers to hit the ground running with our API. Before attempting the following, you should ideally create [an application key and secret](https://www.dwolla.com/applications).

* Change settings in `constants.py` by editing the file, or on-the-fly by doing `from dwolla import constants`, `constants.some_setting = some_value`.
* `from dwolla import module` where `module` is either `accounts`, `checkouts`, `contacts`, `fundingsources`, `masspay`, `oauth`, `request`, or `transactions`, or `from dwolla import *` to import all.
* Use at will!

### Example; Partial Import

`dwolla-python` allows you to import only the modules you need. 

*For this example, we will get information about a Dwolla ID.*

```python
from dwolla import accounts

print accounts.basic('812-121-7199')
```

### Example; Complete Import

`dwolla-python` also allows you to import the entire library to access everything at once.

*For this example, we will get information about a Dwolla ID, as well as request 5.00 from that same ID.*

```python
from dwolla import *

# Get information about the ID

print accounts.basic('812-121-7199')

# Request $5.00 from that ID

print request.create('812-121-7199', 5.00)
```

### Configuration and Use

Whenever you change settings, they will only be partially applied. This means that settings in `constants.py` will remain until they are changed. 

#### Default Settings
```python
client_id = 'YOUR ID HERE'
client_secret = 'YOUR SECRET HERE'
pin = 1234

oauth_scope = 'Send|Transactions|Balance|Request|Contacts|AccountInfoFull|Funding|ManageAccount'
access_token = 'OAUTH TOKENS GO HERE'

# Hostnames, endpoints
production_host = 'https://www.dwolla.com/'
sandbox_host = 'https://uat.dwolla.com/'
default_postfix = 'oauth/rest'

# Client behavior
sandbox = True
debug = True
host = None
rest_timeout = 15
proxy = False
```

#### Proxies

`dwolla-python` also supports proxies. In order to set proxies, you must assign a python dict
