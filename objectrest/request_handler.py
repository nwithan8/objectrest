from requests_oauthlib import OAuth2Session
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient

import objectrest
from objectrest import utils
from objectrest.object_handler import *
from objectrest.decorators import request_handler_request


class RequestHandler:
    def __init__(self,
                 base_url: str = None,
                 universal_parameters: dict = None,
                 universal_headers: dict = None,
                 log_requests: bool = False):
        """
        Create a reusable request handler
        Set universal parameters and headers used for all requests
        Reuses session for all requests

        :param base_url: Base URL of all requests
        :type base_url: str, optional
        :param universal_parameters: Dictionary of parameters to include in all requests (i.e. API token, language)
        :type universal_parameters: dict, optional
        :param universal_headers: Dictionary of header to include in all requests (i.e. API token, user agent)
        :type universal_parameters: dict, optional
        :param log_requests: whether to log the request (default False)
        :type log_requests: bool, optional
        """
        self.base_url = base_url
        self.params = universal_parameters
        self.headers = universal_headers
        self._log = log_requests
        self._session = objectrest.Session()

    def _make_url(self, local_url: str = None) -> str:
        if not local_url:
            if not self.base_url:
                raise Exception("No URL provided.")
            return self.base_url

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
    def get(self, url: str, use_proxy: bool = False, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a GET request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return get(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def get_json(self, url: str, use_proxy: bool = False, **kwargs) -> dict:
        """
        Return the JSON data from a GET request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: a JSON dictionary
        :rtype: dict
        """
        return get_json(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def get_object(self, url: str, model: type, sub_keys: List = None, extract_list: bool = False,
                   use_proxy: bool = False, **kwargs) -> Union[object, None]:
        """
        Parse the JSON data from a GET request into an object
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: an object
        :rtype: object
        """
        return get_object(url=url, model=model, sub_keys=sub_keys, extract_list=extract_list, session=self._session,
                          use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def options(self, url: str, use_proxy: bool = False, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from an OPTIONS request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return options(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def head(self, url: str, use_proxy: bool = False, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a HEAD request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return head(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def post(self, url: str, use_proxy: bool = False, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a POST request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return post(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def post_json(self, url: str, use_proxy: bool = False, **kwargs) -> dict:
        """
        Return the JSON data from a POST request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: a JSON dictionary
        :rtype: dict
        """
        return post_json(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def post_object(self, url: str, model: type, sub_keys: List = None, extract_list: bool = False,
                    use_proxy: bool = False, **kwargs) -> Union[object, None]:
        """
        Parse the JSON data from a POST request into an object
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: an object
        :rtype: object
        """
        return post_object(url=url, model=model, sub_keys=sub_keys, extract_list=extract_list, session=self._session,
                           use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def put(self, url: str, use_proxy: bool = False, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a PUT request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return put(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def put_json(self, url: str, use_proxy: bool = False, **kwargs) -> dict:
        """
        Return the JSON data from a PUT request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: a JSON dictionary
        :rtype: dict
        """
        return put_json(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def put_object(self, url: str, model: type, sub_keys: List = None, extract_list: bool = False,
                   use_proxy: bool = False, **kwargs) -> Union[object, None]:
        """
        Parse the JSON data from a PUT request into an object
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: an object
        :rtype: object
        """
        return put_object(url=url, model=model, sub_keys=sub_keys, extract_list=extract_list, session=self._session,
                          use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def patch(self, url: str, use_proxy: bool = False, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a PATCH request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return patch(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def patch_json(self, url: str, use_proxy: bool = False, **kwargs) -> dict:
        """
        Return the JSON data from a PATCH request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: a JSON dictionary
        :rtype: dict
        """
        return patch_json(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def patch_object(self, url: str, model: type, sub_keys: List = None, extract_list: bool = False,
                     use_proxy: bool = False, **kwargs) -> Union[object, None]:
        """
        Parse the JSON data from a PATCH request into an object
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: an object
        :rtype: object
        """
        return patch_object(url=url, model=model, sub_keys=sub_keys, extract_list=extract_list, session=self._session,
                            use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def delete(self, url: str, use_proxy: bool = False, **kwargs) -> requests.Response:
        """
        Return the requests.Response object from a DELETE request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: A Requests.Response object
        :rtype: requests.Response
        """
        return delete(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def delete_json(self, url: str, use_proxy: bool = False, **kwargs) -> dict:
        """
        Return the JSON data from a DELETE request
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: a JSON dictionary
        :rtype: dict
        """
        return delete_json(url=url, session=self._session, use_proxy=use_proxy, log=self._log, **kwargs)

    @request_handler_request
    def delete_object(self, url: str, model: type, sub_keys: List = None, extract_list: bool = False,
                      use_proxy: bool = False, **kwargs) -> Union[object, None]:
        """
        Parse the JSON data from a DELETE request into an object
        Automatically appends base URL, universal params and headers, reuses session

        :param url: URL endpoint to append to base URL
        :type url: str
        :param model: a Pydantic model to generate from the response JSON data
        :type model: type
        :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
        :type sub_keys: list, optional
        :param extract_list: If top-level of JSON is a list, whether to convert each list item into model or treat entire JSON as a whole object
        :type extract_list: bool
        :param use_proxy: whether to use a random proxy for your request (default False)
        :type use_proxy: bool, optional
        :param kwargs: Keyword arguments to pass to Requests library
        :type kwargs: dict, optional
        :return: an object
        :rtype: object
        """
        return delete_object(url=url, model=model, sub_keys=sub_keys, extract_list=extract_list, session=self._session,
                             use_proxy=use_proxy, log=self._log, **kwargs)


class ApiTokenRequestHandler(RequestHandler):
    def __init__(self,
                 api_token: str,
                 api_token_keyword: str,
                 base_url: str = None,
                 universal_parameters: dict = None,
                 universal_headers: dict = None,
                 include_key_in_header: bool = False,
                 log_requests: bool = False):
        """
        Create a reusable request handler to handle requests requiring API tokens
        Set universal parameters and headers used for all requests
        Reuses session for all requests

        :param base_url: Base URL of all requests
        :type base_url: str, optional
        :param universal_parameters: Dictionary of parameters to include in all requests (i.e. API token, language)
        :type universal_parameters: dict, optional
        :param universal_headers: Dictionary of header to include in all requests (i.e. API token, user agent)
        :type universal_parameters: dict, optional
        :param api_token: The API token needed for each request
        :type api_token: str
        :param api_token_keyword: Name of the API token parameter expected by the API (i.e "token", "key", "api_key")
        :type api_token_keyword: str
        :param include_key_in_header: Whether to include API token in header (included as URL param otherwise)
        :type include_key_in_header: bool, optional
        :param log_requests: whether to log the request (default False)
        :type log_requests: bool, optional
        """
        headers = {}
        params = {}
        if universal_headers:
            headers.update(universal_headers)
        if universal_parameters:
            params.update(universal_parameters)

        if include_key_in_header:
            headers[api_token_keyword] = api_token
        else:
            params[api_token_keyword] = api_token

        super().__init__(base_url, universal_parameters=params, universal_headers=headers, log_requests=log_requests)


class OAuth2RequestHandler(RequestHandler):
    def __init__(self,
                 client_id: str,
                 client_secret: str,
                 authorization_url: str,
                 base_url: str = None,
                 universal_parameters: dict = None,
                 universal_headers: dict = None,
                 log_requests: bool = False):
        """
        Create a reusable request handler to handle requests requiring API tokens
        Set universal parameters and headers used for all requests
        Reuses session for all requests

        :param base_url: Base URL of all requests
        :type base_url: str, optional
        :param universal_parameters: Dictionary of parameters to include in all requests (i.e. API token, language)
        :type universal_parameters: dict, optional
        :param universal_headers: Dictionary of header to include in all requests (i.e. API token, user agent)
        :type universal_parameters: dict, optional
        :param client_id: The client ID required to authenticate each request
        :type client_id: str
        :param client_secret: The client secret required to authenticate each request
        :type client_secret: str
        :param authorization_url: The URL to exchange client ID + secret for a token on each request
        :type authorization_url: str
        :param log_requests: whether to log the request (default False)
        :type log_requests: bool, optional
        """
        super().__init__(base_url=base_url, universal_parameters=universal_parameters,
                         universal_headers=universal_headers, log_requests=log_requests)
        self._client_id = client_id
        self._client_secret = client_secret
        self._auth_url = authorization_url

        self._tokens = self._authorize()

    def _authorize(self) -> dict:
        """
        Access token seems to be valid for a month
        Refresh token seems to be valid for a year

        :return:
        :rtype:
        """
        auth = HTTPBasicAuth(self._client_id, self._client_secret)
        client = BackendApplicationClient(client_id=self._client_id)
        oauth = OAuth2Session(client=client)
        return oauth.fetch_token(token_url=self._auth_url, auth=auth)

    def _get_access_token(self) -> str:
        """
        Handle refreshing tokens if needed

        :return:
        :rtype:
        """
        # If not authorized already
        if not self._tokens:
            self._authorize()

        # If access token has expired
        access_token_expiration_timestamp = self._tokens.get('access_token_expires_in')
        if not access_token_expiration_timestamp \
                or utils.timestamp_is_expired(timestamp=access_token_expiration_timestamp):
            self._authorize()

        if not self._tokens:
            raise Exception("Could not get tokens from the API.")

        access_token = self._tokens.get('access_token')
        if not access_token:
            raise Exception("No access token provided by the API.")
        return access_token

    def _make_headers(self, local_headers: dict = None) -> dict:
        """
        Retrieve access token to make headers for an OAuth2 request

        :param local_headers:
        :return:
        """
        headers = super()._make_headers(local_headers=local_headers)

        access_token = self._get_access_token()
        headers['Authorization'] = f"Bearer {access_token}"

        return headers
