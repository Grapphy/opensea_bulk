import requests
from opensea_bulk.headers import Headers, AuthenticationValues
from opensea_bulk.payloads import Payloads


class Opensea(requests.Session):
    def __init__(self, auth_data: AuthenticationValues):
        super().__init__()
        self.h_suit = Headers(auth_data)
        self.p_suit = Payloads(auth_data.get("x_viewer_address"))

    def create_nft(
        self,
        filepath: str,
        name: str,
        description: str = None,
        collection: str = None,
        nsfw: bool = False,
    ) -> str:
        """
        Timeout: 15 seconds per request
        """

        self.headers = self.h_suit.post_graphql_headers()
        nft_p = self.p_suit.upload_nft(
            filepath,
            name,
            description=description,
            collection=collection,
            nsfw=nsfw,
        )

        with self.post("https://api.opensea.io/graphql/", files=nft_p) as r:
            r_json = r.json()

            if "errors" in r:
                raise Exception(r.text)

            return r_json["data"]["assets"]["create"]["tokenId"]
