import unittest
from dwolla import masspay, rest
from mock import MagicMock


class MassPayTest(unittest.TestCase):
    def setUp(self):
        rest.r._get = MagicMock()
        rest.r._post = MagicMock()
        masspay.client_id = "SOME ID"
        masspay.client_secret = "SOME ID"
        masspay.access_token = "AN OAUTH TOKEN"
        masspay.pin = 1234

    def testcreate(self):
        masspay.create('Balance', {frozenset({'amount': 10.00, 'destination': '812-123-1111'})})
        rest.r._post.assert_any_call('/masspay/', {'fundsSource': 'Balance', 'items': set([frozenset(['amount', 'destination'])]), 'oauth_token': 'AN OAUTH TOKEN', 'pin': 1234})

    def testgetjob(self):
        masspay.getjob('123456')
        rest.r._get.assert_any_call('/masspay/123456', {'oauth_token': 'AN OAUTH TOKEN'})

    def testgetjobitems(self):
        masspay.getjobitems('1234567', {'a': 'parameter'})
        rest.r._get.assert_any_call('/masspay/1234567/items/', {'a': 'parameter', 'oauth_token': 'AN OAUTH TOKEN'})

    def testgetitem(self):
        masspay.getitem('123', '456')
        rest.r._get.assert_any_call('/masspay/123/items/456', {'oauth_token': 'AN OAUTH TOKEN'})

    def testlistjobs(self):
        masspay.listjobs()
        rest.r._get.assert_any_call('/masspay/', {'oauth_token': 'AN OAUTH TOKEN'})

if __name__ == '__main__':
    unittest.main()