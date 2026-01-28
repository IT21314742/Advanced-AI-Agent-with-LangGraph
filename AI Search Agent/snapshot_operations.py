import os
import time
import requests
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional


load_dotenv()


def poll_snapshot_status(
       snapshot_id: str, max_attempts: int = 60, delay: int = 5
) -> bool:
    api_key = os.getenv("BRIGHTDATA_API_KEY")
    progress_url = 