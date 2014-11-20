'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  The following is a quick-start example for the transaction endpoints.
'''

from dwolla import transactions

# Example 1: Send $5.50 to a Dwolla ID.

print transactions.send('812-197-4121', 5.50)

# Example 2: List transactions for the user
# associated with the current OAuth token.

print transactions.get

# Example 3: Refund $2 from "Balance" from transaction
# '123456'

print transactions.refund('123456', 'Balance', 2.00)

# Example 4: Get info for transaction ID '123456'.

print transactions.info('123456')

# Example 5: Get transaction statistics for the user
# associated with the current OAuth token.

print transactions.stats