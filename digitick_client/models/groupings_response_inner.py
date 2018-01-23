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


class GroupingsResponseInner(object):
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
        'name': 'str',
        'category_id': 'int',
        'infos': 'str',
        'sub_category_id': 'int',
        'date_start': 'str',
        'date_end': 'str',
        'image_url': 'str',
        'number_of_events': 'int',
        'number_of_group_list': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'category_id': 'categoryId',
        'infos': 'infos',
        'sub_category_id': 'subCategoryId',
        'date_start': 'dateStart',
        'date_end': 'dateEnd',
        'image_url': 'imageUrl',
        'number_of_events': 'numberOfEvents',
        'number_of_group_list': 'numberOfGroupList'
    }

    def __init__(self, id=None, name=None, category_id=None, infos=None, sub_category_id=None, date_start=None, date_end=None, image_url=None, number_of_events=None, number_of_group_list=None):
        """
        GroupingsResponseInner - a model defined in Swagger
        """

        self._id = None
        self._name = None
        self._category_id = None
        self._infos = None
        self._sub_category_id = None
        self._date_start = None
        self._date_end = None
        self._image_url = None
        self._number_of_events = None
        self._number_of_group_list = None

        if id is not None:
          self.id = id
        if name is not None:
          self.name = name
        if category_id is not None:
          self.category_id = category_id
        if infos is not None:
          self.infos = infos
        if sub_category_id is not None:
          self.sub_category_id = sub_category_id
        if date_start is not None:
          self.date_start = date_start
        if date_end is not None:
          self.date_end = date_end
        if image_url is not None:
          self.image_url = image_url
        if number_of_events is not None:
          self.number_of_events = number_of_events
        if number_of_group_list is not None:
          self.number_of_group_list = number_of_group_list

    @property
    def id(self):
        """
        Gets the id of this GroupingsResponseInner.

        :return: The id of this GroupingsResponseInner.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GroupingsResponseInner.

        :param id: The id of this GroupingsResponseInner.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this GroupingsResponseInner.

        :return: The name of this GroupingsResponseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GroupingsResponseInner.

        :param name: The name of this GroupingsResponseInner.
        :type: str
        """

        self._name = name

    @property
    def category_id(self):
        """
        Gets the category_id of this GroupingsResponseInner.

        :return: The category_id of this GroupingsResponseInner.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this GroupingsResponseInner.

        :param category_id: The category_id of this GroupingsResponseInner.
        :type: int
        """

        self._category_id = category_id

    @property
    def infos(self):
        """
        Gets the infos of this GroupingsResponseInner.

        :return: The infos of this GroupingsResponseInner.
        :rtype: str
        """
        return self._infos

    @infos.setter
    def infos(self, infos):
        """
        Sets the infos of this GroupingsResponseInner.

        :param infos: The infos of this GroupingsResponseInner.
        :type: str
        """

        self._infos = infos

    @property
    def sub_category_id(self):
        """
        Gets the sub_category_id of this GroupingsResponseInner.

        :return: The sub_category_id of this GroupingsResponseInner.
        :rtype: int
        """
        return self._sub_category_id

    @sub_category_id.setter
    def sub_category_id(self, sub_category_id):
        """
        Sets the sub_category_id of this GroupingsResponseInner.

        :param sub_category_id: The sub_category_id of this GroupingsResponseInner.
        :type: int
        """

        self._sub_category_id = sub_category_id

    @property
    def date_start(self):
        """
        Gets the date_start of this GroupingsResponseInner.

        :return: The date_start of this GroupingsResponseInner.
        :rtype: str
        """
        return self._date_start

    @date_start.setter
    def date_start(self, date_start):
        """
        Sets the date_start of this GroupingsResponseInner.

        :param date_start: The date_start of this GroupingsResponseInner.
        :type: str
        """

        self._date_start = date_start

    @property
    def date_end(self):
        """
        Gets the date_end of this GroupingsResponseInner.

        :return: The date_end of this GroupingsResponseInner.
        :rtype: str
        """
        return self._date_end

    @date_end.setter
    def date_end(self, date_end):
        """
        Sets the date_end of this GroupingsResponseInner.

        :param date_end: The date_end of this GroupingsResponseInner.
        :type: str
        """

        self._date_end = date_end

    @property
    def image_url(self):
        """
        Gets the image_url of this GroupingsResponseInner.

        :return: The image_url of this GroupingsResponseInner.
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """
        Sets the image_url of this GroupingsResponseInner.

        :param image_url: The image_url of this GroupingsResponseInner.
        :type: str
        """

        self._image_url = image_url

    @property
    def number_of_events(self):
        """
        Gets the number_of_events of this GroupingsResponseInner.

        :return: The number_of_events of this GroupingsResponseInner.
        :rtype: int
        """
        return self._number_of_events

    @number_of_events.setter
    def number_of_events(self, number_of_events):
        """
        Sets the number_of_events of this GroupingsResponseInner.

        :param number_of_events: The number_of_events of this GroupingsResponseInner.
        :type: int
        """

        self._number_of_events = number_of_events

    @property
    def number_of_group_list(self):
        """
        Gets the number_of_group_list of this GroupingsResponseInner.

        :return: The number_of_group_list of this GroupingsResponseInner.
        :rtype: int
        """
        return self._number_of_group_list

    @number_of_group_list.setter
    def number_of_group_list(self, number_of_group_list):
        """
        Sets the number_of_group_list of this GroupingsResponseInner.

        :param number_of_group_list: The number_of_group_list of this GroupingsResponseInner.
        :type: int
        """

        self._number_of_group_list = number_of_group_list

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
        if not isinstance(other, GroupingsResponseInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other