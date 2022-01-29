from requests import Response, Session as RequestsSession


class Session:
    def __init__(self):
        self._session = RequestsSession()

    def get(self, url, **kwargs) -> Response:
        return self._session.get(url, **kwargs)

    def post(self, url, **kwargs) -> Response:
        return self._session.post(url, **kwargs)

    def put(self, url, **kwargs) -> Response:
        return self._session.put(url, **kwargs)

    def delete(self, url, **kwargs) -> Response:
        return self._session.delete(url, **kwargs)

    def patch(self, url, **kwargs) -> Response:
        return self._session.patch(url, **kwargs)

    def head(self, url, **kwargs) -> Response:
        return self._session.head(url, **kwargs)

    def options(self, url, **kwargs) -> Response:
        return self._session.options(url, **kwargs)
