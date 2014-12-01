'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  The following is a quick-start example for passing in your
  own settings dictionary with dwolla-python.
'''

# We now also import rest
from dwolla import accounts, contacts, rest

# These are our settings, change at will.
mySettings = {

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

}

# Replace rest.r with a new Rest class using the above settings
# Now, you can use *any* module without having to repeat this step.

rest.r = rest.Rest(mySettings)

# Example 1: Get basic information for a user via
# their Dwolla ID.

print accounts.basic('812-121-7199')

# Example 2: Get full account information for
# the user associated with the current OAuth token

print contacts.get
