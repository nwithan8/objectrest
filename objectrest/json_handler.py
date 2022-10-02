from typing import Union

from objectrest.base_requests import (
    get,
    post,
    put,
    patch,
    delete,
    async_get,
    async_post,
    async_put,
    async_patch,
    async_delete,
)
from objectrest.session import (
    Session,
    AsyncSession
)
from objectrest.response import (
    Response,
    AsyncResponse
)


def _parse_response_json(response: Union[Response, AsyncResponse] = None) -> dict:
    """
    Parse the JSON data from the response

    :param response: the response from the request
    :type response: objectrest.response.Response or objectrest.response.AsyncResponse
    :return: a JSON dictionary
    :rtype: dict
    """
    if not response:
        return {}

    try:
        return response.json()
    except:
        return {}


# Synchronous requests


def get_json(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs
) -> dict:
    """
    Return the JSON data from a GET request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: an objectrest.Session to use for the API call (optional)
    :type session: objectrest.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to the Requests library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res: Response = get(url=url, session=session, use_proxy=use_proxy, log=log, **kwargs)
    return _parse_response_json(response=res)


def post_json(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs
) -> dict:
    """
    Return the JSON data from a POST request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: an objectrest.Session to use for the API call (optional)
    :type session: objectrest.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to the Requests library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res: Response = post(url=url, session=session, use_proxy=use_proxy, log=log, **kwargs)
    return _parse_response_json(response=res)


def put_json(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs
) -> dict:
    """
    Return the JSON data from a PUT request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: an objectrest.Session to use for the API call (optional)
    :type session: objectrest.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to the Requests library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res: Response = put(url=url, session=session, use_proxy=use_proxy, log=log, **kwargs)
    return _parse_response_json(response=res)


def patch_json(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs
) -> dict:
    """
    Return the JSON data from a PATCH request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: an objectrest.Session to use for the API call (optional)
    :type session: objectrest.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to the Requests library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res: Response = patch(url=url, session=session, use_proxy=use_proxy, log=log, **kwargs)
    return _parse_response_json(response=res)


def delete_json(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs
) -> dict:
    """
    Return the JSON data from a DELETE request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: an objectrest.Session to use for the API call (optional)
    :type session: objectrest.Session, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to the Requests library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res: Response = delete(url=url, session=session, use_proxy=use_proxy, log=log, **kwargs)
    return _parse_response_json(response=res)


# Asynchronous requests


async def async_get_json(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs
) -> dict:
    """
    Return the JSON data from an asynchronous GET request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: an objectrest.AsyncSession to use for the API call (optional)
    :type session: objectrest.AsyncSession, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to the HTTPX library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res: AsyncResponse = await async_get(
        url=url, session=session, use_proxy=use_proxy, log=log, **kwargs
    )
    return _parse_response_json(response=res)


async def async_post_json(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs
) -> dict:
    """
    Return the JSON data from an asynchronous POST request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: an objectrest.AsyncSession to use for the API call (optional)
    :type session: objectrest.AsyncSession, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to the HTTPX library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res: AsyncResponse = await async_post(
        url=url, session=session, use_proxy=use_proxy, log=log, **kwargs
    )
    return _parse_response_json(response=res)


async def async_put_json(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs
) -> dict:
    """
    Return the JSON data from an asynchronous PUT request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: an objectrest.AsyncSession to use for the API call (optional)
    :type session: objectrest.AsyncSession, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to the HTTPX library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res: AsyncResponse = await async_put(
        url=url, session=session, use_proxy=use_proxy, log=log, **kwargs
    )
    return _parse_response_json(response=res)


async def async_patch_json(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs
) -> dict:
    """
    Return the JSON data from an asynchronous PATCH request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: an objectrest.AsyncSession to use for the API call (optional)
    :type session: objectrest.AsyncSession, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to the HTTPX library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res: AsyncResponse = await async_patch(
        url=url, session=session, use_proxy=use_proxy, log=log, **kwargs
    )
    return _parse_response_json(response=res)


async def async_delete_json(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs
) -> dict:
    """
    Return the JSON data from an asynchronous DELETE request

    :param url: URL endpoint to append to base URL
    :type url: str
    :param session: an objectrest.AsyncSession to use for the API call (optional)
    :type session: objectrest.AsyncSession, optional
    :param use_proxy: whether to use a random proxy for your request (default False)
    :type use_proxy: bool, optional
    :param log: whether to log the request (default False)
    :type log: bool, optional
    :param kwargs: Keyword arguments to pass to the HTTPX library
    :type kwargs: dict, optional
    :return: a JSON dictionary
    :rtype: dict
    """
    res: AsyncResponse = await async_delete(
        url=url, session=session, use_proxy=use_proxy, log=log, **kwargs
    )
    return _parse_response_json(response=res)
