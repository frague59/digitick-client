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


class Seat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, rank=None, number=None, map_room_id=None):
        """
        Seat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'rank': 'str',
            'number': 'str',
            'map_room_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'rank': 'rank',
            'number': 'number',
            'map_room_id': 'mapRoomId'
        }

        self._id = id
        self._rank = rank
        self._number = number
        self._map_room_id = map_room_id

    @property
    def id(self):
        """
        Gets the id of this Seat.

        :return: The id of this Seat.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Seat.

        :param id: The id of this Seat.
        :type: int
        """

        self._id = id

    @property
    def rank(self):
        """
        Gets the rank of this Seat.

        :return: The rank of this Seat.
        :rtype: str
        """
        return self._rank

    @rank.setter
    def rank(self, rank):
        """
        Sets the rank of this Seat.

        :param rank: The rank of this Seat.
        :type: str
        """

        self._rank = rank

    @property
    def number(self):
        """
        Gets the number of this Seat.

        :return: The number of this Seat.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this Seat.

        :param number: The number of this Seat.
        :type: str
        """

        self._number = number

    @property
    def map_room_id(self):
        """
        Gets the map_room_id of this Seat.

        :return: The map_room_id of this Seat.
        :rtype: int
        """
        return self._map_room_id

    @map_room_id.setter
    def map_room_id(self, map_room_id):
        """
        Sets the map_room_id of this Seat.

        :param map_room_id: The map_room_id of this Seat.
        :type: int
        """

        self._map_room_id = map_room_id

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
        if not isinstance(other, Seat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
