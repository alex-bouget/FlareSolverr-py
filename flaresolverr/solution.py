from typing import Dict, List


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
