from .flare_send import request_to_flare


class Sessions:
    _url: str

    def __init__(self, url: str):
        self._url = url

    def create(self, session: str | None = None, proxy: str | None = None,
               proxy_username: str | None = None,
               proxy_password: str | None = None) -> str | bool:
        """This will launch a new browser instance which will retain cookies
        until you destroy it with sessions.destroy. This comes in handy,
        so you don't have to keep solving challenges over and over and
        you won't need to keep sending cookies for the browser to use.
        This also speeds up the requests since it won't have to launch
        a new browser instance for every request"""
        data = {}
        if session:
            data["session"] = session
        if proxy:
            data["proxy"] = {"proxy": proxy}
            if proxy_username:
                data["proxy"]["username"] = proxy_username
            if proxy_password:
                data["proxy"]["password"] = proxy_password
        result = request_to_flare(self._url, "sessions.create", **data)
        if result["status"] == "ok":
            return result["session"]
        return False

    def list(self) -> dict:
        """Returns a list of all the active sessions. More for debugging
        if you are curious to see how many sessions are running. You should
        always make sure to properly close each session when you are done
        using them as too many may slow your computer down."""
        return request_to_flare(self._url, "sessions.list")["sessions"]

    def destroy(self, session: str) -> bool:
        """This will properly shutdown a browser instance and remove all files
        associated with it to free up resources for a new session. When you no
        longer need to use a session you should make sure to close it."""
        result = request_to_flare(self._url, "sessions.destroy",
                                  session=session)
        return result["status"] == "ok"
