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


class VatInfos(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, percentage=None, amount_cents=None):
        """
        VatInfos - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'percentage': 'float',
            'amount_cents': 'int'
        }

        self.attribute_map = {
            'percentage': 'percentage',
            'amount_cents': 'amountCents'
        }

        self._percentage = percentage
        self._amount_cents = amount_cents

    @property
    def percentage(self):
        """
        Gets the percentage of this VatInfos.

        :return: The percentage of this VatInfos.
        :rtype: float
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """
        Sets the percentage of this VatInfos.

        :param percentage: The percentage of this VatInfos.
        :type: float
        """

        self._percentage = percentage

    @property
    def amount_cents(self):
        """
        Gets the amount_cents of this VatInfos.

        :return: The amount_cents of this VatInfos.
        :rtype: int
        """
        return self._amount_cents

    @amount_cents.setter
    def amount_cents(self, amount_cents):
        """
        Sets the amount_cents of this VatInfos.

        :param amount_cents: The amount_cents of this VatInfos.
        :type: int
        """

        self._amount_cents = amount_cents

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
        if not isinstance(other, VatInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
