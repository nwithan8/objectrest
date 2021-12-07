import time
import proxlist


def timestamp_is_expired(timestamp: str) -> bool:
    try:
        timestamp = int(timestamp)
        current_timestamp = int(time.time())
        return timestamp < current_timestamp
    except:
        raise Exception("Could not check timestamp expiration.")


def get_proxy_dict() -> dict:
    proxy = proxlist.random_proxy()
    return {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}',
    }
