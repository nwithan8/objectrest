from functools import wraps
from typing import Union


def request_handler_request(func):
    @wraps(func)
    def wrapper(self, **kwargs) -> Union[dict, object]:
        """
        Create the full URL, params and headers for a RequestHandler request

        :param self:
        :type self:
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        kwargs['url'] = self._make_url(local_url=kwargs.get('url'))
        kwargs['params'] = self._make_params(local_params=kwargs.get('params'))
        kwargs['headers'] = self._make_headers(local_headers=kwargs.get('headers'))
        return func(self, **kwargs)

    return wrapper
