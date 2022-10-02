import time
from typing import List, Optional, Union

import proxlist


def timestamp_is_expired(timestamp: str) -> bool:
    try:
        timestamp: int = int(timestamp)
        current_timestamp: int = int(time.time())
        return timestamp < current_timestamp
    except:
        raise Exception("Could not check timestamp expiration.")


def get_proxy_dict(
        country: Optional[str] = None, verified: bool = True
) -> Union[dict, None]:
    proxy: Union[str, None] = proxlist.random_proxy(country=country, google_verified=verified)
    if proxy:
        return {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        }
    return {}
