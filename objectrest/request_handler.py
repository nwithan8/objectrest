from objectrest.object_handler import *
from objectrest.decorators import request_handler_request


class RequestHandler:
    def __init__(self,
                 base_url: str = None,
                 universal_parameters: dict = None,
                 universal_headers: dict = None):
        self.base_url = base_url
        self.params = universal_parameters
        self.headers = universal_headers
        self._session = requests.Session()

    def _make_url(self, local_url: str) -> str:
        if not self.base_url:
            return local_url

        base = self.base_url
        if base.endswith("/"):
            base = base[:-1]

        if local_url.startswith("/"):
            local_url = local_url[1:]

        return f"{base}/{local_url}"

    def _make_params(self, local_params: dict = None) -> dict:
        params = {}

        if self.params:
            params.update(self.params)

        if local_params:
            params.update(local_params)

        return params

    def _make_headers(self, local_headers: dict = None) -> dict:
        headers = {}

        if self.headers:
            headers.update(self.headers)

        if local_headers:
            headers.update(local_headers)

        return headers

    @request_handler_request
    def get(self, url: str, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a GET request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return get(url=url, session=self._session, **kwargs)

    @request_handler_request
    def get_json(self, url: str, **kwargs) -> dict:
        """
        Return the JSON data from a GET request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: a JSON dictionary
        :rtype: dict
        """
        return get_json(url=url, session=self._session, **kwargs)

    @request_handler_request
    def get_object(self, url: str, model: type, **kwargs) -> Union[object, None]:
        """
        Parse the JSON data from a GET request into an object
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: an object
        :rtype: object
        """
        return get_object(url=url, model=model, session=self._session, **kwargs)

    @request_handler_request
    def post(self, url: str, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a POST request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return post(url=url, session=self._session, **kwargs)

    @request_handler_request
    def post_json(self, url: str, **kwargs) -> dict:
        """
        Return the JSON data from a POST request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: a JSON dictionary
        :rtype: dict
        """
        return post_json(url=url, session=self._session, **kwargs)

    @request_handler_request
    def post_object(self, url: str, model: type, **kwargs) -> Union[object, None]:
        """
        Parse the JSON data from a POST request into an object
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: an object
        :rtype: object
        """
        return post_object(url=url, model=model, session=self._session, **kwargs)

    @request_handler_request
    def put(self, url: str, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a PUT request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return put(url=url, session=self._session, **kwargs)

    @request_handler_request
    def put_json(self, url: str, **kwargs) -> dict:
        """
        Return the JSON data from a PUT request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: a JSON dictionary
        :rtype: dict
        """
        return put_json(url=url, session=self._session, **kwargs)

    @request_handler_request
    def put_object(self, url: str, model: type, **kwargs) -> Union[object, None]:
        """
        Parse the JSON data from a PUT request into an object
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: an object
        :rtype: object
        """
        return put_object(url=url, model=model, session=self._session, **kwargs)

    @request_handler_request
    def patch(self, url: str, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a PATCH request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return patch(url=url, session=self._session, **kwargs)

    @request_handler_request
    def patch_json(self, url: str, **kwargs) -> dict:
        """
        Return the JSON data from a PATCH request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: a JSON dictionary
        :rtype: dict
        """
        return patch_json(url=url, session=self._session, **kwargs)

    @request_handler_request
    def patch_object(self, url: str, model: type, **kwargs) -> Union[object, None]:
        """
        Parse the JSON data from a PATCH request into an object
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: an object
        :rtype: object
        """
        return patch_object(url=url, model=model, session=self._session, **kwargs)

    @request_handler_request
    def delete(self, url: str, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a DELETE request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return delete(url=url, session=self._session, **kwargs)

    @request_handler_request
    def delete_json(self, url: str, **kwargs) -> dict:
        """
        Return the JSON data from a DELETE request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: a JSON dictionary
        :rtype: dict
        """
        return delete_json(url=url, session=self._session, **kwargs)

    @request_handler_request
    def delete_object(self, url: str, model: type, **kwargs) -> Union[object, None]:
        """
        Parse the JSON data from a DELETE request into an object
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict
        :return: an object
        :rtype: object
        """
        return delete_object(url=url, model=model, session=self._session, **kwargs)
