'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  The following is a quick-start example for the OAuth endpoints.
'''

from dwolla import oauth

# Step 1: Generate an OAuth permissions page URL
# with your application's default set redirect.
#
# http://requestb.in is a service that catches
# redirect responses. Go over to their URL and make
# your own so that you may conveniently catch the
# redirect parameters.
#
# You can view your responses at:
# http://requestb.in/[some_id]?inspect
#
# If you're feeling dangerous, feel free to simply use
# http://google.com and manually parse the parameters
# out yourself. The choice remains yours.

print oauth.genauthurl("http://requestb.in/yxlywryx")

# Step 2: The redirect should provide you with a `code`
# parameter. You will now exchange this code for an access
# and refresh token pair.

access_set = oauth.get("Z/KHDIyWO/LboIGn3wGGs1+sRWg=", "http://requestb.in/yxlywryx")
print access_set

# Step 3: Exchange your expiring refresh token for another
# access/refresh token pair.x

print oauth.refresh(access_set['refresh_token'])