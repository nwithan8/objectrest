import logging
from enum import Enum
from typing import Union

from objectrest.session import Session, AsyncSession
from objectrest.response import Response, AsyncResponse
from objectrest.utils import get_proxy_dict


class RequestType(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
    HEAD = "HEAD"
    PATCH = "PATCH"

    def __str__(self) -> str:
        return self.str_value

    @property
    def str_value(self) -> str:
        return str(self.value)


def _add_params(use_proxy: bool = False, **kwargs) -> dict:
    if use_proxy:
        proxy_dict: Union[dict, None] = get_proxy_dict()
        if not proxy_dict:
            raise Exception("No proxies available")
        kwargs["proxies"]: dict = proxy_dict
    return kwargs


# Synchronous requests


def _make_request(
        request_type: RequestType,
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> Response:
    kwargs: dict = _add_params(use_proxy=use_proxy, **kwargs)
    if log:
        logging.info(f"{request_type.value} {url}")

    if not session:
        session: Session = Session()

    res: Response = session.request(method=request_type.str_value, url=url, **kwargs)

    if log:
        logging.info(f"Response: {res}") if res else logging.error(f"Response: {res}")
    return res


def get(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> Response:
    """
    Return the Response object from a GET request

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
    :return: a Response object
    :rtype: Response
    """
    return _make_request(
        request_type=RequestType.GET,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


def options(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> Response:
    """
    Return the Response object from an OPTIONS request

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
    :return: a Response object
    :rtype: Response
    """
    return _make_request(
        request_type=RequestType.OPTIONS,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


def head(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> Response:
    """
    Return the Response object from a HEAD request

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
    :return: a Response object
    :rtype: Response
    """
    return _make_request(
        request_type=RequestType.HEAD,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


def post(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> Response:
    """
    Return the Response object from a POST request

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
    :return: a Response object
    :rtype: Response
    """
    return _make_request(
        request_type=RequestType.POST,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


def put(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> Response:
    """
    Return the Response object from a PUT request

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
    :return: a Response object
    :rtype: Response
    """
    return _make_request(
        request_type=RequestType.PUT,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


def patch(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> Response:
    """
    Return the Response object from a PATCH request

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
    :return: a Response object
    :rtype: Response
    """
    return _make_request(
        request_type=RequestType.PATCH,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


def delete(
        url: str,
        session: Session = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> Response:
    """
    Return the Response object from a DELETE request

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
    :return: a Response object
    :rtype: Response
    """
    return _make_request(
        request_type=RequestType.DELETE,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


# Asynchronous requests


async def _async_make_request(
        request_type: RequestType,
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> AsyncResponse:
    kwargs: dict = _add_params(use_proxy=use_proxy, **kwargs)
    if log:
        logging.info(f"{request_type.value} {url}")

    if not session:
        session: AsyncSession = AsyncSession()

    async with session:
        res: AsyncResponse = await session.request(method=request_type.str_value, url=url, **kwargs)

    if log:
        logging.info(f"Response: {res}") if res else logging.error(f"Response: {res}")
    return res


async def async_get(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> AsyncResponse:
    """
    Return the AsyncResponse object from an asynchronous GET request

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
    :return: an AsyncResponse object
    :rtype: AsyncResponse
    """
    return await _async_make_request(
        request_type=RequestType.GET,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


async def async_options(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> AsyncResponse:
    """
    Return the AsyncResponse object from an asynchronous OPTIONS request

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
    :return: an AsyncResponse object
    :rtype: AsyncResponse
    """
    return await _async_make_request(
        request_type=RequestType.OPTIONS,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


async def async_head(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> AsyncResponse:
    """
    Return the AsyncResponse object from an asynchronous HEAD request

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
    :return: an AsyncResponse object
    :rtype: AsyncResponse
    """
    return await _async_make_request(
        request_type=RequestType.HEAD,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


async def async_post(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> AsyncResponse:
    """
    Return the AsyncResponse object from an asynchronous POST request

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
    :return: an AsyncResponse object
    :rtype: AsyncResponse
    """
    return await _async_make_request(
        request_type=RequestType.POST,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


async def async_put(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> AsyncResponse:
    """
    Return the AsyncResponse object from an asynchronous PUT request

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
    :return: an AsyncResponse object
    :rtype: AsyncResponse
    """
    return await _async_make_request(
        request_type=RequestType.PUT,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


async def async_patch(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> AsyncResponse:
    """
    Return the AsyncResponse object from an asynchronous PATCH request

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
    :return: an AsyncResponse object
    :rtype: AsyncResponse
    """
    return await _async_make_request(
        request_type=RequestType.PATCH,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )


async def async_delete(
        url: str,
        session: AsyncSession = None,
        use_proxy: bool = False,
        log: bool = False,
        **kwargs,
) -> AsyncResponse:
    """
    Return the AsyncResponse object from an asynchronous DELETE request

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
    :return: an AsyncResponse object
    :rtype: AsyncResponse
    """
    return await _async_make_request(
        request_type=RequestType.DELETE,
        url=url,
        session=session,
        use_proxy=use_proxy,
        log=log,
        **kwargs,
    )
