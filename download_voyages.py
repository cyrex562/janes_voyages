from pathlib import Path
import sys
import time
import requests
import argparse
import json


#  curl -X 'GET' \
#   'https://voyages-api-staging.crc.rice.edu/voyage/1' \
#   -H 'accept: application/json' \
#   -H 'Authorization: Basic amhvb3BlcjNAZ211LmVkdTpoMnlFcDNhanc2Wk4rTzlHdzJvTks='

DATA_PATH = Path("data")
URL = "https://voyages-api-staging.crc.rice.edu/voyage/"
ID_START = 1
ID_END = 1000
SLEEP_TIME = 0.5


def run() -> int:
    if not DATA_PATH.exists():
        DATA_PATH.mkdir()
    parser = argparse.ArgumentParser(description="Download voyages")
    parser.add_argument(
        "--start", type=int, default=ID_START, help="The voyage ID to start at"
    )
    parser.add_argument(
        "--end", type=int, default=ID_END, help="The voyage ID to end at"
    )
    args = parser.parse_args()
    id = args.start
    end = args.end
    while id < end:
        url = URL + str(id)
        print(f"Downloading voyage {id}...")
        response = requests.get(
            url,
            headers={
                "accept": "application/json",
                "Authorization": "Basic amhvb3BlcjNAZ211LmVkdTpoMnlFcDNhanc2Wk4rTzlHdzJvTks=",
            },
        )
        if response.status_code == 200:
            data = response.json()
            data = json.dumps(data, indent=2)
            file_path = DATA_PATH / f"{id}.json"
            print(f"Writing to {file_path}")
            with open(file_path, "w") as file:
                file.write(data)
        else:
            print(f"Failed to download voyage {id}: {response.status_code}")
        id += 1
        time.sleep(SLEEP_TIME)

    return 0


if __name__ == "__main__":
    rc = run()
    sys.exit(rc)
