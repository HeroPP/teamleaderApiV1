from enum import Enum
from typing import Any, Iterator, Optional

import requests
from ratelimit import limits, sleep_and_retry
from requests import Response

from .tasks import Tasks


class Client:
    def __init__(
        self,
        api_group="163402",
        api_secret="Jlu9betJ2dJ00DHrzxuLOUBi6o9dP5TzoHCdDcWgNI9Z2l76GIwM7JaUDAMlku0xvZ3I6y2aWMlQTfWv5B5MMoPSec1iU8l"
        + "pzsWTHIiWC8EAOIhB7Vdt03CFng1vtBoEeV9CVHIpfMqpQlWCwqMUqXCwejTaxoc9niY58hl20ksZk35FjSwqHxa1O4V"
        + "4MtXn4zN6umhO",
    ):
        self.api_data = {"api_group": api_group, "api_secret": api_secret}
        self.tasks = Tasks(self.get_request, self.post_request)

    @sleep_and_retry
    @limits(calls=100, period=60)
    def teamleader_request(
        self, method, url_addition: str, additional_data
    ) -> Response:
        """

        :param method:
        :param url_addition:
        :param additional_data:
        :return:
        """
        if not url_addition:
            raise ValueError("No url_addition typed")
        additional_data = self._tranform_enums(additional_data)
        additional_data.update(self.api_data)
        url = f"https://app.teamleader.eu/api/{url_addition}.php"
        response = method(url, data=additional_data)
        response.raise_for_status()
        return response

    def post_request(
        self, url_addition: Any, additional_data: Optional[dict] = None
    ) -> Response:
        """

        :param url_addition:
        :param additional_data:
        :return:
        """
        if additional_data is None:
            additional_data = {}
        return self.teamleader_request(requests.post, url_addition, additional_data)

    def get_request(
        self, url_addition: str, additional_data: Optional[dict] = None
    ) -> Response:
        """

        :param url_addition:
        :param additional_data:
        :return:
        """
        if additional_data is None:
            additional_data = {}
        additional_data.update({"Content-Type": "application/json"})
        return self.teamleader_request(requests.get, url_addition, additional_data)

    def _tranform_enums(self, additional_data):
        for key, value in additional_data.items():
            if isinstance(value, Enum):
                additional_data[key] = value.value

        return additional_data
