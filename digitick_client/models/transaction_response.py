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


class TransactionResponse(object):
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
        'transaction_id': 'int',
        'event_name': 'str',
        'event_picture_url110_png': 'str',
        'event_picture_url80_gif': 'str',
        'event_picture_url45_gif': 'str',
        'venue': 'str',
        'address': 'str',
        'zip_code': 'str',
        'city': 'str',
        'country_id': 'int',
        'date_of_purchase': 'str',
        'start_date': 'str',
        'end_date': 'str',
        'price_value_cents': 'int',
        'buyer_first_name': 'str',
        'buyer_last_name': 'str',
        'end_user_first_name': 'str',
        'end_user_last_name': 'str',
        'sponsor': 'str',
        'producer1': 'str',
        'producer2': 'str',
        'producer_licence': 'str',
        'message': 'str',
        'barcode': 'str',
        'barcode_type': 'str',
        'ticket_details_list': 'list[TicketDetails]'
    }

    attribute_map = {
        'id': 'id',
        'transaction_id': 'transactionId',
        'event_name': 'eventName',
        'event_picture_url110_png': 'eventPictureUrl110Png',
        'event_picture_url80_gif': 'eventPictureUrl80Gif',
        'event_picture_url45_gif': 'eventPictureUrl45Gif',
        'venue': 'venue',
        'address': 'address',
        'zip_code': 'zipCode',
        'city': 'city',
        'country_id': 'countryId',
        'date_of_purchase': 'dateOfPurchase',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'price_value_cents': 'priceValueCents',
        'buyer_first_name': 'buyerFirstName',
        'buyer_last_name': 'buyerLastName',
        'end_user_first_name': 'endUserFirstName',
        'end_user_last_name': 'endUserLastName',
        'sponsor': 'sponsor',
        'producer1': 'producer1',
        'producer2': 'producer2',
        'producer_licence': 'producerLicence',
        'message': 'message',
        'barcode': 'barcode',
        'barcode_type': 'barcodeType',
        'ticket_details_list': 'ticketDetailsList'
    }

    def __init__(self, id=None, transaction_id=None, event_name=None, event_picture_url110_png=None, event_picture_url80_gif=None, event_picture_url45_gif=None, venue=None, address=None, zip_code=None, city=None, country_id=None, date_of_purchase=None, start_date=None, end_date=None, price_value_cents=None, buyer_first_name=None, buyer_last_name=None, end_user_first_name=None, end_user_last_name=None, sponsor=None, producer1=None, producer2=None, producer_licence=None, message=None, barcode=None, barcode_type=None, ticket_details_list=None):
        """
        TransactionResponse - a model defined in Swagger
        """

        self._id = None
        self._transaction_id = None
        self._event_name = None
        self._event_picture_url110_png = None
        self._event_picture_url80_gif = None
        self._event_picture_url45_gif = None
        self._venue = None
        self._address = None
        self._zip_code = None
        self._city = None
        self._country_id = None
        self._date_of_purchase = None
        self._start_date = None
        self._end_date = None
        self._price_value_cents = None
        self._buyer_first_name = None
        self._buyer_last_name = None
        self._end_user_first_name = None
        self._end_user_last_name = None
        self._sponsor = None
        self._producer1 = None
        self._producer2 = None
        self._producer_licence = None
        self._message = None
        self._barcode = None
        self._barcode_type = None
        self._ticket_details_list = None

        if id is not None:
          self.id = id
        if transaction_id is not None:
          self.transaction_id = transaction_id
        if event_name is not None:
          self.event_name = event_name
        if event_picture_url110_png is not None:
          self.event_picture_url110_png = event_picture_url110_png
        if event_picture_url80_gif is not None:
          self.event_picture_url80_gif = event_picture_url80_gif
        if event_picture_url45_gif is not None:
          self.event_picture_url45_gif = event_picture_url45_gif
        if venue is not None:
          self.venue = venue
        if address is not None:
          self.address = address
        if zip_code is not None:
          self.zip_code = zip_code
        if city is not None:
          self.city = city
        if country_id is not None:
          self.country_id = country_id
        if date_of_purchase is not None:
          self.date_of_purchase = date_of_purchase
        if start_date is not None:
          self.start_date = start_date
        if end_date is not None:
          self.end_date = end_date
        if price_value_cents is not None:
          self.price_value_cents = price_value_cents
        if buyer_first_name is not None:
          self.buyer_first_name = buyer_first_name
        if buyer_last_name is not None:
          self.buyer_last_name = buyer_last_name
        if end_user_first_name is not None:
          self.end_user_first_name = end_user_first_name
        if end_user_last_name is not None:
          self.end_user_last_name = end_user_last_name
        if sponsor is not None:
          self.sponsor = sponsor
        if producer1 is not None:
          self.producer1 = producer1
        if producer2 is not None:
          self.producer2 = producer2
        if producer_licence is not None:
          self.producer_licence = producer_licence
        if message is not None:
          self.message = message
        if barcode is not None:
          self.barcode = barcode
        if barcode_type is not None:
          self.barcode_type = barcode_type
        if ticket_details_list is not None:
          self.ticket_details_list = ticket_details_list

    @property
    def id(self):
        """
        Gets the id of this TransactionResponse.

        :return: The id of this TransactionResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TransactionResponse.

        :param id: The id of this TransactionResponse.
        :type: int
        """

        self._id = id

    @property
    def transaction_id(self):
        """
        Gets the transaction_id of this TransactionResponse.

        :return: The transaction_id of this TransactionResponse.
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """
        Sets the transaction_id of this TransactionResponse.

        :param transaction_id: The transaction_id of this TransactionResponse.
        :type: int
        """

        self._transaction_id = transaction_id

    @property
    def event_name(self):
        """
        Gets the event_name of this TransactionResponse.

        :return: The event_name of this TransactionResponse.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """
        Sets the event_name of this TransactionResponse.

        :param event_name: The event_name of this TransactionResponse.
        :type: str
        """

        self._event_name = event_name

    @property
    def event_picture_url110_png(self):
        """
        Gets the event_picture_url110_png of this TransactionResponse.

        :return: The event_picture_url110_png of this TransactionResponse.
        :rtype: str
        """
        return self._event_picture_url110_png

    @event_picture_url110_png.setter
    def event_picture_url110_png(self, event_picture_url110_png):
        """
        Sets the event_picture_url110_png of this TransactionResponse.

        :param event_picture_url110_png: The event_picture_url110_png of this TransactionResponse.
        :type: str
        """

        self._event_picture_url110_png = event_picture_url110_png

    @property
    def event_picture_url80_gif(self):
        """
        Gets the event_picture_url80_gif of this TransactionResponse.

        :return: The event_picture_url80_gif of this TransactionResponse.
        :rtype: str
        """
        return self._event_picture_url80_gif

    @event_picture_url80_gif.setter
    def event_picture_url80_gif(self, event_picture_url80_gif):
        """
        Sets the event_picture_url80_gif of this TransactionResponse.

        :param event_picture_url80_gif: The event_picture_url80_gif of this TransactionResponse.
        :type: str
        """

        self._event_picture_url80_gif = event_picture_url80_gif

    @property
    def event_picture_url45_gif(self):
        """
        Gets the event_picture_url45_gif of this TransactionResponse.

        :return: The event_picture_url45_gif of this TransactionResponse.
        :rtype: str
        """
        return self._event_picture_url45_gif

    @event_picture_url45_gif.setter
    def event_picture_url45_gif(self, event_picture_url45_gif):
        """
        Sets the event_picture_url45_gif of this TransactionResponse.

        :param event_picture_url45_gif: The event_picture_url45_gif of this TransactionResponse.
        :type: str
        """

        self._event_picture_url45_gif = event_picture_url45_gif

    @property
    def venue(self):
        """
        Gets the venue of this TransactionResponse.

        :return: The venue of this TransactionResponse.
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """
        Sets the venue of this TransactionResponse.

        :param venue: The venue of this TransactionResponse.
        :type: str
        """

        self._venue = venue

    @property
    def address(self):
        """
        Gets the address of this TransactionResponse.

        :return: The address of this TransactionResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this TransactionResponse.

        :param address: The address of this TransactionResponse.
        :type: str
        """

        self._address = address

    @property
    def zip_code(self):
        """
        Gets the zip_code of this TransactionResponse.

        :return: The zip_code of this TransactionResponse.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this TransactionResponse.

        :param zip_code: The zip_code of this TransactionResponse.
        :type: str
        """

        self._zip_code = zip_code

    @property
    def city(self):
        """
        Gets the city of this TransactionResponse.

        :return: The city of this TransactionResponse.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this TransactionResponse.

        :param city: The city of this TransactionResponse.
        :type: str
        """

        self._city = city

    @property
    def country_id(self):
        """
        Gets the country_id of this TransactionResponse.

        :return: The country_id of this TransactionResponse.
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """
        Sets the country_id of this TransactionResponse.

        :param country_id: The country_id of this TransactionResponse.
        :type: int
        """

        self._country_id = country_id

    @property
    def date_of_purchase(self):
        """
        Gets the date_of_purchase of this TransactionResponse.

        :return: The date_of_purchase of this TransactionResponse.
        :rtype: str
        """
        return self._date_of_purchase

    @date_of_purchase.setter
    def date_of_purchase(self, date_of_purchase):
        """
        Sets the date_of_purchase of this TransactionResponse.

        :param date_of_purchase: The date_of_purchase of this TransactionResponse.
        :type: str
        """

        self._date_of_purchase = date_of_purchase

    @property
    def start_date(self):
        """
        Gets the start_date of this TransactionResponse.

        :return: The start_date of this TransactionResponse.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """
        Sets the start_date of this TransactionResponse.

        :param start_date: The start_date of this TransactionResponse.
        :type: str
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """
        Gets the end_date of this TransactionResponse.

        :return: The end_date of this TransactionResponse.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """
        Sets the end_date of this TransactionResponse.

        :param end_date: The end_date of this TransactionResponse.
        :type: str
        """

        self._end_date = end_date

    @property
    def price_value_cents(self):
        """
        Gets the price_value_cents of this TransactionResponse.

        :return: The price_value_cents of this TransactionResponse.
        :rtype: int
        """
        return self._price_value_cents

    @price_value_cents.setter
    def price_value_cents(self, price_value_cents):
        """
        Sets the price_value_cents of this TransactionResponse.

        :param price_value_cents: The price_value_cents of this TransactionResponse.
        :type: int
        """

        self._price_value_cents = price_value_cents

    @property
    def buyer_first_name(self):
        """
        Gets the buyer_first_name of this TransactionResponse.

        :return: The buyer_first_name of this TransactionResponse.
        :rtype: str
        """
        return self._buyer_first_name

    @buyer_first_name.setter
    def buyer_first_name(self, buyer_first_name):
        """
        Sets the buyer_first_name of this TransactionResponse.

        :param buyer_first_name: The buyer_first_name of this TransactionResponse.
        :type: str
        """

        self._buyer_first_name = buyer_first_name

    @property
    def buyer_last_name(self):
        """
        Gets the buyer_last_name of this TransactionResponse.

        :return: The buyer_last_name of this TransactionResponse.
        :rtype: str
        """
        return self._buyer_last_name

    @buyer_last_name.setter
    def buyer_last_name(self, buyer_last_name):
        """
        Sets the buyer_last_name of this TransactionResponse.

        :param buyer_last_name: The buyer_last_name of this TransactionResponse.
        :type: str
        """

        self._buyer_last_name = buyer_last_name

    @property
    def end_user_first_name(self):
        """
        Gets the end_user_first_name of this TransactionResponse.

        :return: The end_user_first_name of this TransactionResponse.
        :rtype: str
        """
        return self._end_user_first_name

    @end_user_first_name.setter
    def end_user_first_name(self, end_user_first_name):
        """
        Sets the end_user_first_name of this TransactionResponse.

        :param end_user_first_name: The end_user_first_name of this TransactionResponse.
        :type: str
        """

        self._end_user_first_name = end_user_first_name

    @property
    def end_user_last_name(self):
        """
        Gets the end_user_last_name of this TransactionResponse.

        :return: The end_user_last_name of this TransactionResponse.
        :rtype: str
        """
        return self._end_user_last_name

    @end_user_last_name.setter
    def end_user_last_name(self, end_user_last_name):
        """
        Sets the end_user_last_name of this TransactionResponse.

        :param end_user_last_name: The end_user_last_name of this TransactionResponse.
        :type: str
        """

        self._end_user_last_name = end_user_last_name

    @property
    def sponsor(self):
        """
        Gets the sponsor of this TransactionResponse.

        :return: The sponsor of this TransactionResponse.
        :rtype: str
        """
        return self._sponsor

    @sponsor.setter
    def sponsor(self, sponsor):
        """
        Sets the sponsor of this TransactionResponse.

        :param sponsor: The sponsor of this TransactionResponse.
        :type: str
        """

        self._sponsor = sponsor

    @property
    def producer1(self):
        """
        Gets the producer1 of this TransactionResponse.

        :return: The producer1 of this TransactionResponse.
        :rtype: str
        """
        return self._producer1

    @producer1.setter
    def producer1(self, producer1):
        """
        Sets the producer1 of this TransactionResponse.

        :param producer1: The producer1 of this TransactionResponse.
        :type: str
        """

        self._producer1 = producer1

    @property
    def producer2(self):
        """
        Gets the producer2 of this TransactionResponse.

        :return: The producer2 of this TransactionResponse.
        :rtype: str
        """
        return self._producer2

    @producer2.setter
    def producer2(self, producer2):
        """
        Sets the producer2 of this TransactionResponse.

        :param producer2: The producer2 of this TransactionResponse.
        :type: str
        """

        self._producer2 = producer2

    @property
    def producer_licence(self):
        """
        Gets the producer_licence of this TransactionResponse.

        :return: The producer_licence of this TransactionResponse.
        :rtype: str
        """
        return self._producer_licence

    @producer_licence.setter
    def producer_licence(self, producer_licence):
        """
        Sets the producer_licence of this TransactionResponse.

        :param producer_licence: The producer_licence of this TransactionResponse.
        :type: str
        """

        self._producer_licence = producer_licence

    @property
    def message(self):
        """
        Gets the message of this TransactionResponse.

        :return: The message of this TransactionResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this TransactionResponse.

        :param message: The message of this TransactionResponse.
        :type: str
        """

        self._message = message

    @property
    def barcode(self):
        """
        Gets the barcode of this TransactionResponse.

        :return: The barcode of this TransactionResponse.
        :rtype: str
        """
        return self._barcode

    @barcode.setter
    def barcode(self, barcode):
        """
        Sets the barcode of this TransactionResponse.

        :param barcode: The barcode of this TransactionResponse.
        :type: str
        """

        self._barcode = barcode

    @property
    def barcode_type(self):
        """
        Gets the barcode_type of this TransactionResponse.

        :return: The barcode_type of this TransactionResponse.
        :rtype: str
        """
        return self._barcode_type

    @barcode_type.setter
    def barcode_type(self, barcode_type):
        """
        Sets the barcode_type of this TransactionResponse.

        :param barcode_type: The barcode_type of this TransactionResponse.
        :type: str
        """

        self._barcode_type = barcode_type

    @property
    def ticket_details_list(self):
        """
        Gets the ticket_details_list of this TransactionResponse.

        :return: The ticket_details_list of this TransactionResponse.
        :rtype: list[TicketDetails]
        """
        return self._ticket_details_list

    @ticket_details_list.setter
    def ticket_details_list(self, ticket_details_list):
        """
        Sets the ticket_details_list of this TransactionResponse.

        :param ticket_details_list: The ticket_details_list of this TransactionResponse.
        :type: list[TicketDetails]
        """

        self._ticket_details_list = ticket_details_list

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
        if not isinstance(other, TransactionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
