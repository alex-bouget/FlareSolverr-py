from typing import Dict, List
import regex as re
import json


class Cookie:
    name: str
    value: str
    domain: str
    path: str
    expires: float
    size: int
    http_only: bool
    secure: bool
    same_site: str

    def __init__(self, data: Dict[str, str]):
        self.name = data.get('name')
        self.value = data.get('value')
        self.domain = data.get('domain')
        self.path = data.get('path')
        self.expires = data.get('expires')
        self.secure = data.get('secure')
        self.htt_only = data.get('httpOnly')
        self.same_site = data.get('sameSite')

    def __str__(self):
        return f"{self.name}={self.value}"


class Solution:
    _data: dict

    url: str
    status: int
    user_agent: str
    cookies: List[Cookie]
    response: str
    headers: Dict[str, str]

    def __init__(self, data: dict):
        self._data = data
        self.user_agent = data.get('userAgent')
        self.cookies = [Cookie(cookie) for cookie in data.get('cookies', [])]
        self.response = data.get('response')
        self.headers = data.get('headers')
        self.url = data.get('url')
        self.status = data.get('status')

    def json(self) -> dict | bool:
        if self.headers.get('Content-Type') != 'application/json':
            return False
        data = self._get_json(self.response)
        if not self._is_json(data):
            return False
        return json.loads(data)

    def _is_json(self, data: str) -> bool:
        try:
            json.loads(data)
            return True
        except json.JSONDecodeError:
            return False

    def _get_json(self, data: str) -> str:
        in_dict = self._get_json_dict(data)
        in_list = self._get_json_list(data)
        if len(in_dict) > len(in_list):
            return in_dict
        return in_list

    def _get_json_list(self, data: str) -> str:
        test = re.search(r"(\[.*\])", data)
        if test:
            return test.group(1)
        return ""

    def _get_json_dict(self, data: str) -> str:
        test = re.search(r"(\{.*\})", data)
        if test:
            return test.group(1)
        return ""

    def __str__(self):
        message = f"URL: {self.url}\n"
        message += f"Status: {self.status}\n"
        message += f"User-Agent: {self.user_agent}\n"
        message += f"Cookies: {self.cookies}\n"
        message += f"Headers: {self.headers}\n"
        response = "".join(self.response.strip()[0:100])
        message += f"Response: {response}...\n"
        return message
