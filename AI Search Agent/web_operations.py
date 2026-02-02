from dotenv import load_dotenv
import os
import requests
from urllib.parse import quote_plus
from snapshot_operations import download_snapshot, poll_snapshot_status


load_dotenv()

dataset_id = "gd_lvz8ah06191smkebj4"

def _make_api_requests(url, **kwargs):
    api_key = os.getenv("BRIGHTDATA_API_KEY")


    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(url, headers=headers, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API reuquest failed: {e}")
        return None
    except Exception as e:
        print (f"Unknown error: {e}")
        return None
    
def serp_search(query, engine="google"):
    if engine == "google":
        base_url = "https://www.google.com/search"
    elif engine == "bing":
        base_url == "https://www.bing.com/search"
    else
        raise ValueError

