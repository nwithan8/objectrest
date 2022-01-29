import logging
from enum import Enum

import requests

from objectrest.utils import get_proxy_dict


class RequestType(Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    OPTIONS = 'OPTIONS'
    HEAD = 'HEAD'
    PATCH = 'PATCH'


def _add_params(use_proxy: bool = False, **kwargs) -> dict:
    if use_proxy:
        proxy_dict = get_proxy_dict()
        if not proxy_dict:
            raise Exception('No proxies available')
        kwargs['proxies'] = proxy_dict
    return kwargs


def _make_request(request_type: RequestType, url: str, session: requests.Session = None, use_proxy: bool = False,
                  log: bool = False, **kwargs) -> requests.Response:
    kwargs = _add_params(use_proxy=use_proxy, **kwargs)
    if log:
        logging.info(f'{request_type.value} {url}')

    if request_type == RequestType.GET:
        res = session.get(url, **kwargs) if session else requests.get(url, **kwargs)
    elif request_type == RequestType.POST:
        res = session.post(url, **kwargs) if session else requests.post(url, **kwargs)
    elif request_type == RequestType.PUT:
        res = session.put(url, **kwargs) if session else requests.put(url, **kwargs)
    elif request_type == RequestType.DELETE:
        res = session.delete(url, **kwargs) if session else requests.delete(url, **kwargs)
    elif request_type == RequestType.OPTIONS:
        res = session.options(url, **kwargs) if session else requests.options(url, **kwargs)
    elif request_type == RequestType.HEAD:
        res = session.head(url, **kwargs) if session else requests.head(url, **kwargs)
    elif request_type == RequestType.PATCH:
        res = session.patch(url, **kwargs) if session else requests.patch(url, **kwargs)
    else:
        raise Exception(f'Invalid request type: {request_type}')

    if log:
        logging.info(f"Response: {res}") if res else logging.error(f"Response: {res}")
    return res


def get(url: str, session: requests.Session = None, use_proxy: bool = False, log: bool = False, **kwargs) \
        -> requests.Response:
    """
    Return the requests.Response object from a GET request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    return _make_request(request_type=RequestType.GET, url=url, session=session, use_proxy=use_proxy, log=log,
                         **kwargs)


def options(url: str, session: requests.Session = None, use_proxy: bool = False, log: bool = False, **kwargs) \
        -> requests.Response:
    """
    Return the requests.Response object from an OPTIONS request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    return _make_request(request_type=RequestType.OPTIONS, url=url, session=session, use_proxy=use_proxy, log=log,
                         **kwargs)


def head(url: str, session: requests.Session = None, use_proxy: bool = False, log: bool = False, **kwargs) \
        -> requests.Response:
    """
    Return the requests.Response object from a HEAD request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    return _make_request(request_type=RequestType.HEAD, url=url, session=session, use_proxy=use_proxy, log=log,
                         **kwargs)


def post(url: str, session: requests.Session = None, use_proxy: bool = False, log: bool = False, **kwargs) \
        -> requests.Response:
    """
    Return the requests.Response object from a POST request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    return _make_request(request_type=RequestType.POST, url=url, session=session, use_proxy=use_proxy, log=log,
                         **kwargs)


def put(url: str, session: requests.Session = None, use_proxy: bool = False, log: bool = False, **kwargs) \
        -> requests.Response:
    """
    Return the requests.Response object from a PUT request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    return _make_request(request_type=RequestType.PUT, url=url, session=session, use_proxy=use_proxy, log=log,
                         **kwargs)


def patch(url: str, session: requests.Session = None, use_proxy: bool = False, log: bool = False, **kwargs) \
        -> requests.Response:
    """
    Return the requests.Response object from a PATCH request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    return _make_request(request_type=RequestType.PATCH, url=url, session=session, use_proxy=use_proxy, log=log,
                         **kwargs)


def delete(url: str, session: requests.Session = None, use_proxy: bool = False, log: bool = False, **kwargs) \
        -> requests.Response:
    """
    Return the requests.Response object from a DELETE request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    return _make_request(request_type=RequestType.DELETE, url=url, session=session, use_proxy=use_proxy, log=log,
                         **kwargs)
