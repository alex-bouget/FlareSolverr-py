from .flare_send import request_to_flare
from typing import List, Dict
from .solution import Solution
from urllib.parse import urlencode


class Request:
    _url: str

    def __init__(self, url: str):
        self._url = url

    def get(self, url: str, session: str | None = None,
            session_ttl_minutes: int | None = None,
            max_timeout: int | None = None,
            cookies: List[Dict[str, str]] | None = None,
            return_only_cookies: bool = False,
            proxy: str | None = None) -> Solution | bool:
        request_data = {
            "url": url
        }
        if session is not None:
            request_data["session"] = session
        if session_ttl_minutes is not None:
            request_data["session_ttl_minutes"] = session_ttl_minutes
        if max_timeout is not None:
            request_data["maxTimeout"] = max_timeout
        if cookies is not None:
            request_data["cookies"] = cookies
        if return_only_cookies:
            request_data["returnOnlyCookies"] = return_only_cookies
        if proxy is not None:
            request_data["proxy"] = {"url": proxy}
        data = request_to_flare(self._url, "request.get", **request_data)
        if data is False:
            return False
        return Solution(data["solution"])

    def post(self, url: str, post_data: Dict[str, str],
             session: str | None = None,
             session_ttl_minutes: int | None = None,
             max_timeout: int | None = None,
             cookies: List[Dict[str, str]] | None = None,
             return_only_cookies: bool = False,
             proxy: str | None = None) -> Solution | bool:
        request_data = {
            "url": url,
            "postData": urlencode(post_data)
        }
        if session is not None:
            request_data["session"] = session
        if session_ttl_minutes is not None:
            request_data["session_ttl_minutes"] = session_ttl_minutes
        if max_timeout is not None:
            request_data["maxTimeout"] = max_timeout
        if cookies is not None:
            request_data["cookies"] = cookies
        if return_only_cookies:
            request_data["returnOnlyCookies"] = return_only_cookies
        if proxy is not None:
            request_data["proxy"] = {"url": proxy}
        data = request_to_flare(self._url, "request.post", **request_data)
        if data is False:
            return False
        return Solution(data["solution"])
