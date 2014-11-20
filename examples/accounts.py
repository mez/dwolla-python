'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  The following is a quick-start example for the account endpoints.
'''

from dwolla import accounts

# Example 1: Get basic information for a user via
# their Dwolla ID

print accounts.basic('812-121-7199')

# Example 2: Get full account information for
# the user associated with the current OAuth token

print accounts.full

# Example 3: Get the balance of the account for
# the user associated with the current OAuth token

print accounts.balance

# Example 4: Get users near a certain geographical
# location

print accounts.nearby(40.7127, 74.0059)

# Example 5: Get the auto-withdrawal status of the user
# associated with the current OAuth token.

print accounts.autowithdrawalstatus

# Example 6: Toggle the auto-withdrawal status of an account
# under the Dwolla user associated with the current OAuth token.

print accounts.toggleautowithdrawalstatus(True, '12345678')