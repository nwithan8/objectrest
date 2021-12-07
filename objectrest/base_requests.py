import requests
from objectrest.utils import get_proxy_dict


def _add_params(use_proxy: bool = False, **kwargs) -> dict:
    if use_proxy:
        kwargs['proxies'] = get_proxy_dict()
    return kwargs


def get(url: str, session: requests.Session = None, use_proxy: bool = False, **kwargs) -> requests.Response:
    """
    Return the requests.Response object from a GET request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    kwargs = _add_params(use_proxy=use_proxy, **kwargs)
    if session:
        res = session.get(url=url, **kwargs)
    else:
        res = requests.get(url=url, **kwargs)
    return res


def post(url: str, session: requests.Session = None, **kwargs) -> requests.Response:
    """
    Return the requests.Response object from a POST request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    kwargs = _add_params(use_proxy=use_proxy, **kwargs)
    if session:
        res = session.post(url=url, **kwargs)
    else:
        res = requests.post(url=url, **kwargs)
    return res


def put(url: str, session: requests.Session = None, use_proxy: bool = False, **kwargs) -> requests.Response:
    """
    Return the requests.Response object from a PUT request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    kwargs = _add_params(use_proxy=use_proxy, **kwargs)
    if session:
        res = session.put(url=url, **kwargs)
    else:
        res = requests.put(url=url, **kwargs)
    return res


def patch(url: str, session: requests.Session = None, use_proxy: bool = False, **kwargs) -> requests.Response:
    """
    Return the requests.Response object from a PATCH request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    kwargs = _add_params(use_proxy=use_proxy, **kwargs)
    if session:
        res = session.patch(url=url, **kwargs)
    else:
        res = requests.patch(url=url, **kwargs)
    return res


def delete(url: str, session: requests.Session = None, use_proxy: bool = False, **kwargs) -> requests.Response:
    """
    Return the requests.Response object from a DELETE request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    kwargs = _add_params(use_proxy=use_proxy, **kwargs)
    if session:
        res = session.delete(url=url, **kwargs)
    else:
        res = requests.delete(url=url, **kwargs)
    return res
