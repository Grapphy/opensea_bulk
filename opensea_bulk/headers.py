from __future__ import annotations

from typing import TypedDict
from collections import OrderedDict


DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) "
    "Gecko/20100101 Firefox/94.0"
)


class AuthenticationValues(TypedDict):
    x_api_key: str
    x_build_id: str
    x_viewer_address: str
    authorization_jwt: str
    x_signed_query: str


class Headers:
    __slots__ = (
        "x_api_key",
        "x_build_id",
        "x_viewer_address",
        "authorization_jwt",
        "x_signed_query",
    )

    def __init__(self, auth_values: AuthenticationValues) -> None:
        self._update(auth_values)

    def _update(self, auth_values: AuthenticationValues) -> None:
        self.x_api_key = auth_values.get("x_api_key")
        self.x_build_id = auth_values.get("x_build_id")
        self.x_viewer_address = auth_values.get("x_viewer_address")
        self.authorization_jwt = auth_values.get("authorization_jwt")
        self.x_signed_query = auth_values.get("x_signed_query")

    def post_graphql_headers(self) -> OrderedDict:
        return OrderedDict(
            (
                ("Host", "api.opensea.io"),
                ("User-Agent", DEFAULT_UA),
                ("Accept", "*/*"),
                ("Accept-Language", "en-US,en;q=0.5"),
                ("Accept-Encoding", "gzip, deflate"),
                ("Referer", "https://opensea.io/"),
                ("X-Api-Key", self.x_api_key),
                ("X-Build-Id", self.x_build_id),
                ("X-Viewer-Address", self.x_viewer_address),
                ("Authorization", self.authorization_jwt),
                ("X-Signed-Query", self.x_signed_query),
                ("Origin", "https://opensea.io"),
            )
        )
