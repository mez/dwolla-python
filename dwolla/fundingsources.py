'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  This file contains functionality for all funding source related endpoints.
'''

from constants import *
from rest import r


def info(fid, access_token=False):
    """
    Retrieves information about a funding source by ID.

    :param fid: String of funding ID of account to retrieve information for.
    :return: Dictionary with funding ID info.
    """
    if not fid:
        raise Exception('info() requires fid parameter')

    return r._get('/fundingsources/' + fid, {'oauth_token': access_token if access_token else access_token})


def get(params=False, access_token=False):
    """
    Returns a list of funding sources associated to the account
    under the current OAuth token.

    :param params: Dictionary with additional parameters.
    :return: Dictionary of funding sources.
    """
    p = {'oauth_token': access_token if access_token else access_token}

    if params:
        p = dict(params.items() + p.items())

    return r._get('/fundingsources/', p)


def add(account, routing, type, name, access_token=False):
    """
    Adds a funding source to the account under the current
    OAuth token.

    :param account: String with account number.
    :param routing: String with routing number.
    :param type: String with account type.
    :param name: String with user defined name for account.
    :return: None
    """
    if not account:
        raise Exception('add() requires account parameter')
    if not routing:
        raise Exception('add() requires routing parameter')
    if not type:
        raise Exception('add() requires type parameter')
    if not name:
        raise Exception('add() requires name parameter')

    return r._post('/fundingsources/',
                   {
                       'oauth_token': access_token if access_token else access_token,
                       'account_number': account,
                       'routing_number': routing,
                       'account_type': type,
                       'account_name': name
                   })


def verify(d1, d2, fid, access_token=False):
    """
    Verifies a funding source for the account associated
    with the funding ID under the current OAuth token via
    the two micro-deposits.
    :param d1: Double of first micro-deposit
    :param d2: Double of second micro-deposit
    :param fid: String with funding ID.
    :return: None
    """
    if not d1:
        raise Exception('verify() requires d1 parameter')
    if not d2:
        raise Exception('verify() requires d2 parameter')
    if not fid:
        raise Exception('verify() requires fid parameter')

    return r._post('/fundingsources/' + fid,
                   {
                       'oauth_token': access_token if access_token else access_token,
                       'deposit1': d1,
                       'deposit2': d2
                   })


def withdraw(amount, fid, access_token=False, pin=False):
    """
    Withdraws funds from a Dwolla account to the funding source
    associated with the passed ID, under the account associated
    with the current OAuth token.

    :param amount: Double with amount to withdraw.
    :param fid: String with funding ID to withdraw to.
    :return: None
    """
    if not amount:
        raise Exception('withdraw() requires amount parameter')
    if not fid:
        raise Exception('withdraw() requires fid parameter')

    return r._post('/fundingsources/'+ fid + '/withdraw/',
                   {
                       'oauth_token': access_token if access_token else access_token,
                       'pin': pin if pin else pin,
                       'amount': amount
                   })


def deposit(amount, fid, access_token=False, pin=False):
    """
    Deposits funds into the Dwolla account associated with the
    OAuth token from the funding ID associated with the passed
    ID.

    :param amount: Double with amount to deposit.
    :param fid: String with funding ID to deposit from.
    :return: None
    """
    if not amount:
        raise Exception('deposit() requires amount parameter')
    if not fid:
        raise Exception('deposit() requires fid parameter')

    return r._post('/fundingsources/' + fid + '/deposit/',
                   {
                       'oauth_token': access_token if access_token else access_token,
                       'pin': pin if pin else pin,
                       'amount': amount
                   })
