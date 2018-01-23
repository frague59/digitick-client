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


class PlaceNoBlock(object):
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
        'price_id': 'int'
    }

    attribute_map = {
        'nb_seats': 'nbSeats',
        'promotionnal_code': 'promotionnalCode',
        'price_id': 'priceId'
    }

    def __init__(self, nb_seats=None, promotionnal_code=None, price_id=None):
        """
        PlaceNoBlock - a model defined in Swagger
        """

        self._nb_seats = None
        self._promotionnal_code = None
        self._price_id = None

        if nb_seats is not None:
          self.nb_seats = nb_seats
        if promotionnal_code is not None:
          self.promotionnal_code = promotionnal_code
        if price_id is not None:
          self.price_id = price_id

    @property
    def nb_seats(self):
        """
        Gets the nb_seats of this PlaceNoBlock.

        :return: The nb_seats of this PlaceNoBlock.
        :rtype: int
        """
        return self._nb_seats

    @nb_seats.setter
    def nb_seats(self, nb_seats):
        """
        Sets the nb_seats of this PlaceNoBlock.

        :param nb_seats: The nb_seats of this PlaceNoBlock.
        :type: int
        """

        self._nb_seats = nb_seats

    @property
    def promotionnal_code(self):
        """
        Gets the promotionnal_code of this PlaceNoBlock.

        :return: The promotionnal_code of this PlaceNoBlock.
        :rtype: str
        """
        return self._promotionnal_code

    @promotionnal_code.setter
    def promotionnal_code(self, promotionnal_code):
        """
        Sets the promotionnal_code of this PlaceNoBlock.

        :param promotionnal_code: The promotionnal_code of this PlaceNoBlock.
        :type: str
        """

        self._promotionnal_code = promotionnal_code

    @property
    def price_id(self):
        """
        Gets the price_id of this PlaceNoBlock.

        :return: The price_id of this PlaceNoBlock.
        :rtype: int
        """
        return self._price_id

    @price_id.setter
    def price_id(self, price_id):
        """
        Sets the price_id of this PlaceNoBlock.

        :param price_id: The price_id of this PlaceNoBlock.
        :type: int
        """

        self._price_id = price_id

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
        if not isinstance(other, PlaceNoBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
