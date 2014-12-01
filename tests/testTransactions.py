import unittest
from dwolla import transactions, rest
from mock import MagicMock


class TransactionsTest(unittest.TestCase):
    def setUp(self):
        rest.r._get = MagicMock()
        rest.r._post = MagicMock()
        rest.r.settings['client_id'] = "SOME ID"
        rest.r.settings['client_secret'] = "SOME ID"
        rest.r.settings['oauth_token'] = "AN OAUTH TOKEN"
        rest.r.settings['pin'] = 1234

    def testsend(self):
        transactions.send('812-111-1234', 5.00, {'a': 'parameter'})
        print rest.r._post.mock_calls

    def testget(self):
        transactions.get({'another': 'parameter'})
        print rest.r._get.mock_calls

if __name__ == '__main__':
    unittest.main()