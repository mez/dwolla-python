# Include the Dwolla REST Client
from dwolla import DwollaClientApp, DwollaUser

# Include any required keys
import _keys

# Instantiate a new Dwolla User client
# And, Seed a previously generated access token
DwollaUser = DwollaUser(_keys.token)

'''
    EXAMPLE 1: 
      Get the Dwolla balance for the user
      with the given OAuth token
'''
balance = DwollaUser.get_balance()
print(balance)
