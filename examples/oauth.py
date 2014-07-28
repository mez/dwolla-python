# Include the Flask framework
from flask import Flask, url_for, request, redirect, render_template, session
app = Flask(__name__)

# Include the Dwolla REST Client
from dwolla import DwollaClientApp

# Include any required keys
import _keys

# Instantiate a new Dwolla User client
# And, Seed a previously generated access token
Dwolla = DwollaClientApp(_keys.apiKey, _keys.apiSecret)


'''
    STEP 1: 
      Create an authentication URL
      that the user will be redirected to
'''
@app.route("/")
def index():
    oauth_return_url = url_for('dwolla_oauth_return', _external=True) # Point back to this file/URL
    permissions = 'Send|Transactions|Balance|Request|Contacts|AccountInfoFull'
    authUrl = Dwolla.init_oauth_url(oauth_return_url, permissions)
    return 'To begin the OAuth process, send the user off to <a href="%s">%s</a>' % (authUrl, authUrl)


'''
    STEP 2: 
      Exchange the temporary code given
      to us in the querystring, for
      an expiring OAuth access token and refresh token
'''
@app.route("/dwolla/oauth_return")
def dwolla_oauth_return():
    oauth_return_url = url_for('dwolla_oauth_return', _external=True) # Point back to this file/URL
    code = request.args.get("code")
    info = Dwolla.get_oauth_token(code, redirect_uri=oauth_return_url)
    # Token expiration can be found as parameters in the 'info' array.
    return 'Your expiring OAuth access token is: <b>%s</b>, and refresh token is: <b>%s</b>' % (info['access_token'], info['refresh_token'])

'''
    STEP 3:
      Exchange your expiring OAuth token with a new
      one by providing a refresh token given by
      `get_oauth_token`
'''

@app.route("/dwolla/oauth_refresh")
def dwolla_oauth_refresh():
    oauth_return_url = url_for('dwolla_oauth_return', _external=True) # Point back to this file/URL
    refresh_token = request.args.get("refresh_token")
    info = Dwolla.refresh_auth(refresh_token, redirect_uri=oauth_return_url)
    # Token expiration can be found as parameters in the 'info' array.
    return 'Your expiring OAuth access token is: <b>%s</b>, and refresh token is: <b>%s</b>' % (info['access_token'], info['refresh_token'])


# Run the app
if __name__ == "__main__":
    app.run(debug=True)