import unittest
from dwolla import fundingsources, rest
from mock import MagicMock


class FundingSourcesTest(unittest.TestCase):
    def setUp(self):
        rest.r._get = MagicMock()
        rest.r._post = MagicMock()
        fundingsources.client_id = "SOME ID"
        fundingsources.client_secret = "SOME ID"
        fundingsources.access_token = "AN OAUTH TOKEN"
        fundingsources.pin = 1234

    def testinfo(self):
        fundingsources.info('123456')
        rest.r._get.assert_any_call('/fundingsources/123456', {'oauth_token': 'AN OAUTH TOKEN'})

    def testget(self):
        fundingsources.get({'a': 'parameter'})
        rest.r._get.assert_any_call('/fundingsources/', {'a': 'parameter', 'oauth_token': 'AN OAUTH TOKEN'})

    def testadd(self):
        fundingsources.add('123456', '654321', 'Checking', 'Unit Test Bank')
        rest.r._post.assert_any_call('/fundingsources/', {'routing_number': '654321', 'account_type': 'Checking', 'oauth_token': 'AN OAUTH TOKEN', 'account_number': '123456', 'account_name': 'Unit Test Bank'})

    def testverify(self):
        fundingsources.verify(0.03, 0.02, '123456')
        rest.r._post.assert_any_call('/fundingsources/123456', {'deposit2': 0.02, 'oauth_token': 'AN OAUTH TOKEN', 'deposit1': 0.03})

    def testwithdraw(self):
        fundingsources.withdraw(20.50, '123456')
        rest.r._post.assert_any_call('/fundingsources/123456/withdraw/', {'amount': 20.5, 'oauth_token': 'AN OAUTH TOKEN', 'pin': 1234})

    def testdeposit(self):
        fundingsources.deposit(30.50, '123456')
        rest.r._post.assert_any_call('/fundingsources/123456/deposit/', {'amount': 30.5, 'oauth_token': 'AN OAUTH TOKEN', 'pin': 1234})


if __name__ == '__main__':
    unittest.main()