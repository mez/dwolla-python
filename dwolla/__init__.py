'''
      _               _ _
   __| |_      _____ | | | __ _
  / _` \ \ /\ / / _ \| | |/ _` |
 | (_| |\ V  V / (_) | | | (_| |
  \__,_| \_/\_/ \___/|_|_|\__,_|

  An official requests based wrapper for the Dwolla API

  Support is available on our forums at: https://discuss.dwolla.com/category/api-support

  Package -- Dwolla/dwolla-python
  Author -- Dwolla (David Stancu): api@dwolla.com, david@dwolla.com
  Copyright -- Copyright (C) 2014 Dwolla Inc.
  License -- MIT
  Version -- 2.0.0
  Link -- http://developers.dwolla.com
'''

import requests
import json

import _settings

class RestClient():
    def __init__(self, settings=False):
        """
        Constructor.

        :param settings: Dictionary with custom settings if
                         using _settings.py is not desired
        :return: None (__new__() returns the new instance ;))
        """
        self.settings = settings if settings else _settings.DwollaSettings()
        self.settings.host = self.settings.sandbox_host if self.settings.sandbox else self.settings.production_host

    def _parse(self, response):
        """
        Parses the Dwolla API response.

        :param response: Dictionary with content of API response.
        :return: Usually either a string or a dictionary depending
                 the on endpoint accessed.
        """
        if json['Success'] is not True:
            raise Exception("dwolla-python: An API error was encountered.\nServer Message:\n" + response['Message'])
        else:
            return response['Response']

    def _post(self, endpoint, params, customPostfix=False, dwollaParse=True):
        """
        Wrapper for requests' POST functionality.

        :param endpoint: String containing endpoint desired.
        :param params: Dictionary containing parameters for request.
        :param customPostfix: String containing custom OAuth postfix (for special endpoints).
        :param dwollaParse: Boolean deciding whether or not to call self._parse().
        :return: Dictionary String containing endpoint desired. containing API response.
        """
        try:
            resp = requests.post(self.settings.host
                                 + customPostfix if customPostfix else self.settings.default_postfix
                                 + endpoint, json.dumps(params))
        except Exception as e:
            if self.settings.debug:
                print "dwolla-python: An error has occurred while making a POST request:\n" + e.message

        return self._parse(json.loads(resp.json())) if dwollaParse else json.loads(resp.json())

    def _get(self, endpoint, params, dwollaParse=True):
        """
        Wrapper for requests' GET functionality.

        :param endpoint: String containing endpoint desired.
        :param params: Dictionary containing parameters for request
        :param dwollaParse: Boolean deciding whether or not to call self._parse().
        :return: Dictionary String containing endpoint desired. containing API response.
        """
        try:
            resp = requests.get(self.settings.host + self.settings.default_postfix + endpoint, params)
        except Exception as e:
            if self.settings.debug:
                print "dwolla-python: An error has occurred while making a GET request:\n" + e.message

        return self._parse(json.loads(resp.json())) if dwollaParse else json.loads(resp.json())
