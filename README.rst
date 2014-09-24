dwolla-python
=============

Official Python wrapper for Dwolla's API

Version
-------

1.6.6

Requirements
------------

-  `Python <http://www.python.org/>`__
-  `Dwolla Application <https://www.dwolla.com/applications>`__

Installation
------------

Automatic installation using `pip <http://pypi.python.org/pypi>`__:

::

    pip install dwolla

Usage
-----

.. code:: python

    from dwolla import DwollaUser
    DwollaUser = DwollaUser('[OAuth Token Goes Here]')

    transactionId = DwollaUser.send_funds(1.00, '812-626-8794', '[PIN]')
    print transactionId

Examples / Quickstart
---------------------

To use the examples in the /examples folder, first edit the \_keys.py
file and add your Dwolla API application's key, and secret, along with
your account's `OAuth
token <https://developers.dwolla.com/dev/token>`__, and PIN.

This repo includes various usage examples, including:

-  Authenticating with OAuth [oauth.py]
-  Sending money [send.py]
-  Fetching account information [accountInfo.py]
-  Grabbing a user's contacts [contacts.py]
-  Listing a user's funding sources [fundingSources.py]
-  Creating offsite gateway sessions [offsiteGateway.py]
-  Registering a new Dwolla user account [registerUser.py]
-  Handling money requests [request.py]

Environment Variables
---------------------

-  ``DWOLLA_VERIFY_SSL`` (optional; True/False) Should we verify
   Dwolla's SSL?
-  ``DWOLLA_DEBUG`` (optional; True/False) Enable verbose debug?
-  ``DWOLLA_SANDBOX`` (optional; True/False) Use Dwolla's UAT env?
-  ``DWOLLA_API_HOST`` (optional; String/URL) A custom API host URL;
   defaults to https://www.dwolla.com/

Instantiation Variables
-----------------------

If an application makes it difficult to use environment variables to set
parameters, each of the aforementioned variables can be put into a
Python ``dict`` upon instantiation of ``DwollaGateway()``,
``DwollaClientApp()``, and ``DwollaUser()``.

.. code:: python

    {
        'VERIFY_SSL': True,
        'DEBUG': True,
        'SANDBOX': True,
        'HOST': 'https://somecustomhost.thatyouprobablywontset.dwolla.com'
    }

Let's take the previous example from the Usage section, and make our
requests target the UAT environment via instantiation variables:

.. code:: python

    from dwolla import DwollaUser
    DwollaUser = DwollaUser('[OAuth Token Goes Here]', {'SANDBOX': True})

    transactionId = DwollaUser.send_funds(1.00, '812-626-8794', '[PIN]')
    print transactionId

Methods
-------

DwollaClientApp class:

::

    init_oauth_url(redircet_uri, scope) ==> (string) OAuth permissions page URL
    get_oauth_token(code)               ==> (string) a never-expiring OAuth access token
    get_account_info(account_id)        ==> (array) the user entity for {account_id}
    get_nearby_spots([lat, lon, range, limit])  ==> (array) list of nearby spots matching the search criteria
    register_user(email, password, pin, firstName, lastName, address, address2, city, state, zip, phone, dateOfBirth[, organization, ein, type, acceptTerms])   ==> (dict) the newly created user record

DwollaUser class:

::

    get_balance()                           ==> (string) the Dwolla balance of the account associated with the token
    get_account_info(account_id)            ==> (dict) the user entity associated with the token
    get_nearby_users(lat, lon)
    get_contacts([search, types, limit])    ==> (array) list of contacts matching the search criteria

    get_transaction(transaction_id)         ==> (dict) transaction details
    get_transaction_list([since, types, limit, skip])       ==> (array) a list of recent transactions matching the search criteria
    get_transaction_stats([types, start_date, end_date])    ==> (dict) statistics about the account associated with the token
    send_funds(amount, dest, pin[, notes, assume_cost, facil_amount, dest_type])    ==> (string) transaction ID

    request_funds(amount, source, pin[, notes, facil_amount, source_type])          ==> (string) request ID
    fulfill_request(request_id, pin[, amount, notes, funds_source, assume_cost])
    cancel_request(request_id)
    get_request(request_id)
    get_pending_requests()

    get_funding_sources()   ==> (array) a list of funding sources associated with the token
    get_funding_source(id)  ==> (dict) information about the {id} funding source
    add_funding_source(routing_number, account_number, account_type, account_name)
    verify_funding_source(source_id, deposit1, deposit2)
    withdraw(source_id, pin, amount)
    deposit(source_id, pin, amount)

DwollaGateway class:

::

    set_mode(mode)          ==> (bool) did mode change?
    start_gateway_session() ==> (bool) did session start?
    add_gateway_product(name, amount[, desc, qty])              ==> (bool) was product added?
    verify_gateway_signature(signature, checkout_id, amount)    ==> (bool) is signature valid?
    get_gateway_URL(destination_id[, order_id, discount, shipping, tax, notes, callback])    ==> (string) checkout URL

Changelog
---------

1.6.5

-  Fixed PyPi issue with README error on install. README on PyPi is of
   fully compliant RST format and no longer a symlink.

1.6.4

-  Updated a payment and request response to use HOST variable instead
   of hardcoded string (should now work with UAT)

1.6.3

-  Fix an issue with the verify\_ssl variable

1.6.2

-  Add verify\_webhook\_signature method

1.6.1

-  Add the AllowGuestCheckout flag to the offiste gateway

1.6.0

-  Add refund API endpoint

1.5.1

-  Fixed float(amount) bug - `Pull
   req <https://github.com/Dwolla/dwolla-python/pull/6>`__ by
   [@anfedorov](https://github.com/anfedorov)
-  Fix timing vulnerability in verify\_gateway\_signature - `Pull
   req <https://github.com/Dwolla/dwolla-python/pull/3>`__ by
   [@anfedorov](https://github.com/anfedorov)
-  DwollaGateway.\ **init** shouldn't require redirect\_uri -
   `Issue <https://github.com/Dwolla/dwolla-python/issues/4>`__ by
   [@anfedorov](https://github.com/anfedorov)

1.5.0

-  Add support for Dwolla's UAT

1.4.9

-  Remove PIN requirement on def request()

1.4.8

-  Added Guest Checkout flag to get\_gateway\_URL() (Thanks, @pegler)

1.4.7

-  Fixed endpoint URLs

1.4.6

-  Removed unwanted print statements

1.4.5

-  Add support for SSL verification override

1.4.4

-  Add support for host override

1.4.3

-  Fixed docs for the transaction/listings() delimiter (Thanks,
   @klobyone)

1.4.2

-  Fixed wrong parameter name in add\_funding\_source() (Thanks
   @Louis11)
-  Fixed typos in example files

1.4.1

-  Fix for assume\_cost parameter

1.4

-  Implement add\_funding\_source
-  Implement verify\_funding\_source
-  Implement withdraw
-  Implement deposit
-  Implement get\_nearby\_users
-  Implement fulfill\_request
-  Implement cancel\_request
-  Implement get\_request
-  Implement get\_pending\_requests
-  Add example code for fundingSources.py
-  Add example code for request.py

1.3.4

-  Verify SSL certificate

Credits
-------

This wrapper is a forked extension of Thomas Hansen's 'dwolla-python'
module.

-  Thomas Hansen <thomas.hansen@gmail.com>
-  Jordan Bouvier <jbouvier@gmail.com>
-  Michael Schonfeld <michael@dwolla.com>
-  George Sibble <george.sibble@ultapay.com>
-  Andrey Fedorov <anfedorov@gmail.com>

Support
-------

-  Dwolla API <api@dwolla.com>
-  Michael Schonfeld <michael@dwolla.com>

References / Documentation
--------------------------

http://developers.dwolla.com/dev

License
-------

(The MIT License)

Copyright (c) 2012 Dwolla <michael@dwolla.com>

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.