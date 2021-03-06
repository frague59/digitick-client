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


class EntriesCartDetailResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, event_name=None, event_picture_url110_png=None, event_picture_url80_gif=None, event_picture_url45_gif=None, start_date=None, venue=None, address=None, zip_code=None, city=None, country_id=None, end_user_first_name=None, end_user_last_name=None, price_name=None, price_value_cents=None, position=None, vat_list=None):
        """
        EntriesCartDetailResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'event_name': 'str',
            'event_picture_url110_png': 'str',
            'event_picture_url80_gif': 'str',
            'event_picture_url45_gif': 'str',
            'start_date': 'str',
            'venue': 'str',
            'address': 'str',
            'zip_code': 'str',
            'city': 'str',
            'country_id': 'int',
            'end_user_first_name': 'str',
            'end_user_last_name': 'str',
            'price_name': 'str',
            'price_value_cents': 'int',
            'position': 'str',
            'vat_list': 'list[VatInfos]'
        }

        self.attribute_map = {
            'id': 'id',
            'event_name': 'eventName',
            'event_picture_url110_png': 'eventPictureUrl110Png',
            'event_picture_url80_gif': 'eventPictureUrl80Gif',
            'event_picture_url45_gif': 'eventPictureUrl45Gif',
            'start_date': 'startDate',
            'venue': 'venue',
            'address': 'address',
            'zip_code': 'zipCode',
            'city': 'city',
            'country_id': 'countryId',
            'end_user_first_name': 'endUserFirstName',
            'end_user_last_name': 'endUserLastName',
            'price_name': 'priceName',
            'price_value_cents': 'priceValueCents',
            'position': 'position',
            'vat_list': 'vatList'
        }

        self._id = id
        self._event_name = event_name
        self._event_picture_url110_png = event_picture_url110_png
        self._event_picture_url80_gif = event_picture_url80_gif
        self._event_picture_url45_gif = event_picture_url45_gif
        self._start_date = start_date
        self._venue = venue
        self._address = address
        self._zip_code = zip_code
        self._city = city
        self._country_id = country_id
        self._end_user_first_name = end_user_first_name
        self._end_user_last_name = end_user_last_name
        self._price_name = price_name
        self._price_value_cents = price_value_cents
        self._position = position
        self._vat_list = vat_list

    @property
    def id(self):
        """
        Gets the id of this EntriesCartDetailResponse.

        :return: The id of this EntriesCartDetailResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EntriesCartDetailResponse.

        :param id: The id of this EntriesCartDetailResponse.
        :type: int
        """

        self._id = id

    @property
    def event_name(self):
        """
        Gets the event_name of this EntriesCartDetailResponse.

        :return: The event_name of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this EntriesCartDetailResponse.

        :param event_name: The event_name of this EntriesCartDetailResponse.
        :type: str
        """

        self._event_name = event_name

    @property
    def event_picture_url110_png(self):
        """
        Gets the event_picture_url110_png of this EntriesCartDetailResponse.

        :return: The event_picture_url110_png of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._event_picture_url110_png

    @event_picture_url110_png.setter
    def event_picture_url110_png(self, event_picture_url110_png):
        """
        Sets the event_picture_url110_png of this EntriesCartDetailResponse.

        :param event_picture_url110_png: The event_picture_url110_png of this EntriesCartDetailResponse.
        :type: str
        """

        self._event_picture_url110_png = event_picture_url110_png

    @property
    def event_picture_url80_gif(self):
        """
        Gets the event_picture_url80_gif of this EntriesCartDetailResponse.

        :return: The event_picture_url80_gif of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._event_picture_url80_gif

    @event_picture_url80_gif.setter
    def event_picture_url80_gif(self, event_picture_url80_gif):
        """
        Sets the event_picture_url80_gif of this EntriesCartDetailResponse.

        :param event_picture_url80_gif: The event_picture_url80_gif of this EntriesCartDetailResponse.
        :type: str
        """

        self._event_picture_url80_gif = event_picture_url80_gif

    @property
    def event_picture_url45_gif(self):
        """
        Gets the event_picture_url45_gif of this EntriesCartDetailResponse.

        :return: The event_picture_url45_gif of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._event_picture_url45_gif

    @event_picture_url45_gif.setter
    def event_picture_url45_gif(self, event_picture_url45_gif):
        """
        Sets the event_picture_url45_gif of this EntriesCartDetailResponse.

        :param event_picture_url45_gif: The event_picture_url45_gif of this EntriesCartDetailResponse.
        :type: str
        """

        self._event_picture_url45_gif = event_picture_url45_gif

    @property
    def start_date(self):
        """
        Gets the start_date of this EntriesCartDetailResponse.

        :return: The start_date of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this EntriesCartDetailResponse.

        :param start_date: The start_date of this EntriesCartDetailResponse.
        :type: str
        """

        self._start_date = start_date

    @property
    def venue(self):
        """
        Gets the venue of this EntriesCartDetailResponse.

        :return: The venue of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """
        Sets the venue of this EntriesCartDetailResponse.

        :param venue: The venue of this EntriesCartDetailResponse.
        :type: str
        """

        self._venue = venue

    @property
    def address(self):
        """
        Gets the address of this EntriesCartDetailResponse.

        :return: The address of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this EntriesCartDetailResponse.

        :param address: The address of this EntriesCartDetailResponse.
        :type: str
        """

        self._address = address

    @property
    def zip_code(self):
        """
        Gets the zip_code of this EntriesCartDetailResponse.

        :return: The zip_code of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this EntriesCartDetailResponse.

        :param zip_code: The zip_code of this EntriesCartDetailResponse.
        :type: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """
        Gets the city of this EntriesCartDetailResponse.

        :return: The city of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this EntriesCartDetailResponse.

        :param city: The city of this EntriesCartDetailResponse.
        :type: str
        """

        self._city = city

    @property
    def country_id(self):
        """
        Gets the country_id of this EntriesCartDetailResponse.

        :return: The country_id of this EntriesCartDetailResponse.
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """
        Sets the country_id of this EntriesCartDetailResponse.

        :param country_id: The country_id of this EntriesCartDetailResponse.
        :type: int
        """

        self._country_id = country_id

    @property
    def end_user_first_name(self):
        """
        Gets the end_user_first_name of this EntriesCartDetailResponse.

        :return: The end_user_first_name of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._end_user_first_name

    @end_user_first_name.setter
    def end_user_first_name(self, end_user_first_name):
        """
        Sets the end_user_first_name of this EntriesCartDetailResponse.

        :param end_user_first_name: The end_user_first_name of this EntriesCartDetailResponse.
        :type: str
        """

        self._end_user_first_name = end_user_first_name

    @property
    def end_user_last_name(self):
        """
        Gets the end_user_last_name of this EntriesCartDetailResponse.

        :return: The end_user_last_name of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._end_user_last_name

    @end_user_last_name.setter
    def end_user_last_name(self, end_user_last_name):
        """
        Sets the end_user_last_name of this EntriesCartDetailResponse.

        :param end_user_last_name: The end_user_last_name of this EntriesCartDetailResponse.
        :type: str
        """

        self._end_user_last_name = end_user_last_name

    @property
    def price_name(self):
        """
        Gets the price_name of this EntriesCartDetailResponse.

        :return: The price_name of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._price_name

    @price_name.setter
    def price_name(self, price_name):
        """
        Sets the price_name of this EntriesCartDetailResponse.

        :param price_name: The price_name of this EntriesCartDetailResponse.
        :type: str
        """

        self._price_name = price_name

    @property
    def price_value_cents(self):
        """
        Gets the price_value_cents of this EntriesCartDetailResponse.

        :return: The price_value_cents of this EntriesCartDetailResponse.
        :rtype: int
        """
        return self._price_value_cents

    @price_value_cents.setter
    def price_value_cents(self, price_value_cents):
        """
        Sets the price_value_cents of this EntriesCartDetailResponse.

        :param price_value_cents: The price_value_cents of this EntriesCartDetailResponse.
        :type: int
        """

        self._price_value_cents = price_value_cents

    @property
    def position(self):
        """
        Gets the position of this EntriesCartDetailResponse.

        :return: The position of this EntriesCartDetailResponse.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this EntriesCartDetailResponse.

        :param position: The position of this EntriesCartDetailResponse.
        :type: str
        """

        self._position = position

    @property
    def vat_list(self):
        """
        Gets the vat_list of this EntriesCartDetailResponse.

        :return: The vat_list of this EntriesCartDetailResponse.
        :rtype: list[VatInfos]
        """
        return self._vat_list

    @vat_list.setter
    def vat_list(self, vat_list):
        """
        Sets the vat_list of this EntriesCartDetailResponse.

        :param vat_list: The vat_list of this EntriesCartDetailResponse.
        :type: list[VatInfos]
        """

        self._vat_list = vat_list

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
        if not isinstance(other, EntriesCartDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
