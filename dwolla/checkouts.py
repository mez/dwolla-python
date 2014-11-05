'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API.

  This file contains functionality for all checkouts related endpoints.
'''

import dwolla


class Checkouts(dwolla.DwollaRest):
    def __init__(self):
        self.cart = False

    def resetcart(self):
        self.cart = False

    def addtocart(self, name, desc, cost, quantity):
        if not name:
            raise Exception('addtocart() requires name parameter')
        if not desc:
            raise Exception('addtocart() requires desc parameter')
        if not cost:
            raise Exception('addtocart() requires cost parameter')
        if not quantity:
            raise Exception('addtocart() requires quantity parameter')

        if not self.cart:
            self.cart = []

        self.cart.append({
            'name': name,
            'description': desc,
            'price': cost,
            'quantity': quantity
        })

    def create(self, purchaseorder, params=False):
        if not purchaseorder:
            raise Exception('create() requires purchaseorder parameter')
        if type(purchaseorder) is dict:
            if not purchaseorder['destinationId']:
                raise Exception('purchaseorder has no destinationId key')
            if not self.cart and not purchaseorder['total']:
                raise Exception('purchaseorder has no total amount')
        else:
            raise Exception('create() requires purchaseorder to be of type dict')

        p = {
            'client_id': self.settings['client_id'],
            'client_secret': self.settings['client_secret'],
            'purchaseOrder': purchaseorder
        }

        if self.cart:
            p['purchaseOrder']['total'] = 0
            for item in self.cart:
                p['purchaseOrder']['total'] += (item['price'] * item['quantity'])
            p['purchaseOrder']['orderItems'] = self.cart

        if not p['purchaseOrder']['total']:
            for item in p['purchaseOrder']['orderItems']:
                p['purchaseOrder']['total'] += (item['price'] * item['quantity'])

        if 'tax' in p['purchaseOrder']:
            p['purchaseOrder']['total'] += p['purchaseOrder']['tax']
        if 'shipping' in p['purchaseOrder']:
            p['purchaseOrder']['total'] += p['purchaseOrder']['shipping']

        if 'discount' in p['purchaseOrder']:
            if p['purchaseOrder']['discount'] > 0:
                p['purchaseOrder']['total'] -= p['purchaseOrder']['discount']
            else:
                p['purchaseOrder']['total'] += p['purchaseOrder']['discount']

        p['purchaseOrder']['total'] = "{0:.2f}".format(p['purchaseOrder']['total'])

        if params:
            p = p.items + params.items

        id = self._post('/offsitegateway/checkouts/', p)

        if 'CheckoutId' in id:
            return {'URL': self.settings['host'] + 'payment/checkout/' + id['CheckoutId']}.items + id.items
        else:
            raise Exception('Unable to create checkout due to API error.')

    def get(self, id):
        if not id:
            raise Exception('get() requires id parameter')

        return self._get('/offsitegateway/checkouts/' + id,
                         {
                             'client_id': self.settings['client_id'],
                             'client_secret': self.settings['client_secret']
                         })

    def complete(self, id):
        if not id:
            raise Exception('complete() requires id parameter')

        return self._get('/offsitegateway/checkouts/' + id + '/complete/',
                         {
                             'client_id': self.settings['client_id'],
                             'client_secret': self.settings['client_secret']
                         })

    def verify(self, sig, id, amount):
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
        return hmac.new(self.settings['client_secret'], ampstr, hashlib.sha1).hexdigest() == sig






