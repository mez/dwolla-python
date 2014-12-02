import unittest
import dwolla

from mock import MagicMock


class AccountsTest(unittest.TestCase):
    def setUp(self):
        dwolla.rest.r._get = MagicMock()
        dwolla.rest.r._post = MagicMock()
        dwolla.client_id = "SOME ID"
        dwolla.client_secret = "SOME ID"
        dwolla.access_token = "AN OAUTH TOKEN"

    def testbasic(self):
        dwolla.accounts.basic('123456')
        print dwolla.rest.r._get.mock_calls
        dwolla.rest.r._get.assert_any_call('/users/123456', {'client_secret': 'SOME ID', 'client_id': 'SOME ID'})

    def testfull(self):
        dwolla.accounts.full()
        dwolla.rest.r._get.assert_any_call('/users/', {'oauth_token': 'AN OAUTH TOKEN'})

    def testbalance(self):
        dwolla.accounts.balance()
        dwolla.rest.r._get.assert_any_call('/balance/', {'oauth_token': 'AN OAUTH TOKEN'})

    def testnearby(self):
        dwolla.accounts.nearby(45, 50)
        dwolla.rest.r._get.assert_any_call('/users/nearby/', {'latitude': 45, 'client_secret': 'SOME ID', 'longitude': 50, 'client_id': 'SOME ID'})

    def testautowithdrawalstatus(self):
        dwolla.accounts.autowithdrawalstatus()
        dwolla.rest.r._get.assert_any_call('/accounts/features/auto_withdrawl/', {'oauth_token': 'AN OAUTH TOKEN'})

    def testtoggleautowithdrawalstatus(self):
        dwolla.accounts.toggleautowithdrawalstatus(True, '123456')
        dwolla.rest.r._post.assert_any_call('/accounts/features/auto_withdrawl', {'enabled': True, 'oauth_token': 'AN OAUTH TOKEN', 'fundingId': '123456'})


if __name__ == '__main__':
    unittest.main()