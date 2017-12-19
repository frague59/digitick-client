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


class Ticket(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, lastname=None, firstname=None, deleted=None, show_id=None, entries=None):
        """
        Ticket - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'lastname': 'str',
            'firstname': 'str',
            'deleted': 'bool',
            'show_id': 'int',
            'entries': 'list[int]'
        }

        self.attribute_map = {
            'id': 'id',
            'lastname': 'lastname',
            'firstname': 'firstname',
            'deleted': 'deleted',
            'show_id': 'showId',
            'entries': 'entries'
        }

        self._id = id
        self._lastname = lastname
        self._firstname = firstname
        self._deleted = deleted
        self._show_id = show_id
        self._entries = entries

    @property
    def id(self):
        """
        Gets the id of this Ticket.

        :return: The id of this Ticket.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Ticket.

        :param id: The id of this Ticket.
        :type: int
        """

        self._id = id

    @property
    def lastname(self):
        """
        Gets the lastname of this Ticket.

        :return: The lastname of this Ticket.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this Ticket.

        :param lastname: The lastname of this Ticket.
        :type: str
        """

        self._lastname = lastname

    @property
    def firstname(self):
        """
        Gets the firstname of this Ticket.

        :return: The firstname of this Ticket.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this Ticket.

        :param firstname: The firstname of this Ticket.
        :type: str
        """

        self._firstname = firstname

    @property
    def deleted(self):
        """
        Gets the deleted of this Ticket.

        :return: The deleted of this Ticket.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this Ticket.

        :param deleted: The deleted of this Ticket.
        :type: bool
        """

        self._deleted = deleted

    @property
    def show_id(self):
        """
        Gets the show_id of this Ticket.

        :return: The show_id of this Ticket.
        :rtype: int
        """
        return self._show_id

    @show_id.setter
    def show_id(self, show_id):
        """
        Sets the show_id of this Ticket.

        :param show_id: The show_id of this Ticket.
        :type: int
        """

        self._show_id = show_id

    @property
    def entries(self):
        """
        Gets the entries of this Ticket.

        :return: The entries of this Ticket.
        :rtype: list[int]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this Ticket.

        :param entries: The entries of this Ticket.
        :type: list[int]
        """

        self._entries = entries

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
        if not isinstance(other, Ticket):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
