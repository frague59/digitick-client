A client to access to Digitick online shop API
**********************************************

This project provides a swagger-generated API access for the digitick online shops.

This project **IS NOT** a digitick official product.

Installation
============

The project can be installed with pip::

   $ pip install digitick-client


API access
==========

Authorization
-------------

You have to get a token to access to the API functions::

    import sys
    import base64
    from digitick_client import api_client
    from digitick_client.rest import ApiException

    HOST = "https://api.digitick.com"


    def main(args):
        api = api_client.ApiClient(host=HOST)
        login, password = 'foo', 'bar'
        access_token = connect(api, login, password)
        api.access_token = access_token


    def connect(api, login, password):
        api_instance = api_client.AuthorizationApi(api_client=api)
        login, password = 'foo', 'bar'  # You have to provide login and password !
        str_key = bytes(('%s:%s' % (self._username, self._password)), encoding='utf-8')
        auth_key = base64.b64encode(str_key)
        try:
            api_response = api_instance.authorize(auth_key)
        except ApiException as e:
            print ('Unable to authenticate user with login %s on api' % login)
            raise  # Re raise the exception
        else:
            if api_response.access_token is None:
                raise AttributeException('`access_token` not initialized.')
            return api_response.access_token

    if __name__ == "__main__":
        main(sys.argv[1:])


List events
-----------

Events listing uses the access token built from previous method::

