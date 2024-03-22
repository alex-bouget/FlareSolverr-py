from requests import post
import logging


def request_to_flare(url: str, cmd: str, **kwargs) -> dict | bool:
    """Send a request to the flare server."""
    headers = {"Content-Type": "application/json"}
    data = {"cmd": cmd, **kwargs}
    logger = logging.getLogger("flaresolverr")
    logger.info(f"request {cmd}")
    logger.debug(f"Request to flare: {data}")
    result = post(url, headers=headers, json=data).json()
    if result["message"]:
        if result["status"] == "ok":
            logger.info(result["message"])
        else:
            logger.error(result["message"])
    logger.debug(f"Response from flare: {result}")
    return result
