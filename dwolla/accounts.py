'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  This file contains functionality for all accounts related endpoints.
'''

import dwolla


class Accounts(dwolla.DwollaRest):
    def balance(self):
        """
        Gets balance for the account associated with the
        currently set OAuth token.

        :return: Balance
        """
        return self._get('/balance', {'oauth_token': self.settings['oauth_token']})
