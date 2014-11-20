'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  The following is a quick-start example for the contacts endpoints.
'''

from dwolla import contacts

# Example 1: Get the first 10 contacts from the user
# associated with the current OAuth token.

print contacts.get()

# Example 2: Get the first 2 contacts from the user
# associated with the current OAuth token.

print contacts.get({'limit': 2})

# Example 3: Get Dwolla spots near NYC's official
# coordinates.

print contacts.nearby(40.7127, 74.0059)