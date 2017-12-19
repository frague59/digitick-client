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


class Room(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, address=None, zipcode=None, city_id=None):
        """
        Room - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'address': 'str',
            'zipcode': 'str',
            'city_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'address': 'address',
            'zipcode': 'zipcode',
            'city_id': 'cityId'
        }

        self._id = id
        self._name = name
        self._address = address
        self._zipcode = zipcode
        self._city_id = city_id

    @property
    def id(self):
        """
        Gets the id of this Room.

        :return: The id of this Room.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Room.

        :param id: The id of this Room.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Room.

        :return: The name of this Room.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Room.

        :param name: The name of this Room.
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """
        Gets the address of this Room.

        :return: The address of this Room.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Room.

        :param address: The address of this Room.
        :type: str
        """

        self._address = address

    @property
    def zipcode(self):
        """
        Gets the zipcode of this Room.

        :return: The zipcode of this Room.
        :rtype: str
        """
        return self._zipcode

    @zipcode.setter
    def zipcode(self, zipcode):
        """
        Sets the zipcode of this Room.

        :param zipcode: The zipcode of this Room.
        :type: str
        """

        self._zipcode = zipcode

    @property
    def city_id(self):
        """
        Gets the city_id of this Room.

        :return: The city_id of this Room.
        :rtype: int
        """
        return self._city_id

    @city_id.setter
    def city_id(self, city_id):
        """
        Sets the city_id of this Room.

        :param city_id: The city_id of this Room.
        :type: int
        """

        self._city_id = city_id

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
        if not isinstance(other, Room):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
