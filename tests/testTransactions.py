import unittest
from dwolla import transactions, rest
from mock import MagicMock


class TransTest(unittest.TestCase):
    def setUp(self):
        rest.r._get = MagicMock()
        rest.r._post = MagicMock()
        transactions.client_id = "SOME ID"
        transactions.client_secret = "SOME ID"
        transactions.access_token = "AN OAUTH TOKEN"
        transactions.pin = 1234

    def testsend(self):
        transactions.send('812-111-1234', 5.00, {'a': 'parameter'})
        rest.r._post.assert_any_call('/transactions/send/', {'a': 'parameter', 'destinationId': '812-111-1234', 'oauth_token': 'AN OAUTH TOKEN', 'amount': 5.0, 'pin': 1234})

    def testget(self):
        transactions.get({'another': 'parameter'})
        rest.r._get.assert_any_call('/transactions/', {'client_secret': 'SOME ID', 'oauth_token': 'AN OAUTH TOKEN', 'another': 'parameter', 'client_id': 'SOME ID'})

    def testinfo(self):
        transactions.info('123456')
        rest.r._get.assert_any_call('/transactions/123456', {'client_secret': 'SOME ID', 'oauth_token': 'AN OAUTH TOKEN', 'client_id': 'SOME ID'})

    def testrefund(self):
        transactions.refund('12345', 'Balance', 10.50, {'a': 'parameter'})
        rest.r._post.assert_any_call('/transactions/refund/', {'fundsSource': 'Balance', 'a': 'parameter', 'pin': 1234, 'amount': 10.5, 'oauth_token': 'AN OAUTH TOKEN', 'transactionId': '12345'})

    def teststats(self):
        transactions.stats({'a': 'parameter'})
        rest.r._get.assert_any_call('/transactions/stats/', {'a': 'parameter', 'oauth_token': 'AN OAUTH TOKEN'})

if __name__ == '__main__':
    unittest.main()