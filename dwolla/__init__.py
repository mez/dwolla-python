'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API

  Support is available on our forums at: https://discuss.dwolla.com/category/api-support

  Package -- Dwolla/dwolla-python
  Author -- Dwolla (David Stancu): api@dwolla.com, david@dwolla.com
  Copyright -- Copyright (C) 2014 Dwolla Inc.
  License -- MIT
  Version -- 2.0.0
  Link -- http://developers.dwolla.com
'''

__all__ = ['rest', 'accounts', 'checkouts', 'contacts', 'fundingsources', 'masspay', 'oauth', 'request', 'transactions']

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