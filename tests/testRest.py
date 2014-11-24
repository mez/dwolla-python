import unittest, requests, json
from dwolla import rest
from mock import MagicMock

class RestTest(unittest.TestCase):
    def setUp(self):
        requests.post = MagicMock()
        requests.get = MagicMock()
        json.loads = MagicMock()

    def testpost(self):
        rest.r._post('/some/endpoint', {'key': 'value'}, False, False)
        requests.post.assert_any_call('https://uat.dwolla.com/oauth/rest/some/endpoint',
                                      '{"key": "value"}',
                                      headers={'Content-Type': 'application/json',
                                      'User-Agent': 'dwolla-python/2.x'})

    def testget(self):
        rest.r._get('/another/endpoint', {'another_key': 'another_value'}, False)
        requests.get.assert_any_call('https://uat.dwolla.com/oauth/rest/another/endpoint',
                                      headers={'User-Agent': 'dwolla-python/2.x'},
                                      params={'another_key': 'another_value'})

if __name__ == '__main__':
    unittest.main()