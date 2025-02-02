from abc import ABC, abstractmethod


class AccessJWTTokenRequestHandler(ABC):
    @abstractmethod
    def get_access_token_from_request(self) -> str | None: ...
