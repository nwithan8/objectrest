import requests


def get(url: str, session: requests.Session = None, **kwargs) -> requests.Response:
    """
    Return the requests.Response object from a GET request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
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
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    if session:
        res = session.post(url=url, **kwargs)
    else:
        res = requests.post(url=url, **kwargs)
    return res


def put(url: str, session: requests.Session = None, **kwargs) -> requests.Response:
    """
    Return the requests.Response object from a PUT request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    if session:
        res = session.put(url=url, **kwargs)
    else:
        res = requests.put(url=url, **kwargs)
    return res


def patch(url: str, session: requests.Session = None, **kwargs) -> requests.Response:
    """
    Return the requests.Response object from a PATCH request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    if session:
        res = session.patch(url=url, **kwargs)
    else:
        res = requests.patch(url=url, **kwargs)
    return res


def delete(url: str, session: requests.Session = None, **kwargs) -> requests.Response:
    """
    Return the requests.Response object from a DELETE request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a requests.Response object
    :rtype: requests.Response
    """
    if session:
        res = session.delete(url=url, **kwargs)
    else:
        res = requests.delete(url=url, **kwargs)
    return res
