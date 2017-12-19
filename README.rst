A client to access to Digitick online shop API
==============================================

This project provides a swagger-generated API access for the digitick online shops.

This project **IS NOT** a digitick official product.

Installation
------------

The project can be installed with pip::

   $ pip install digitick-client


API access
----------

You have to get a token to access to the API functions::

    import base64
    from digitick_client import api_client
    from digitick_client.rest import ApiException


    api_instance = api_client.AuthorizationApi()
    login, password = 'foo', 'bar'  # You have to provide login and password !
    str_key = bytes(('%s:%s' % (self._username, self._password)), encoding='utf-8')
    auth_key = base64.b64encode(str_key)
    try:
        api_response = api_instance.authorize(auth_key)
    except ApiException as e:
        print ('Unable to authenticate user with login %s on api' % login)


