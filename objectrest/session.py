from objectrest.response import Response, AsyncResponse
from requests import Session as RequestsSession
from httpx import Client as HTTPXClient


class Session:
    def __init__(self):
        self._session: RequestsSession = RequestsSession()

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

    def request(self, method, url, **kwargs) -> Response:
        return self._session.request(method, url, **kwargs)


class AsyncSession:
    def __init__(self):
        self._session: HTTPXClient = HTTPXClient()

    async def get(self, url, **kwargs) -> AsyncResponse:
        async with self._session as session:
            return await session.get(url, **kwargs)

    async def post(self, url, **kwargs) -> AsyncResponse:
        async with self._session as session:
            return await session.post(url, **kwargs)

    async def put(self, url, **kwargs) -> AsyncResponse:
        async with self._session as session:
            return await session.put(url, **kwargs)

    async def delete(self, url, **kwargs) -> AsyncResponse:
        async with self._session as session:
            return await session.delete(url, **kwargs)

    async def patch(self, url, **kwargs) -> AsyncResponse:
        async with self._session as session:
            return await session.patch(url, **kwargs)

    async def head(self, url, **kwargs) -> AsyncResponse:
        async with self._session as session:
            return await session.head(url, **kwargs)

    async def options(self, url, **kwargs) -> AsyncResponse:
        async with self._session as session:
            return await session.options(url, **kwargs)

    async def request(self, method, url, **kwargs) -> AsyncResponse:
        async with self._session as session:
            return await session.request(method, url, **kwargs)
