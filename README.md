# opensea_bulk
Quick opensea bulk upload script

# Usage
```python
import os
import time
from dotenv import load_dotenv

load_dotenv()

AUTHENTICATION = {
    "x_api_key": os.getenv("x_api_key"),
    "x_build_id": os.getenv("x_build_id"),
    "x_viewer_address": os.getenv("x_viewer_address"),
    "authorization_jwt": os.getenv("authorization_jwt"),
    "x_signed_query": os.getenv("x_signed_query"),
}


if __name__ == "__main__":
    folder = input("Folder with files: ")
    opensea = Opensea(AUTHENTICATION)
    for filename in os.listdir(folder):
        r = opensea.create_nft(
            f"{folder}/{filename}",
            f"{filename}",
            "<Some description>",
            "<some collection> (optional)",
        )
        time.sleep(15) # Rate limit
```
