import logging
from .logger import setup_logger
from .sessions import Sessions


class FlareSolverr:
    _url: str
    _logger: logging.Logger

    sessions: Sessions

    def __init__(self, url: str, log_level: str = "CRITICAL"):
        if not url.endswith("/v1"):
            url += "/v1"
        self._url = url
        setup_logger(log_level)
        self._logger = logging.getLogger("flaresolverr")
        self.sessions = Sessions(url)
