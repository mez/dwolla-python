'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  This file contains functionality for all OAuth related endpoints.
'''

import dwolla


class OAuth(dwolla.DwollaRest):

    def genauthurl(self, redirect=False, scope=False):
        """
        Returns an OAuth permissions page URL. If no redirect is set,
        the redirect in the Dwolla Application Settings will be used.
        If no scope is set, the scope in the settings object will be used.

        :param redirect: String with redirect destination.
        :param scope: OAuth scope string to override default scope in settings object.

        :return: String with URL
        """
        if not scope:
            scope = self.settings['oauth_scope']

        return self.settings['host'] \
        +'oauth/v2/authenticate?client_id=' \
        + self.settings['client_id'] \
        + '&response_type=code&scope=' + scope \
        + ("&redirect_uri=" + redirect if redirect else None)

    def get(self, code, redirect=False):
        """
        Returns an OAuth token + refresh pair in an array. If no redirect
        is set, the redirect in the Dwolla Application Settings will be used.

        :param code: Code from redirect response.
        :param redirect: String with redirect destination.
        :return: Dictionary with access and refresh token pair.
        """
        if not code:
            raise Exception('get() requires code parameter')

        p = {
            'client_id': self.settings['client_id'],
            'client_secret': self.settings['client_secret'],
            'grant_type': 'authorization_code',
            'code': code
        }

        if redirect:
            p['redirect'] = redirect

        return self._post('/token/', p, '/oauth/v2', False)

    def refresh(self, refreshtoken):
        """
        Returns a newly refreshed access token and refresh token pair.

        :param refreshtoken: String with refresh token from initial OAuth handshake.
        :return: Dictionary with access and refresh token pair.
        """
        if not refreshtoken:
            raise Exception('refresh() requires refreshtoken parameter')

        p = {
            'client_id': self.settings['client_id'],
            'client_secret': self.settings['client_secret'],
            'grant_type': 'refresh_token',
            'refresh_token': refreshtoken
        }

        return self._post('/token/', p, '/oauth/v2', False)