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


class UserActionsInner(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, op=None, _property=None, value=None):
        """
        UserActionsInner - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'op': 'str',
            '_property': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'op': 'op',
            '_property': 'property',
            'value': 'value'
        }

        self._op = op
        self.__property = _property
        self._value = value

    @property
    def op(self):
        """
        Gets the op of this UserActionsInner.

        :return: The op of this UserActionsInner.
        :rtype: str
        """
        return self._op

    @op.setter
    def op(self, op):
        """
        Sets the op of this UserActionsInner.

        :param op: The op of this UserActionsInner.
        :type: str
        """

        self._op = op

    @property
    def _property(self):
        """
        Gets the _property of this UserActionsInner.

        :return: The _property of this UserActionsInner.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """
        Sets the _property of this UserActionsInner.

        :param _property: The _property of this UserActionsInner.
        :type: str
        """

        self.__property = _property

    @property
    def value(self):
        """
        Gets the value of this UserActionsInner.

        :return: The value of this UserActionsInner.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserActionsInner.

        :param value: The value of this UserActionsInner.
        :type: str
        """

        self._value = value

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
        if not isinstance(other, UserActionsInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
