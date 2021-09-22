from objectrest.base_requests import *


def _parse_response_json(response: requests.Response = None) -> dict:
    """
    Parse the JSON data from the response

    :param response:
    :type response:
    :return:
    :rtype:
    """
    if not response:
        return {}

    try:
        return response.json()
    except:
        return {}


def get_json(url: str, session: requests.Session = None, **kwargs) -> dict:
    """
    Return the JSON data from a GET request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res = get(url=url, session=session, **kwargs)
    return _parse_response_json(response=res)


def post_json(url: str, session: requests.Session = None, **kwargs) -> dict:
    """
    Return the JSON data from a POST request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res = post(url=url, session=session, **kwargs)
    return _parse_response_json(response=res)


def put_json(url: str, session: requests.Session = None, **kwargs) -> dict:
    """
    Return the JSON data from a PUT request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res = put(url=url, session=session, **kwargs)
    return _parse_response_json(response=res)


def patch_json(url: str, session: requests.Session = None, **kwargs) -> dict:
    """
    Return the JSON data from a PATCH request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res = patch(url=url, session=session, **kwargs)
    return _parse_response_json(response=res)


def delete_json(url: str, session: requests.Session = None, **kwargs) -> dict:
    """
    Return the JSON data from a DELETE request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res = delete(url=url, session=session, **kwargs)
    return _parse_response_json(response=res)
