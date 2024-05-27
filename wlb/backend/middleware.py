from typing import Any

class RequestMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass