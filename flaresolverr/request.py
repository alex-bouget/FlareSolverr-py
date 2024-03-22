from .flare_send import request_to_flare


class Request:
    _url: str

    def __init__(self, url: str):
        self._url = url
