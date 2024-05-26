from _typeshed import Incomplete
from typing import Any

from hvac.adapters import Adapter

has_hcl_parser: bool

class Client:
    def __init__(
        self,
        url: str | None = None,
        token: str | None = None,
        cert: tuple[str, str] | None = None,
        verify: bool | str | None = None,
        timeout: int = 30,
        proxies: dict[str, str] | None = None,
        allow_redirects: bool = True,
        session: Incomplete | None = None,
        adapter: type[Adapter[Any]] = ...,
        namespace: Incomplete | None = None,
        **kwargs: Any,
    ) -> None: ...
    def __getattr__(self, name: str) -> Any: ...
    @property
    def adapter(self) -> Adapter[Any]: ...
    @adapter.setter
    def adapter(self, adapter: Adapter[Any]) -> None: ...
    @property
    def url(self) -> str: ...
    @url.setter
    def url(self, url: str) -> None: ...
    @property
    def token(self) -> str: ...
    @token.setter
    def token(self, token: str) -> None: ...
    @property
    def session(self): ...
    @session.setter
    def session(self, session) -> None: ...
    @property
    def allow_redirects(self) -> bool: ...
    @allow_redirects.setter
    def allow_redirects(self, allow_redirects: bool) -> None: ...
    @property
    def auth(self): ...
    @property
    def secrets(self): ...
    @property
    def sys(self): ...
    @property
    def generate_root_status(self): ...
    @property
    def key_status(self): ...
    @property
    def rekey_status(self): ...
    @property
    def ha_status(self): ...
    @property
    def seal_status(self): ...
    def read(self, path: str, wrap_ttl: int | str | None = None): ...
    def list(self, path: str): ...
    def write(self, path: str, wrap_ttl: int | str | None, **kwargs: Any): ...
    def write_data(self, path: str, *, data: dict[str, Any] | None = None, wrap_ttl: int | str | None = None): ...
    def delete(self, path: str) -> None: ...
    def get_policy(self, name: str, parse: bool = False): ...
    def lookup_token(self, token: str | None = None, accessor: bool = False, wrap_ttl: int | str | None = None): ...
    def revoke_token(self, token: str, orphan: bool = False, accessor: bool = False) -> None: ...
    def renew_token(self, token: str, increment: bool | None = None, wrap_ttl: int | str | None = None): ...
    def logout(self, revoke_token: bool = False) -> None: ...
    def is_authenticated(self) -> bool: ...
    def auth_cubbyhole(self, token: str): ...
    def login(self, url: str, use_token: bool = True, **kwargs: Any): ...
