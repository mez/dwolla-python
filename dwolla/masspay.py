'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  This file contains functionality for all MassPay related endpoints.
'''

from rest import r


def create(fundssource, items, params=False):
    """
    Creates a MassPay job. Must pass in an array of items.

    :param fundsSource: String of funding source for jobs.
    :param items: Dictionary with items of type frozenset
    :param params: Dictionary with optional parameters
    :return: None
    """
    if not fundssource:
        raise Exception('create() requires fundssource parameter')
    if not items:
        raise Exception('create() requires items parameter')

    p = {
        'oauth_token': r.settings['oauth_token'],
        'pin': r.settings['pin'],
        'fundsSource': fundssource,
        'items': items
    }

    if params:
        p = dict(p.items() + params.items())

    return r._post('/masspay/', p)


def getjob(id):
    """
    Check the status of an existing MassPay job and
    returns additional information.

    :param id: String with MassPay job ID
    :return: Dictionary with information about the job
    """
    if not id:
        raise Exception('getjob() requires id parameter')

    return r._get('/masspay/' + id, {'oauth_token': r.settings['oauth_token']})


def getjobitems(id, params=False):
    """
    Gets all items for a created MassPay job.

    :param id: String with MassPay job ID
    :param params: Dictionary with additional parameters.
    :return: Dictionary with job items
    """
    if not id:
        raise Exception('getjobitems() requires id parameter')

    p = {'oauth_token': r.settings['oauth_token']}

    if params:
        p = dict(p.items() + params.items())

    return r._get('/masspay/' + id + '/items/', p)


def getitem(jobid, itemid):
    """
    Gets an item from a created MassPay job.

    :param jobid: String with MassPay job ID
    :param itemid: String with item ID.
    :return: Dictionary with information about item from job.
    """
    if not jobid:
        raise Exception('getitem() requires jobid parameter')
    if not itemid:
        raise Exception('getitem() requires itemid parameter')

    return r._get('/masspay/' + jobid + '/items/' + itemid,
                     {'oauth_token': r.settings['oauth_token']})


def listjobs():
    """
    Lists all MassPay jobs for the user
    under the current OAuth token.

    :return: Dictionary with MassPay jobs.
    """
    return r._get('/masspay/', {'oauth_token': r.settings['oauth_token']})