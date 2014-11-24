import unittest
from dwolla import oauth, rest
from mock import MagicMock


class OAuthTest(unittest.TestCase):
    def setUp(self):
        rest.r._get = MagicMock()
        rest.r._post = MagicMock()
        rest.r.settings['client_id'] = "SOME ID"
        rest.r.settings['client_secret'] = "SOME ID"
        rest.r.settings['oauth_token'] = "AN OAUTH TOKEN"
        rest.r.settings['oauth_scope'] = "Balance|AccountInfo"

    def testgenauthurl(self):
        self.assertEqual(oauth.genauthurl(), 'https://uat.dwolla.com/oauth/v2/authenticate?client_id=SOME ID&response_type=code&scope=Balance|AccountInfo')

if __name__ == '__main__':
    unittest.main()