# coding: utf-8

"""
    OpenAPI Specification of DeepAffects audio APIs

    OpenAPI spec version: v1
"""

from pprint import pformat

from six import iteritems


class AsyncResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self, request_id=None, api=None):
        """
        AsyncResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'request_id': 'str',
            'api': 'str'
        }

        self.attribute_map = {
            'request_id': 'request_id',
            'api': 'api'
        }

        self._request_id = request_id
        self._api = api

    @property
    def request_id(self):
        """
        Gets the request_id of this AsyncResponse.
        Unique identifier for the api call

        :return: The request_id of this AsyncResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this AsyncResponse.
        Unique identifier for the api call

        :param request_id: The request_id of this AsyncResponse.
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")

        self._request_id = request_id

    @property
    def api(self):
        """
        Gets the api of this AsyncResponse.
        API hit

        :return: The api of this AsyncResponse.
        :rtype: str
        """
        return self._api

    @api.setter
    def api(self, api):
        """
        Sets the api of this AsyncResponse.
        API hit

        :param api: The api of this AsyncResponse.
        :type: str
        """
        if api is None:
            raise ValueError("Invalid value for `api`, must not be `None`")

        self._api = api

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
        if not isinstance(other, AsyncResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
