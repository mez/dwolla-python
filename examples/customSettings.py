'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  The following is a quick-start example for passing in your
  own settings with dwolla-python.
'''

# Let's import everything from dwolla
import dwolla

# Now we can set our parameters
dwolla.client_id = "My ID"
dwolla.client_secret = "My Secret"


# Example 1: Get basic information for a user via
# their Dwolla ID.

print dwolla.accounts.basic('812-121-7199')

# Example 2: Get full account information for
# the user associated with the current OAuth token

print dwolla.contacts.get
