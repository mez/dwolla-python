# Include the Dwolla REST Client
from dwolla import DwollaUser

# Include any required keys
import _keys

# Instantiate a new Dwolla User client
# And, Sseed a previously generated access token
DwollaUser = DwollaUser(_keys.token)


'''
    EXAMPLE 1:
      Get a list of pending requests
      for the user with the given oauth token
'''
pending_requests = DwollaUser.get_pending_requests()
print(pending_requests)


'''
    EXAMPLE 2:
      Get detailed information for the request
      with the given 'request_id'
'''
request_id = '2209516'
request = DwollaUser.get_request(request_id)
print(request)


'''
    EXAMPLE 3:
      Initiate a money request
'''
request = DwollaUser.request_funds('1.00', 'reflector@dwolla.com', _keys.pin, source_type='Email')
print(request)


'''
    EXAMPLE 4:
      Cancel a pending money request
'''
request_id = request
canceled_request = DwollaUser.cancel_request(request_id)
print(canceled_request)


'''
    EXAMPLE 5:
      Fulfill (:pay) a pending payment request
'''
request_id = '2214710'
fulfilled_request = DwollaUser.fulfill_request(request_id, _keys.pin)
print(fulfilled)
