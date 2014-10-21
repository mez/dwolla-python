'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  This file contains functionality for all transactions related endpoints.
'''

import dwolla

class Transactions(dwolla.DwollaRest):

    def send(self, destinationid, amount, params=False):
        """
        Sends money to the specified destination user.

        :param destinationid: String of Dwolla ID to send funds to.
        :param amount: Double of amount to send.
        :param params: Dictionary of additional parameters
        :return: Integer of transaction ID
        """
        if not destinationid:
            raise Exception('send() requires destinationid parameter')
        if not amount:
            raise Exception('send() requires amount parameter')

        p = {
            'oauth_token': self.settings['oauth_token'],
            'pin': self.settings['pin'],
            'destinationId': destinationid,
            'amount': amount
        }

        if params:
            p = p.items + params.items

        return self._post('/transactions/send/', p)

    def get(self, params=False):
        """
        Lists transactions for the uer associated with
        the currently set OAuth token.

        :param params: Dictionary with additional parameters
        :return: Dictionary with transactions
        """
        p = {
            'oauth_token': self.settings['oauth_token'],
            'client_id': self.settings['client_id'],
            'client_secret': self.settings['client_secret']
        }

        if params:
            p = p.items + params.items

        return self._get('/transactions/', p)

    def info(self, id):
        """
        Returns transaction information for the transaction
        associated with the passed transaction ID

        :param id: String with transaction ID.
        :return: Dictionary with information about transaction.
        """
        if not id:
            raise Exception('info() requires id parameter')

        return self._get('/transactions/' + id,
                         {
                             'oauth_token': self.settings['oauth_token'],
                             'client_id': self.settings['client_id'],
                             'client_secret': self.settings['client_secret']
                         })

    def refund(self, id, fundingsource, amount, params=False):
        """
        Refunds (either completely or partially) funds to
        the sending user for a transaction.

        :param id: String with transaction ID.
        :param fundingsource: String with funding source for refund transaction.
        :param amount: Double with amount to refund.
        :param params: Dictionary with additional parameters.
        :return: Dictionary with information about refund transaction.
        """
        if not id:
            raise Exception('refund() requires parameter id')
        if not fundingsource:
            raise Exception('refund() requires parameter fundingsource')
        if not amount:
            raise Exception('refund() requires parameter amount')

        p = {
            'oauth_token': self.settings['oauth_token'],
            'pin': self.settings['pin'],
            'fundsSource': fundingsource,
            'transactionId': id,
            'amount': amount
        }

        if params:
            p = p.items + params.items

        return self._post('/transactions/refund/', p)

    def stats(self, params=False):
        """
        Retrieves transaction statistics for
        the user associated with the current OAuth token.

        :param params: Dictionary with additional parameters
        :return: Dictionary with transaction statistics
        """
        p = {
            'oauth_token': self.settings['oauth_token']
        }

        if params:
            p = p.items + params.items

        return self._get('/transactions/stats/', p)