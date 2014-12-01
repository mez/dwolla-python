'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  This file contains functionality for all checkouts related endpoints.
  ---------------------------------------------------------------------
  These methods only submit requests to the API, the developer is
  responsible for submitting properly formatted and correct requests.

  Further information is available on: https://docs.dwolla.com
'''

from rest import r


def create(purchaseorder, params=False):
    if not purchaseorder:
        raise Exception('create() requires purchaseorder parameter')
    if type(purchaseorder) is dict:
        if not purchaseorder['destinationId']:
            raise Exception('purchaseorder has no destinationId key')
        if not purchaseorder['total']:
            raise Exception('purchaseorder has no total amount')
    else:
        raise Exception('create() requires purchaseorder to be of type dict')

    p = {
        'client_id': r.settings['client_id'],
        'client_secret': r.settings['client_secret'],
        'purchaseOrder': purchaseorder
    }

    if params:
        p = dict(p.items() + params.items())

    id = r._post('/offsitegateway/checkouts/', p)

    if 'CheckoutId' in id['Response']:
        return dict({'URL': (r.settings['host'] + 'payment/checkout/' + id['Response']['CheckoutId'])}.items() + id.items())
    else:
        raise Exception('Unable to create checkout due to API error.')

def get(id):
    if not id:
        raise Exception('get() requires id parameter')

    return r._get('/offsitegateway/checkouts/' + id,
                     {
                         'client_id': r.settings['client_id'],
                         'client_secret': r.settings['client_secret']
                     })

def complete(id):
    if not id:
        raise Exception('complete() requires id parameter')

    return r._get('/offsitegateway/checkouts/' + id + '/complete/',
                     {
                         'client_id': r.settings['client_id'],
                         'client_secret': r.settings['client_secret']
                     })

def verify(sig, id, amount):
    import hmac
    import hashlib

    if not sig:
        raise Exception('verify() requires sig parameter')
    if not id:
        raise Exception('verify() requires id parameter')
    if not amount:
        raise Exception('verify() requires amount parameter')

    # Normalize amount
    ampstr = '%s&%.2f' % (id, amount)

    # Check signature
    return hmac.new(r.settings['client_secret'], ampstr, hashlib.sha1).hexdigest() == sig






