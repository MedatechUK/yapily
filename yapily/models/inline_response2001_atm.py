# coding: utf-8

"""
    Yapily API

    To access endpoints that require authentication, use your application key and secret created in the Dashboard (https://dashboard.yapily.com)  # noqa: E501

    The version of the OpenAPI document: 0.0.359
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from yapily.configuration import Configuration


class InlineResponse2001ATM(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'atm_services': 'list[str]',
        'access24_hours_indicator': 'bool',
        'accessibility': 'list[str]',
        'branch': 'Branch',
        'identification': 'str',
        'location': 'Location',
        'minimum_possible_amount': 'str',
        'note': 'list[str]',
        'other_atm_services': 'list[InlineResponse2001OtherATMServices]',
        'other_accessibility': 'list[InlineResponse2001OtherAccessibility]',
        'supported_currencies': 'list[str]',
        'supported_languages': 'list[str]'
    }

    attribute_map = {
        'atm_services': 'ATMServices',
        'access24_hours_indicator': 'Access24HoursIndicator',
        'accessibility': 'Accessibility',
        'branch': 'Branch',
        'identification': 'Identification',
        'location': 'Location',
        'minimum_possible_amount': 'MinimumPossibleAmount',
        'note': 'Note',
        'other_atm_services': 'OtherATMServices',
        'other_accessibility': 'OtherAccessibility',
        'supported_currencies': 'SupportedCurrencies',
        'supported_languages': 'SupportedLanguages'
    }

    def __init__(self, atm_services=None, access24_hours_indicator=None, accessibility=None, branch=None, identification=None, location=None, minimum_possible_amount=None, note=None, other_atm_services=None, other_accessibility=None, supported_currencies=None, supported_languages=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse2001ATM - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._atm_services = None
        self._access24_hours_indicator = None
        self._accessibility = None
        self._branch = None
        self._identification = None
        self._location = None
        self._minimum_possible_amount = None
        self._note = None
        self._other_atm_services = None
        self._other_accessibility = None
        self._supported_currencies = None
        self._supported_languages = None
        self.discriminator = None

        if atm_services is not None:
            self.atm_services = atm_services
        if access24_hours_indicator is not None:
            self.access24_hours_indicator = access24_hours_indicator
        if accessibility is not None:
            self.accessibility = accessibility
        if branch is not None:
            self.branch = branch
        if identification is not None:
            self.identification = identification
        if location is not None:
            self.location = location
        if minimum_possible_amount is not None:
            self.minimum_possible_amount = minimum_possible_amount
        if note is not None:
            self.note = note
        if other_atm_services is not None:
            self.other_atm_services = other_atm_services
        if other_accessibility is not None:
            self.other_accessibility = other_accessibility
        if supported_currencies is not None:
            self.supported_currencies = supported_currencies
        if supported_languages is not None:
            self.supported_languages = supported_languages

    @property
    def atm_services(self):
        """Gets the atm_services of this InlineResponse2001ATM.  # noqa: E501


        :return: The atm_services of this InlineResponse2001ATM.  # noqa: E501
        :rtype: list[str]
        """
        return self._atm_services

    @atm_services.setter
    def atm_services(self, atm_services):
        """Sets the atm_services of this InlineResponse2001ATM.


        :param atm_services: The atm_services of this InlineResponse2001ATM.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["Balance", "BillPayments", "CashDeposits", "CharityDonation", "ChequeDeposits", "CashWithdrawal", "EnvelopeDeposit", "FastCash", "MobileBankingRegistration", "MobilePaymentRegistration", "MobilePhoneTopUp", "OrderStatement", "Other", "PINActivation", "PINChange", "PINUnblock", "MiniStatement"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(atm_services).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `atm_services` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(atm_services) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._atm_services = atm_services

    @property
    def access24_hours_indicator(self):
        """Gets the access24_hours_indicator of this InlineResponse2001ATM.  # noqa: E501


        :return: The access24_hours_indicator of this InlineResponse2001ATM.  # noqa: E501
        :rtype: bool
        """
        return self._access24_hours_indicator

    @access24_hours_indicator.setter
    def access24_hours_indicator(self, access24_hours_indicator):
        """Sets the access24_hours_indicator of this InlineResponse2001ATM.


        :param access24_hours_indicator: The access24_hours_indicator of this InlineResponse2001ATM.  # noqa: E501
        :type: bool
        """

        self._access24_hours_indicator = access24_hours_indicator

    @property
    def accessibility(self):
        """Gets the accessibility of this InlineResponse2001ATM.  # noqa: E501


        :return: The accessibility of this InlineResponse2001ATM.  # noqa: E501
        :rtype: list[str]
        """
        return self._accessibility

    @accessibility.setter
    def accessibility(self, accessibility):
        """Sets the accessibility of this InlineResponse2001ATM.


        :param accessibility: The accessibility of this InlineResponse2001ATM.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["AudioCashMachine", "AutomaticDoors", "ExternalRamp", "InductionLoop", "InternalRamp", "LevelAccess", "LowerLevelCounter", "Other", "WheelchairAccess"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(accessibility).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `accessibility` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(accessibility) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._accessibility = accessibility

    @property
    def branch(self):
        """Gets the branch of this InlineResponse2001ATM.  # noqa: E501


        :return: The branch of this InlineResponse2001ATM.  # noqa: E501
        :rtype: Branch
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this InlineResponse2001ATM.


        :param branch: The branch of this InlineResponse2001ATM.  # noqa: E501
        :type: Branch
        """

        self._branch = branch

    @property
    def identification(self):
        """Gets the identification of this InlineResponse2001ATM.  # noqa: E501


        :return: The identification of this InlineResponse2001ATM.  # noqa: E501
        :rtype: str
        """
        return self._identification

    @identification.setter
    def identification(self, identification):
        """Sets the identification of this InlineResponse2001ATM.


        :param identification: The identification of this InlineResponse2001ATM.  # noqa: E501
        :type: str
        """

        self._identification = identification

    @property
    def location(self):
        """Gets the location of this InlineResponse2001ATM.  # noqa: E501


        :return: The location of this InlineResponse2001ATM.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this InlineResponse2001ATM.


        :param location: The location of this InlineResponse2001ATM.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def minimum_possible_amount(self):
        """Gets the minimum_possible_amount of this InlineResponse2001ATM.  # noqa: E501


        :return: The minimum_possible_amount of this InlineResponse2001ATM.  # noqa: E501
        :rtype: str
        """
        return self._minimum_possible_amount

    @minimum_possible_amount.setter
    def minimum_possible_amount(self, minimum_possible_amount):
        """Sets the minimum_possible_amount of this InlineResponse2001ATM.


        :param minimum_possible_amount: The minimum_possible_amount of this InlineResponse2001ATM.  # noqa: E501
        :type: str
        """

        self._minimum_possible_amount = minimum_possible_amount

    @property
    def note(self):
        """Gets the note of this InlineResponse2001ATM.  # noqa: E501


        :return: The note of this InlineResponse2001ATM.  # noqa: E501
        :rtype: list[str]
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this InlineResponse2001ATM.


        :param note: The note of this InlineResponse2001ATM.  # noqa: E501
        :type: list[str]
        """

        self._note = note

    @property
    def other_atm_services(self):
        """Gets the other_atm_services of this InlineResponse2001ATM.  # noqa: E501


        :return: The other_atm_services of this InlineResponse2001ATM.  # noqa: E501
        :rtype: list[InlineResponse2001OtherATMServices]
        """
        return self._other_atm_services

    @other_atm_services.setter
    def other_atm_services(self, other_atm_services):
        """Sets the other_atm_services of this InlineResponse2001ATM.


        :param other_atm_services: The other_atm_services of this InlineResponse2001ATM.  # noqa: E501
        :type: list[InlineResponse2001OtherATMServices]
        """

        self._other_atm_services = other_atm_services

    @property
    def other_accessibility(self):
        """Gets the other_accessibility of this InlineResponse2001ATM.  # noqa: E501


        :return: The other_accessibility of this InlineResponse2001ATM.  # noqa: E501
        :rtype: list[InlineResponse2001OtherAccessibility]
        """
        return self._other_accessibility

    @other_accessibility.setter
    def other_accessibility(self, other_accessibility):
        """Sets the other_accessibility of this InlineResponse2001ATM.


        :param other_accessibility: The other_accessibility of this InlineResponse2001ATM.  # noqa: E501
        :type: list[InlineResponse2001OtherAccessibility]
        """

        self._other_accessibility = other_accessibility

    @property
    def supported_currencies(self):
        """Gets the supported_currencies of this InlineResponse2001ATM.  # noqa: E501


        :return: The supported_currencies of this InlineResponse2001ATM.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_currencies

    @supported_currencies.setter
    def supported_currencies(self, supported_currencies):
        """Sets the supported_currencies of this InlineResponse2001ATM.


        :param supported_currencies: The supported_currencies of this InlineResponse2001ATM.  # noqa: E501
        :type: list[str]
        """

        self._supported_currencies = supported_currencies

    @property
    def supported_languages(self):
        """Gets the supported_languages of this InlineResponse2001ATM.  # noqa: E501


        :return: The supported_languages of this InlineResponse2001ATM.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_languages

    @supported_languages.setter
    def supported_languages(self, supported_languages):
        """Sets the supported_languages of this InlineResponse2001ATM.


        :param supported_languages: The supported_languages of this InlineResponse2001ATM.  # noqa: E501
        :type: list[str]
        """

        self._supported_languages = supported_languages

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001ATM):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse2001ATM):
            return True

        return self.to_dict() != other.to_dict()