import unittest
from dwolla import request, rest
from mock import MagicMock


class RequestTest(unittest.TestCase):
    def setUp(self):
        rest.r._get = MagicMock()
        rest.r._post = MagicMock()
        rest.r.settings['client_id'] = "SOME ID"
        rest.r.settings['client_secret'] = "SOME ID"
        rest.r.settings['oauth_token'] = "AN OAUTH TOKEN"

    def testcreate(self):
        request.create('812-123-1234', 5.50, {'a': 'parameter'})
        rest.r._post.assert_any_call('/requests/', {'sourceId': '812-123-1234', 'a': 'parameter', 'amount': 5.5, 'oauth_token': 'AN OAUTH TOKEN'})

    def testget(self):
        request.get({'another': 'parameter'})
        rest.r._get.assert_any_call('/requests/', params={'oauth_token': 'AN OAUTH TOKEN', 'another': 'parameter'})

    def testinfo(self):
        request.info('654321')
        rest.r._get.assert_any_call('/requests/654321', params={'oauth_token': 'AN OAUTH TOKEN'})

    def testcancel(self):
        request.cancel('12345')
        rest.r._post.assert_any_call('/requests/12345/cancel/', params={'oauth_token': 'AN OAUTH TOKEN'})

    def testfulfill(self):
        request.fulfill('12345', 13.37, {'a': 'parameter'})
        rest.r._post.assert_any_call('/requests/12345/fulfill', {'a': 'parameter', 'oauth_token': 'AN OAUTH TOKEN'})

if __name__ == '__main__':
    unittest.main()