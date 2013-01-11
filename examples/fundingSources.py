# Include the Dwolla REST Client
from dwolla import DwollaUser

# Include any required keys
import _keys

# Instantiate a new Dwolla User client
# And, Sseed a previously generated access token
DwollaUser = DwollaUser(_keys.token)

'''
    EXAMPLE 1: 
      Fetch all funding sources for the
      account associated with the provided
      OAuth token
'''
sources = DwollaUser.get_funding_sources()
print(sources)


'''
    EXAMPLE 2: 
      Fetch detailed information for the
      funding source with a specific ID
'''
source_id = 'a4946ae2d2b7f1f880790f31a36887f5'
source = DwollaUser.get_funding_source(source_id)
print(source)


'''
    EXAMPLE 3: 
      Initiate a withdraw of 'amount' from
      the the user's Dwolla balance, and into
      the funding source with the given 'source_id'
'''
source_id = 'a4946ae2d2b7f1f880790f31a36887f5'
amount = '1.00'
withdraw = DwollaUser.withdraw(source_id, _keys.pin, amount)
print(withdraw)


'''
    EXAMPLE 4: 
      Initiate a deposit of 'amount' from
      the the user's funding source with the 
      given 'source_id', and into the user's
      Dwolla balance
'''
source_id = 'a4946ae2d2b7f1f880790f31a36887f5'
amount = '1.00'
deposit = DwollaUser.deposit(source_id, _keys.pin, amount)
print(deposit)
