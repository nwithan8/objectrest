import time
from typing import List, Union

import sslproxies


def timestamp_is_expired(timestamp: str) -> bool:
    try:
        timestamp = int(timestamp)
        current_timestamp = int(time.time())
        return timestamp < current_timestamp
    except:
        raise Exception("Could not check timestamp expiration.")


def get_proxy_dict(anonymous: bool = False, countries: List[str] = None) -> Union[dict, None]:
    proxy = sslproxies.get_proxy(countries=countries, anonymous=anonymous, verify=True)
    if proxy:
        return proxy.requests_dict
    return {}
