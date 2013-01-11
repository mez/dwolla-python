# Include the Dwolla REST Client
from dwolla import DwollaUser

# Include any required keys
import _keys

# Instantiate a new Dwolla User client
# And, Sseed a previously generated access token
DwollaUser = DwollaUser(_keys.token)

'''
    EXAMPLE 1:
      Get transaction statistics for the
      user with the given OAuth token
'''
stats = DwollaUser.get_transaction_stats()
print stats


'''
    EXAMPLE 2:
      Get a list of recent transactions for 
      the user with the given OAuth token
'''
transactions = DwollaUser.get_transaction_list()
print transactions


'''
    EXAMPLE 3:
      Get detailed information for the transaction
      specified with transaction_id
'''
transaction_id = transactions[0]['Id']
transaction = DwollaUser.get_transaction(transaction_id)
print transaction