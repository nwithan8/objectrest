from typing import List, Union

from objectrest.json_handler import *


def _create_object(json_data: dict, model: type, sub_keys: List = None, extract_list: bool = False) -> Union[object, None]:
    """
    Parse JSON data into a Pydantic model

    :param json_data:
    :type json_data:
    :param model:
    :type model:
    :param sub_keys:
    :type sub_keys:
    :param extract_list: If top-level of JSON is a list, whether to convert each list item into model, or treat entire JSON as a whole object
    :type extract_list: bool
    :return:
    :rtype:
    """
    if sub_keys:
        for key in sub_keys:
            json_data = json_data.get(key, {})

    if not json_data:
        return None

    try:
        if type(json_data) == list and extract_list:
            return [model(**item) for item in json_data]
        else:
            return model(**json_data)
    except:
        return None


def get_object(url: str, model: type, sub_keys: List = None, extract_list: bool = False, session: requests.Session = None, **kwargs) -> Union[object, None]:
    """
    Parse the JSON data from a GET request into an object

    :param url: URL endpoint to append to base URL
    :type url: str
    :param model: a Pydantic model to generate from the response JSON data
    :type model: type
    :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
    :type sub_keys: list, optional
    :param extract_list: If top-level of JSON is a list, whether to convert each list item into model, or treat entire JSON as a whole object
    :type extract_list: bool
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: an object
    :rtype: object
    """
    json_data = get_json(url=url, session=session, **kwargs)
    return _create_object(json_data=json_data, model=model, sub_keys=sub_keys, extract_list=extract_list)


def post_object(url: str, model: type, sub_keys: List = None, extract_list: bool = False, session: requests.Session = None, **kwargs) -> Union[object, None]:
    """
    Parse the JSON data from a POST request into an object

    :param url: URL endpoint to append to base URL
    :type url: str
    :param model: a Pydantic model to generate from the response JSON data
    :type model: type
    :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
    :type sub_keys: list, optional
    :param extract_list: If top-level of JSON is a list, whether to convert each list item into model, or treat entire JSON as a whole object
    :type extract_list: bool
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: an object
    :rtype: object
    """
    json_data = post_json(url=url, session=session, **kwargs)
    return _create_object(json_data=json_data, model=model, sub_keys=sub_keys, extract_list=extract_list)


def put_object(url: str, model: type, sub_keys: List = None, extract_list: bool = False, session: requests.Session = None, **kwargs) -> Union[object, None]:
    """
    Parse the JSON data from a PUT request into an object

    :param url: URL endpoint to append to base URL
    :type url: str
    :param model: a Pydantic model to generate from the response JSON data
    :type model: type
    :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
    :type sub_keys: list, optional
    :param extract_list: If top-level of JSON is a list, whether to convert each list item into model, or treat entire JSON as a whole object
    :type extract_list: bool
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: an object
    :rtype: object
    """
    json_data = put_json(url=url, session=session, **kwargs)
    return _create_object(json_data=json_data, model=model, sub_keys=sub_keys, extract_list=extract_list)


def patch_object(url: str, model: type, sub_keys: List = None, extract_list: bool = False, session: requests.Session = None, **kwargs) -> Union[object, None]:
    """
    Parse the JSON data from a PATCH request into an object

    :param url: URL endpoint to append to base URL
    :type url: str
    :param model: a Pydantic model to generate from the response JSON data
    :type model: type
    :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
    :type sub_keys: list, optional
    :param extract_list: If top-level of JSON is a list, whether to convert each list item into model, or treat entire JSON as a whole object
    :type extract_list: bool
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: an object
    :rtype: object
    """
    json_data = patch_json(url=url, session=session, **kwargs)
    return _create_object(json_data=json_data, model=model, sub_keys=sub_keys, extract_list=extract_list)


def delete_object(url: str, model: type, sub_keys: List = None, extract_list: bool = False, session: requests.Session = None, **kwargs) -> Union[object, None]:
    """
    Parse the JSON data from a DELETE request into an object

    :param url: URL endpoint to append to base URL
    :type url: str
    :param model: a Pydantic model to generate from the response JSON data
    :type model: type
    :param sub_keys: A list of sub-keys to search for (in order) to find JSON data for model.
    :type sub_keys: list, optional
    :param extract_list: If top-level of JSON is a list, whether to convert each list item into model, or treat entire JSON as a whole object
    :type extract_list: bool
    :param session: a requests.Session to use for the API call (optional)
    :type session: requests.Session, optional
    :param kwargs: Keyword arguments to pass to Requests library
    :type kwargs: dict, optional
    :return: an object
    :rtype: object
    """
    json_data = delete_json(url=url, session=session, **kwargs)
    return _create_object(json_data=json_data, model=model, sub_keys=sub_keys, extract_list=extract_list)
