'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API

  This contains the default settings for the library; you can modify
  these values or use this dictionary as a boilerplate for your own settings values.
'''

s = {

    'client_id': 'YOUR ID HERE',
    'client_secret': 'YOUR SECRET HERE',
    'pin': 1234,

    'oauth_scope': 'Send|Transactions|Balance|Request|Contacts|AccountInfoFull|Funding|ManageAccount',
    'oauth_token': 'OAUTH TOKENS GO HERE',
    'refresh_token': 'REFRESH TOKENS GO HERE',

    # Hostnames, endpoints
    'production_host': 'https://www.dwolla.com/',
    'sandbox_host': 'https://uat.dwolla.com/',
    'default_postfix': 'oauth/rest',

    # Client behavior
    'sandbox': True,
    'debug': True,
    'host': None,
    'rest_timeout': 15,
    'proxy': False

    # Proxy must be set to a dictionary in this manner as per requests'
    # requirements:
    # {
    # 'http'  : 'http://someproxy:someport',
    # 'https' : 'https://someproxy:someport',
    # 'ftp'   : 'ftp://someproxy:someport'
    # }
}
