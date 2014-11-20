'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  The following is a quick-start example for the request endpoints.
'''

from dwolla import request

# Example 1: Request $5 from 812-740-3809

print request.create('812-740-3809', 5.00)

# Example 2: Get all pending requests from the user
# associated with the current OAuth token.

print request.get

# Example 3: Get info regarding a pending money request.

print request.info(1470)

# Example 4: Cancel a pending money request.

print request.cancel(1470)

# Example 5: Fulfill a pending money request.

print request.fulfill(1475, 10.00)