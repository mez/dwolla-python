'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  The following is a quick-start example for the account endpoints.
'''

from dwolla import masspay

# Example 1: Create a MassPay job with two items to
# the Balance of the user associated with the current
# OAuth token.

info = masspay.create('Balance',
               {
                   {
                       'amount': 1.00,
                       'destination': '812-197-4121'
                   },
                   {
                       'amount': 2.00,
                       'destination': '812-174-9528'
                   }
               })

print info

# Example 2: Get info regarding the MassPay
# job which you have just created.

print masspay.getjob(info['Id'])

# Example 3: Get all the items submitted with the
# MassPay job which you have just created.

items = masspay.getjobitems(info['Id'])
print items

# Example 4: Get information about the 0th item from
# the MassPay job you just submitted.
#
# Note: You do not need to get all items first, I just
# re-use data for illustrative purposes.

print masspay.getitem(info['Id'], items[0]['ItemId'])

# Example 5: Get all current MassPay jobs for the
# user associated with the current OAuth token.

print masspay.listjobs