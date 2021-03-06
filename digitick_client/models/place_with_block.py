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


class PlaceWithBlock(object):
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
        'nb_seats': 'int',
        'promotionnal_code': 'str',
        'price_ids': 'list[ERRORUNKNOWN]',
        'block_ids': 'list[ERRORUNKNOWN]'
    }

    attribute_map = {
        'nb_seats': 'nbSeats',
        'promotionnal_code': 'promotionnalCode',
        'price_ids': 'priceIds',
        'block_ids': 'blockIds'
    }

    def __init__(self, nb_seats=None, promotionnal_code=None, price_ids=None, block_ids=None):
        """
        PlaceWithBlock - a model defined in Swagger
        """

        self._nb_seats = None
        self._promotionnal_code = None
        self._price_ids = None
        self._block_ids = None

        if nb_seats is not None:
          self.nb_seats = nb_seats
        if promotionnal_code is not None:
          self.promotionnal_code = promotionnal_code
        if price_ids is not None:
          self.price_ids = price_ids
        if block_ids is not None:
          self.block_ids = block_ids

    @property
    def nb_seats(self):
        """
        Gets the nb_seats of this PlaceWithBlock.

        :return: The nb_seats of this PlaceWithBlock.
        :rtype: int
        """
        return self._nb_seats

    @nb_seats.setter
    def nb_seats(self, nb_seats):
        """
        Sets the nb_seats of this PlaceWithBlock.

        :param nb_seats: The nb_seats of this PlaceWithBlock.
        :type: int
        """

        self._nb_seats = nb_seats

    @property
    def promotionnal_code(self):
        """
        Gets the promotionnal_code of this PlaceWithBlock.

        :return: The promotionnal_code of this PlaceWithBlock.
        :rtype: str
        """
        return self._promotionnal_code

    @promotionnal_code.setter
    def promotionnal_code(self, promotionnal_code):
        """
        Sets the promotionnal_code of this PlaceWithBlock.

        :param promotionnal_code: The promotionnal_code of this PlaceWithBlock.
        :type: str
        """

        self._promotionnal_code = promotionnal_code

    @property
    def price_ids(self):
        """
        Gets the price_ids of this PlaceWithBlock.

        :return: The price_ids of this PlaceWithBlock.
        :rtype: list[ERRORUNKNOWN]
        """
        return self._price_ids

    @price_ids.setter
    def price_ids(self, price_ids):
        """
        Sets the price_ids of this PlaceWithBlock.

        :param price_ids: The price_ids of this PlaceWithBlock.
        :type: list[ERRORUNKNOWN]
        """

        self._price_ids = price_ids

    @property
    def block_ids(self):
        """
        Gets the block_ids of this PlaceWithBlock.

        :return: The block_ids of this PlaceWithBlock.
        :rtype: list[ERRORUNKNOWN]
        """
        return self._block_ids

    @block_ids.setter
    def block_ids(self, block_ids):
        """
        Sets the block_ids of this PlaceWithBlock.

        :param block_ids: The block_ids of this PlaceWithBlock.
        :type: list[ERRORUNKNOWN]
        """

        self._block_ids = block_ids

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
        if not isinstance(other, PlaceWithBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
