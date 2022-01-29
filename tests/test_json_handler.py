import logging

import pytest

import objectrest

URL = "https://httpbin.org/anything"


@pytest.fixture(scope="session", autouse=True)
def execute_before_any_test():
    logging.basicConfig(level=logging.DEBUG)


def test_get_json():
    data = objectrest.get_json(url=URL, log=True)
    assert data["method"] == "GET"


def test_post_json():
    data = objectrest.post_json(url=URL, log=True)
    assert data["method"] == "POST"


def test_put_json():
    data = objectrest.put_json(url=URL, log=True)
    assert data["method"] == "PUT"


def test_patch_json():
    data = objectrest.patch_json(url=URL, log=True)
    assert data["method"] == "PATCH"


def test_delete_json():
    data = objectrest.delete_json(url=URL, log=True)
    assert data["method"] == "DELETE"
