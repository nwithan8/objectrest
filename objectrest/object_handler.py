import requests

from objectrest import json_handler


def _create_object(json_data: dict, model: type):
    """
    Parse JSON data into a Pydantic model

    :param json_data:
    :type json_data:
    :param model:
    :type model:
    :return:
    :rtype:
    """
    if not json_data:
        return None

    try:
        return model(**json_data)
    except:
        return None


def get_object(url: str, model: type, session: requests.Session = None, **kwargs):
    """
    Parse the JSON data from a GET request into an object

    :param url: URL endpoint to append to base URL
    :type url: str
    :param model: a Pydantic model to generate from the response JSON data
    :type model: type
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict
    :return: an object
    :rtype: object
    """
    json_data = json_handler.get_json(url=url, session=session, **kwargs)
    return _create_object(json_data=json_data, model=model)


def post_object(url: str, model: type, session: requests.Session = None, **kwargs):
    """
    Parse the JSON data from a POST request into an object

    :param url: URL endpoint to append to base URL
    :type url: str
    :param model: a Pydantic model to generate from the response JSON data
    :type model: type
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict
    :return: an object
    :rtype: object
    """
    json_data = json_handler.post_json(url=url, session=session, **kwargs)
    return _create_object(json_data=json_data, model=model)


def put_object(url: str, model: type, session: requests.Session = None, **kwargs):
    """
    Parse the JSON data from a PUT request into an object

    :param url: URL endpoint to append to base URL
    :type url: str
    :param model: a Pydantic model to generate from the response JSON data
    :type model: type
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict
    :return: an object
    :rtype: object
    """
    json_data = json_handler.put_json(url=url, session=session, **kwargs)
    return _create_object(json_data=json_data, model=model)


def patch_object(url: str, model: type, session: requests.Session = None, **kwargs):
    """
    Parse the JSON data from a PATCH request into an object

    :param url: URL endpoint to append to base URL
    :type url: str
    :param model: a Pydantic model to generate from the response JSON data
    :type model: type
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict
    :return: an object
    :rtype: object
    """
    json_data = json_handler.patch_json(url=url, session=session, **kwargs)
    return _create_object(json_data=json_data, model=model)


def delete_object(url: str, model: type, session: requests.Session = None, **kwargs):
    """
    Parse the JSON data from a DELETE request into an object

    :param url: URL endpoint to append to base URL
    :type url: str
    :param model: a Pydantic model to generate from the response JSON data
    :type model: type
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict
    :return: an object
    :rtype: object
    """
    json_data = json_handler.delete_json(url=url, session=session, **kwargs)
    return _create_object(json_data=json_data, model=model)
