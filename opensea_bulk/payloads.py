from __future__ import annotations

import json
from typing import Dict, Any, Union, TYPE_CHECKING

from .utils import upload_query, commit_query

if TYPE_CHECKING:
    Json = Dict[str, Any]
    Files = Dict[str, Tuple(Union[str, None], Any)]


class Payloads:
    def __init__(self, waddress: str):
        self.waddress = waddress

    def upload_nft(
        self,
        filepath: str,
        name: str,
        description: str = None,
        collection: str = None,
        nsfw: bool = False,
    ) -> Files:
        p_operations = {
            "query": upload_query,
            "variables": {
                "assetContract": None,
                "collection": collection,
                "description": description,
                "externalLink": None,
                "identity": {"address": self.waddress},
                "imageFile": None,
                "maxSupply": "1",
                "mediaFile": None,
                "name": name,
                "tokenId": None,
                "chain": "MATIC",
                "unlockableContent": "",
                "isNsfw": nsfw,
                "properties": [],
                "levels": [],
                "stats": [],
            },
        }
        fbytes = open(filepath, "rb").read()
        fname = filepath.split("/")[-1]
        ftype = fname.split(".")[-1]
        p_map = {"1": ["variables.imageFile"]}

        return {
            "operations": (None, json.dumps(p_operations)),
            "map": (None, json.dumps(p_map)),
            "1": (fname, fbytes, f"image/{ftype}"),
        }
