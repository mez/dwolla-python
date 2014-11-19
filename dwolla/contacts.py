'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  This file contains functionality for all contact related endpoints.
'''

import dwolla

class Contacts(dwolla.Rest):

    def get(self, params=False):
        """
        Get contacts from user associated with OAuth token.

        :param params: Dictionary with additional parameters.
        :return: Dictionary with contacts.
        """
        p = {'oauth_token': self.settings['oauth_token']}

        if params:
            p = (p.items + params.items)

        return self._get('/contacts/', p)

    def nearby(self, lat, lon, params=False):
        """
        Returns Dwolla spots near the specified geographical location.

        :param lat: Double of latitudinal coordinates.
        :param lon: Double of longitudinal coordinates.
        :param params: Dictionary with additional parameters.
        :return: Dictionary with spots.
        """
        if not lat:
            raise Exception('nearby() requires lat parameter')
        if not lon:
            raise Exception('nearby() requires lon parameter')

        p = {
            'client_id': self.settings['client_id'],
            'client_secret': self.settings['client_secret'],
            'latitude': lat,
            'longitude': lon
        }

        if params:
            p = (p.items + params.items)

        return self._get('/contacts/nearby/', p)