import logging

import pytest

import objectrest

URL = "https://httpbin.org/anything"


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    logging.basicConfig(level=logging.DEBUG)


def test_get():
    res = objectrest.get(url=URL, log=True)
    assert res.request.method == "GET"
    assert res.status_code == 200


def test_options():
    res = objectrest.options(url=URL, log=True)
    assert res.request.method == "OPTIONS"
    assert res.status_code == 200


def test_head():
    res = objectrest.head(url=URL, log=True)
    assert res.request.method == "HEAD"
    assert res.status_code == 200


def test_post():
    res = objectrest.post(url=URL, log=True)
    assert res.request.method == "POST"
    assert res.status_code == 200


def test_put():
    res = objectrest.put(url=URL, log=True)
    assert res.request.method == "PUT"
    assert res.status_code == 200


def test_patch():
    res = objectrest.patch(url=URL, log=True)
    assert res.request.method == "PATCH"
    assert res.status_code == 200


def test_delete():
    res = objectrest.delete(url=URL, log=True)
    assert res.request.method == "DELETE"
    assert res.status_code == 200


def test_get_with_session():
    session = objectrest.Session()
    res = objectrest.get(url=URL, session=session, log=True)
    assert res.request.method == "GET"
    assert res.status_code == 200


def test_post_with_session():
    session = objectrest.Session()
    res = objectrest.post(url=URL, session=session, log=True)
    assert res.request.method == "POST"
    assert res.status_code == 200


def test_put_with_session():
    session = objectrest.Session()
    res = objectrest.put(url=URL, session=session, log=True)
    assert res.request.method == "PUT"
    assert res.status_code == 200


def test_delete_with_session():
    session = objectrest.Session()
    res = objectrest.delete(url=URL, session=session, log=True)
    assert res.request.method == "DELETE"
    assert res.status_code == 200


def test_patch_with_session():
    session = objectrest.Session()
    res = objectrest.patch(url=URL, session=session, log=True)
    assert res.request.method == "PATCH"
    assert res.status_code == 200


def test_head_with_session():
    session = objectrest.Session()
    res = objectrest.head(url=URL, session=session, log=True)
    assert res.request.method == "HEAD"
    assert res.status_code == 200


def test_options_with_session():
    session = objectrest.Session()
    res = objectrest.options(url=URL, session=session, log=True)
    assert res.request.method == "OPTIONS"
    assert res.status_code == 200
