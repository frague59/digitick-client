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


class SalesChannelEvent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, short_name=None, presentation1=None, presentation2=None, producer1=None, producer2=None, sponsor=None, category_id=None, sub_category_id=None, thumbnail=None, cover=None, vat_percentage=None, keywords=None, facebook=None, prod_license=None, external_videos=None, minimum_age=None, product_type=None, formatted_date=None):
        """
        SalesChannelEvent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'short_name': 'str',
            'presentation1': 'str',
            'presentation2': 'str',
            'producer1': 'str',
            'producer2': 'str',
            'sponsor': 'str',
            'category_id': 'int',
            'sub_category_id': 'int',
            'thumbnail': 'str',
            'cover': 'str',
            'vat_percentage': 'str',
            'keywords': 'str',
            'facebook': 'str',
            'prod_license': 'str',
            'external_videos': 'str',
            'minimum_age': 'int',
            'product_type': 'str',
            'formatted_date': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'short_name': 'shortName',
            'presentation1': 'presentation1',
            'presentation2': 'presentation2',
            'producer1': 'producer1',
            'producer2': 'producer2',
            'sponsor': 'sponsor',
            'category_id': 'categoryId',
            'sub_category_id': 'subCategoryId',
            'thumbnail': 'thumbnail',
            'cover': 'cover',
            'vat_percentage': 'vatPercentage',
            'keywords': 'keywords',
            'facebook': 'facebook',
            'prod_license': 'prodLicense',
            'external_videos': 'externalVideos',
            'minimum_age': 'minimumAge',
            'product_type': 'productType',
            'formatted_date': 'formattedDate'
        }

        self._id = id
        self._name = name
        self._short_name = short_name
        self._presentation1 = presentation1
        self._presentation2 = presentation2
        self._producer1 = producer1
        self._producer2 = producer2
        self._sponsor = sponsor
        self._category_id = category_id
        self._sub_category_id = sub_category_id
        self._thumbnail = thumbnail
        self._cover = cover
        self._vat_percentage = vat_percentage
        self._keywords = keywords
        self._facebook = facebook
        self._prod_license = prod_license
        self._external_videos = external_videos
        self._minimum_age = minimum_age
        self._product_type = product_type
        self._formatted_date = formatted_date

    @property
    def id(self):
        """
        Gets the id of this SalesChannelEvent.

        :return: The id of this SalesChannelEvent.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SalesChannelEvent.

        :param id: The id of this SalesChannelEvent.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this SalesChannelEvent.

        :return: The name of this SalesChannelEvent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SalesChannelEvent.

        :param name: The name of this SalesChannelEvent.
        :type: str
        """

        self._name = name

    @property
    def short_name(self):
        """
        Gets the short_name of this SalesChannelEvent.

        :return: The short_name of this SalesChannelEvent.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this SalesChannelEvent.

        :param short_name: The short_name of this SalesChannelEvent.
        :type: str
        """

        self._short_name = short_name

    @property
    def presentation1(self):
        """
        Gets the presentation1 of this SalesChannelEvent.

        :return: The presentation1 of this SalesChannelEvent.
        :rtype: str
        """
        return self._presentation1

    @presentation1.setter
    def presentation1(self, presentation1):
        """
        Sets the presentation1 of this SalesChannelEvent.

        :param presentation1: The presentation1 of this SalesChannelEvent.
        :type: str
        """

        self._presentation1 = presentation1

    @property
    def presentation2(self):
        """
        Gets the presentation2 of this SalesChannelEvent.

        :return: The presentation2 of this SalesChannelEvent.
        :rtype: str
        """
        return self._presentation2

    @presentation2.setter
    def presentation2(self, presentation2):
        """
        Sets the presentation2 of this SalesChannelEvent.

        :param presentation2: The presentation2 of this SalesChannelEvent.
        :type: str
        """

        self._presentation2 = presentation2

    @property
    def producer1(self):
        """
        Gets the producer1 of this SalesChannelEvent.

        :return: The producer1 of this SalesChannelEvent.
        :rtype: str
        """
        return self._producer1

    @producer1.setter
    def producer1(self, producer1):
        """
        Sets the producer1 of this SalesChannelEvent.

        :param producer1: The producer1 of this SalesChannelEvent.
        :type: str
        """

        self._producer1 = producer1

    @property
    def producer2(self):
        """
        Gets the producer2 of this SalesChannelEvent.

        :return: The producer2 of this SalesChannelEvent.
        :rtype: str
        """
        return self._producer2

    @producer2.setter
    def producer2(self, producer2):
        """
        Sets the producer2 of this SalesChannelEvent.

        :param producer2: The producer2 of this SalesChannelEvent.
        :type: str
        """

        self._producer2 = producer2

    @property
    def sponsor(self):
        """
        Gets the sponsor of this SalesChannelEvent.

        :return: The sponsor of this SalesChannelEvent.
        :rtype: str
        """
        return self._sponsor

    @sponsor.setter
    def sponsor(self, sponsor):
        """
        Sets the sponsor of this SalesChannelEvent.

        :param sponsor: The sponsor of this SalesChannelEvent.
        :type: str
        """

        self._sponsor = sponsor

    @property
    def category_id(self):
        """
        Gets the category_id of this SalesChannelEvent.

        :return: The category_id of this SalesChannelEvent.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this SalesChannelEvent.

        :param category_id: The category_id of this SalesChannelEvent.
        :type: int
        """

        self._category_id = category_id

    @property
    def sub_category_id(self):
        """
        Gets the sub_category_id of this SalesChannelEvent.

        :return: The sub_category_id of this SalesChannelEvent.
        :rtype: int
        """
        return self._sub_category_id

    @sub_category_id.setter
    def sub_category_id(self, sub_category_id):
        """
        Sets the sub_category_id of this SalesChannelEvent.

        :param sub_category_id: The sub_category_id of this SalesChannelEvent.
        :type: int
        """

        self._sub_category_id = sub_category_id

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this SalesChannelEvent.

        :return: The thumbnail of this SalesChannelEvent.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this SalesChannelEvent.

        :param thumbnail: The thumbnail of this SalesChannelEvent.
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def cover(self):
        """
        Gets the cover of this SalesChannelEvent.

        :return: The cover of this SalesChannelEvent.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """
        Sets the cover of this SalesChannelEvent.

        :param cover: The cover of this SalesChannelEvent.
        :type: str
        """

        self._cover = cover

    @property
    def vat_percentage(self):
        """
        Gets the vat_percentage of this SalesChannelEvent.

        :return: The vat_percentage of this SalesChannelEvent.
        :rtype: str
        """
        return self._vat_percentage

    @vat_percentage.setter
    def vat_percentage(self, vat_percentage):
        """
        Sets the vat_percentage of this SalesChannelEvent.

        :param vat_percentage: The vat_percentage of this SalesChannelEvent.
        :type: str
        """

        self._vat_percentage = vat_percentage

    @property
    def keywords(self):
        """
        Gets the keywords of this SalesChannelEvent.

        :return: The keywords of this SalesChannelEvent.
        :rtype: str
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this SalesChannelEvent.

        :param keywords: The keywords of this SalesChannelEvent.
        :type: str
        """

        self._keywords = keywords

    @property
    def facebook(self):
        """
        Gets the facebook of this SalesChannelEvent.

        :return: The facebook of this SalesChannelEvent.
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """
        Sets the facebook of this SalesChannelEvent.

        :param facebook: The facebook of this SalesChannelEvent.
        :type: str
        """

        self._facebook = facebook

    @property
    def prod_license(self):
        """
        Gets the prod_license of this SalesChannelEvent.

        :return: The prod_license of this SalesChannelEvent.
        :rtype: str
        """
        return self._prod_license

    @prod_license.setter
    def prod_license(self, prod_license):
        """
        Sets the prod_license of this SalesChannelEvent.

        :param prod_license: The prod_license of this SalesChannelEvent.
        :type: str
        """

        self._prod_license = prod_license

    @property
    def external_videos(self):
        """
        Gets the external_videos of this SalesChannelEvent.

        :return: The external_videos of this SalesChannelEvent.
        :rtype: str
        """
        return self._external_videos

    @external_videos.setter
    def external_videos(self, external_videos):
        """
        Sets the external_videos of this SalesChannelEvent.

        :param external_videos: The external_videos of this SalesChannelEvent.
        :type: str
        """

        self._external_videos = external_videos

    @property
    def minimum_age(self):
        """
        Gets the minimum_age of this SalesChannelEvent.

        :return: The minimum_age of this SalesChannelEvent.
        :rtype: int
        """
        return self._minimum_age

    @minimum_age.setter
    def minimum_age(self, minimum_age):
        """
        Sets the minimum_age of this SalesChannelEvent.

        :param minimum_age: The minimum_age of this SalesChannelEvent.
        :type: int
        """

        self._minimum_age = minimum_age

    @property
    def product_type(self):
        """
        Gets the product_type of this SalesChannelEvent.

        :return: The product_type of this SalesChannelEvent.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """
        Sets the product_type of this SalesChannelEvent.

        :param product_type: The product_type of this SalesChannelEvent.
        :type: str
        """

        self._product_type = product_type

    @property
    def formatted_date(self):
        """
        Gets the formatted_date of this SalesChannelEvent.

        :return: The formatted_date of this SalesChannelEvent.
        :rtype: str
        """
        return self._formatted_date

    @formatted_date.setter
    def formatted_date(self, formatted_date):
        """
        Sets the formatted_date of this SalesChannelEvent.

        :param formatted_date: The formatted_date of this SalesChannelEvent.
        :type: str
        """

        self._formatted_date = formatted_date

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
        if not isinstance(other, SalesChannelEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
