# coding: utf-8

"""
    Digitick REST API

    The Digitick REST API is a set of methods giving access to catalog, user and cart management.

    OpenAPI spec version: v1.0
    Contact: contact@digitick.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ShowsResponseInner(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'start': 'str',
        'end': 'str',
        'venue': 'str',
        'address': 'str',
        'zip_code': 'str',
        'city': 'str',
        'country_id': 'int',
        'number_of_prices': 'int',
        'min_price_cents': 'int',
        'max_price_cents': 'int',
        'reserved_seats': 'bool',
        'plan_url': 'str',
        'plan_last_change': 'str',
        'status': 'int',
        'sales_start': 'str',
        'sales_end': 'str',
        'is_exclu': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'start': 'start',
        'end': 'end',
        'venue': 'venue',
        'address': 'address',
        'zip_code': 'zipCode',
        'city': 'city',
        'country_id': 'countryId',
        'number_of_prices': 'numberOfPrices',
        'min_price_cents': 'minPriceCents',
        'max_price_cents': 'maxPriceCents',
        'reserved_seats': 'reservedSeats',
        'plan_url': 'planUrl',
        'plan_last_change': 'planLastChange',
        'status': 'status',
        'sales_start': 'salesStart',
        'sales_end': 'salesEnd',
        'is_exclu': 'isExclu'
    }

    def __init__(self, id=None, start=None, end=None, venue=None, address=None, zip_code=None, city=None, country_id=None, number_of_prices=None, min_price_cents=None, max_price_cents=None, reserved_seats=None, plan_url=None, plan_last_change=None, status=None, sales_start=None, sales_end=None, is_exclu=None):
        """
        ShowsResponseInner - a model defined in Swagger
        """

        self._id = None
        self._start = None
        self._end = None
        self._venue = None
        self._address = None
        self._zip_code = None
        self._city = None
        self._country_id = None
        self._number_of_prices = None
        self._min_price_cents = None
        self._max_price_cents = None
        self._reserved_seats = None
        self._plan_url = None
        self._plan_last_change = None
        self._status = None
        self._sales_start = None
        self._sales_end = None
        self._is_exclu = None

        if id is not None:
          self.id = id
        if start is not None:
          self.start = start
        if end is not None:
          self.end = end
        if venue is not None:
          self.venue = venue
        if address is not None:
          self.address = address
        if zip_code is not None:
          self.zip_code = zip_code
        if city is not None:
          self.city = city
        if country_id is not None:
          self.country_id = country_id
        if number_of_prices is not None:
          self.number_of_prices = number_of_prices
        if min_price_cents is not None:
          self.min_price_cents = min_price_cents
        if max_price_cents is not None:
          self.max_price_cents = max_price_cents
        if reserved_seats is not None:
          self.reserved_seats = reserved_seats
        if plan_url is not None:
          self.plan_url = plan_url
        if plan_last_change is not None:
          self.plan_last_change = plan_last_change
        if status is not None:
          self.status = status
        if sales_start is not None:
          self.sales_start = sales_start
        if sales_end is not None:
          self.sales_end = sales_end
        if is_exclu is not None:
          self.is_exclu = is_exclu

    @property
    def id(self):
        """
        Gets the id of this ShowsResponseInner.

        :return: The id of this ShowsResponseInner.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ShowsResponseInner.

        :param id: The id of this ShowsResponseInner.
        :type: int
        """

        self._id = id

    @property
    def start(self):
        """
        Gets the start of this ShowsResponseInner.

        :return: The start of this ShowsResponseInner.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this ShowsResponseInner.

        :param start: The start of this ShowsResponseInner.
        :type: str
        """

        self._start = start

    @property
    def end(self):
        """
        Gets the end of this ShowsResponseInner.

        :return: The end of this ShowsResponseInner.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this ShowsResponseInner.

        :param end: The end of this ShowsResponseInner.
        :type: str
        """

        self._end = end

    @property
    def venue(self):
        """
        Gets the venue of this ShowsResponseInner.

        :return: The venue of this ShowsResponseInner.
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """
        Sets the venue of this ShowsResponseInner.

        :param venue: The venue of this ShowsResponseInner.
        :type: str
        """

        self._venue = venue

    @property
    def address(self):
        """
        Gets the address of this ShowsResponseInner.

        :return: The address of this ShowsResponseInner.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this ShowsResponseInner.

        :param address: The address of this ShowsResponseInner.
        :type: str
        """

        self._address = address

    @property
    def zip_code(self):
        """
        Gets the zip_code of this ShowsResponseInner.

        :return: The zip_code of this ShowsResponseInner.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this ShowsResponseInner.

        :param zip_code: The zip_code of this ShowsResponseInner.
        :type: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """
        Gets the city of this ShowsResponseInner.

        :return: The city of this ShowsResponseInner.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this ShowsResponseInner.

        :param city: The city of this ShowsResponseInner.
        :type: str
        """

        self._city = city

    @property
    def country_id(self):
        """
        Gets the country_id of this ShowsResponseInner.

        :return: The country_id of this ShowsResponseInner.
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """
        Sets the country_id of this ShowsResponseInner.

        :param country_id: The country_id of this ShowsResponseInner.
        :type: int
        """

        self._country_id = country_id

    @property
    def number_of_prices(self):
        """
        Gets the number_of_prices of this ShowsResponseInner.

        :return: The number_of_prices of this ShowsResponseInner.
        :rtype: int
        """
        return self._number_of_prices

    @number_of_prices.setter
    def number_of_prices(self, number_of_prices):
        """
        Sets the number_of_prices of this ShowsResponseInner.

        :param number_of_prices: The number_of_prices of this ShowsResponseInner.
        :type: int
        """

        self._number_of_prices = number_of_prices

    @property
    def min_price_cents(self):
        """
        Gets the min_price_cents of this ShowsResponseInner.

        :return: The min_price_cents of this ShowsResponseInner.
        :rtype: int
        """
        return self._min_price_cents

    @min_price_cents.setter
    def min_price_cents(self, min_price_cents):
        """
        Sets the min_price_cents of this ShowsResponseInner.

        :param min_price_cents: The min_price_cents of this ShowsResponseInner.
        :type: int
        """

        self._min_price_cents = min_price_cents

    @property
    def max_price_cents(self):
        """
        Gets the max_price_cents of this ShowsResponseInner.

        :return: The max_price_cents of this ShowsResponseInner.
        :rtype: int
        """
        return self._max_price_cents

    @max_price_cents.setter
    def max_price_cents(self, max_price_cents):
        """
        Sets the max_price_cents of this ShowsResponseInner.

        :param max_price_cents: The max_price_cents of this ShowsResponseInner.
        :type: int
        """

        self._max_price_cents = max_price_cents

    @property
    def reserved_seats(self):
        """
        Gets the reserved_seats of this ShowsResponseInner.

        :return: The reserved_seats of this ShowsResponseInner.
        :rtype: bool
        """
        return self._reserved_seats

    @reserved_seats.setter
    def reserved_seats(self, reserved_seats):
        """
        Sets the reserved_seats of this ShowsResponseInner.

        :param reserved_seats: The reserved_seats of this ShowsResponseInner.
        :type: bool
        """

        self._reserved_seats = reserved_seats

    @property
    def plan_url(self):
        """
        Gets the plan_url of this ShowsResponseInner.

        :return: The plan_url of this ShowsResponseInner.
        :rtype: str
        """
        return self._plan_url

    @plan_url.setter
    def plan_url(self, plan_url):
        """
        Sets the plan_url of this ShowsResponseInner.

        :param plan_url: The plan_url of this ShowsResponseInner.
        :type: str
        """

        self._plan_url = plan_url

    @property
    def plan_last_change(self):
        """
        Gets the plan_last_change of this ShowsResponseInner.

        :return: The plan_last_change of this ShowsResponseInner.
        :rtype: str
        """
        return self._plan_last_change

    @plan_last_change.setter
    def plan_last_change(self, plan_last_change):
        """
        Sets the plan_last_change of this ShowsResponseInner.

        :param plan_last_change: The plan_last_change of this ShowsResponseInner.
        :type: str
        """

        self._plan_last_change = plan_last_change

    @property
    def status(self):
        """
        Gets the status of this ShowsResponseInner.

        :return: The status of this ShowsResponseInner.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ShowsResponseInner.

        :param status: The status of this ShowsResponseInner.
        :type: int
        """

        self._status = status

    @property
    def sales_start(self):
        """
        Gets the sales_start of this ShowsResponseInner.

        :return: The sales_start of this ShowsResponseInner.
        :rtype: str
        """
        return self._sales_start

    @sales_start.setter
    def sales_start(self, sales_start):
        """
        Sets the sales_start of this ShowsResponseInner.

        :param sales_start: The sales_start of this ShowsResponseInner.
        :type: str
        """

        self._sales_start = sales_start

    @property
    def sales_end(self):
        """
        Gets the sales_end of this ShowsResponseInner.

        :return: The sales_end of this ShowsResponseInner.
        :rtype: str
        """
        return self._sales_end

    @sales_end.setter
    def sales_end(self, sales_end):
        """
        Sets the sales_end of this ShowsResponseInner.

        :param sales_end: The sales_end of this ShowsResponseInner.
        :type: str
        """

        self._sales_end = sales_end

    @property
    def is_exclu(self):
        """
        Gets the is_exclu of this ShowsResponseInner.

        :return: The is_exclu of this ShowsResponseInner.
        :rtype: bool
        """
        return self._is_exclu

    @is_exclu.setter
    def is_exclu(self, is_exclu):
        """
        Sets the is_exclu of this ShowsResponseInner.

        :param is_exclu: The is_exclu of this ShowsResponseInner.
        :type: bool
        """

        self._is_exclu = is_exclu

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ShowsResponseInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
