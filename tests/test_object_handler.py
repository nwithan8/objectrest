import logging

import pytest

import objectrest
from tests.object import Object

URL = "https://httpbin.org/anything"


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    logging.basicConfig(level=logging.DEBUG)


def test_get_object():
    obj = objectrest.get_object(url=URL, model=Object)
    assert type(obj) == Object
    assert obj.method == "GET"
    assert obj.url == URL


def test_post_object():
    obj = objectrest.post_object(url=URL, model=Object)
    assert type(obj) == Object
    assert obj.method == "POST"
    assert obj.url == URL


def test_put_object():
    obj = objectrest.put_object(url=URL, model=Object)
    assert type(obj) == Object
    assert obj.method == "PUT"
    assert obj.url == URL


def test_patch_object():
    obj = objectrest.patch_object(url=URL, model=Object)
    assert type(obj) == Object
    assert obj.method == "PATCH"
    assert obj.url == URL


def test_delete_object():
    obj = objectrest.delete_object(url=URL, model=Object)
    assert type(obj) == Object
    assert obj.method == "DELETE"
    assert obj.url == URL
