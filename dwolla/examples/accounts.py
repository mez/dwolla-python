'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  The following is a quick-start example for the Account class.
'''

import dwolla.accounts as a

# Example 1: Get basic information for a user
# via their Dwolla ID

print a.Accounts.basic('812-121-7199')