import unittest
from dwolla import checkouts, rest
from mock import MagicMock


class TransactionsTest(unittest.TestCase):
    def setUp(self):
        rest.r._get = MagicMock()
        rest.r._post = MagicMock()

        rest.r._post.return_value = dict({'Response': {'CheckoutId': 'TEST'}})

        rest.r.settings['client_id'] = "SOME ID"
        rest.r.settings['client_secret'] = "SOME ID"
        rest.r.settings['oauth_token'] = "AN OAUTH TOKEN"
        rest.r.settings['pin'] = 1234

    def testcreate(self):
        checkouts.create({
            'orderItems': {
                frozenset({
                    'name': 'Prime Rib Sandwich',
                    'description': 'A somewhat tasty non-vegetarian sandwich',
                    'quantity': '1',
                    'price': '15.00'
                })
            },
            'destinationId': '812-740-4294',
            'total': 15.00,
            'notes': 'blahhh',
            'metadata': frozenset({
                'key1': 'something',
                'key2': 'another thing'
            })})
        rest.r._post.assert_any_call('/offsitegateway/checkouts/', {'client_secret': 'SOME ID', 'purchaseOrder': {'destinationId': '812-740-4294', 'total': 15.0, 'notes': 'blahhh', 'orderItems': set([frozenset(['price', 'description', 'name', 'quantity'])]), 'metadata': frozenset(['key2', 'key1'])}, 'client_id': 'SOME ID'})

    def testget(self):
        checkouts.get('123456')
        rest.r._get.assert_any_call('/offsitegateway/checkouts/123456', {'client_secret': 'SOME ID', 'client_id': 'SOME ID'})

    def testcomplete(self):
        checkouts.complete('123456')
        print rest.r._get.assert_any_call('/offsitegateway/checkouts/123456/complete/', {'client_secret': 'SOME ID', 'client_id': 'SOME ID'})

if __name__ == '__main__':
    unittest.main()