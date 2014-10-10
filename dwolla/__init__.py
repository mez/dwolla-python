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
        self.settings = settings if settings else _settings.DwollaSettings()
        self.settings.host = self.settings.sandbox_host if self.settings.sandbox else self.settings.production_host

    def _post(self, endpoint, params, customPostfix=False, dwollaParse=True):
        try:
            resp = requests.post(self.settings.host
                                 + customPostfix if customPostfix else self.settings.default_postfix
                                 + endpoint, json.dumps(params))
        except Exception as e:
            if self.settings.debug:
                print "dwolla-python: An error has occured while making a POST request:\n" + e.message

        return resp.json() if resp else ""

