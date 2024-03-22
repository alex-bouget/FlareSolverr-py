from requests import post
import logging


def request_to_flare(_url: str, _cmd: str, **kwargs) -> dict | bool:
    """Send a request to the flare server."""
    headers = {"Content-Type": "application/json"}
    data = {"cmd": _cmd, **kwargs}
    logger = logging.getLogger("flaresolverr")
    logger.info(f"request {_cmd}")
    logger.debug(f"Request to flare: {data}")
    result = post(_url, headers=headers, json=data).json()
    if result["message"]:
        if result["status"] == "ok":
            logger.info(result["message"])
        else:
            logger.error(result["message"])
            return False
    logger.debug(f"Response from flare: {result}")
    return result
