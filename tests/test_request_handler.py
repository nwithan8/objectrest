import logging

import pytest

import objectrest

from tests.object import Object

URL = "https://httpbin.org/anything"
PARAMS = {"ping": "pong"}

HANDLER = objectrest.RequestHandler()


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    logging.basicConfig(level=logging.DEBUG)
    global HANDLER
    HANDLER = objectrest.RequestHandler(base_url=URL, universal_parameters=PARAMS, log_requests=True)


def test_get():
    res = HANDLER.get(url=URL)
    assert res.request.method == "GET"
    assert res.status_code == 200


def test_get_json():
    data = HANDLER.get_json(url=URL)
    assert data["method"] == "GET"


def test_get_object():
    obj = HANDLER.get_object(url=URL, model=Object)
    assert type(obj) == Object
    assert obj.method == "GET"
    assert obj.args == PARAMS


def test_options():
    res = HANDLER.options(url=URL)
    assert res.request.method == "OPTIONS"
    assert res.status_code == 200


def test_head():
    res = HANDLER.head(url=URL)
    assert res.request.method == "HEAD"
    assert res.status_code == 200


def test_post():
    res = HANDLER.post(url=URL)
    assert res.request.method == "POST"
    assert res.status_code == 200


def test_post_json():
    data = HANDLER.post_json(url=URL)
    assert data["method"] == "POST"


def test_post_object():
    obj = HANDLER.post_object(url=URL, model=Object)
    assert type(obj) == Object
    assert obj.method == "POST"
    assert obj.args == PARAMS


def test_put():
    res = HANDLER.put(url=URL)
    assert res.request.method == "PUT"
    assert res.status_code == 200


def test_put_json():
    data = HANDLER.put_json(url=URL)
    assert data["method"] == "PUT"


def test_put_object():
    obj = HANDLER.put_object(url=URL, model=Object)
    assert type(obj) == Object
    assert obj.method == "PUT"
    assert obj.args == PARAMS


def test_patch():
    res = HANDLER.patch(url=URL)
    assert res.request.method == "PATCH"
    assert res.status_code == 200


def test_patch_json():
    data = HANDLER.patch_json(url=URL)
    assert data["method"] == "PATCH"


def test_patch_object():
    obj = HANDLER.patch_object(url=URL, model=Object)
    assert type(obj) == Object
    assert obj.method == "PATCH"
    assert obj.args == PARAMS


def test_delete():
    res = HANDLER.delete(url=URL)
    assert res.request.method == "DELETE"
    assert res.status_code == 200


def test_delete_json():
    data = HANDLER.delete_json(url=URL)
    assert data["method"] == "DELETE"


def test_delete_object():
    obj = HANDLER.delete_object(url=URL, model=Object)
    assert type(obj) == Object
    assert obj.method == "DELETE"
    assert obj.args == PARAMS
