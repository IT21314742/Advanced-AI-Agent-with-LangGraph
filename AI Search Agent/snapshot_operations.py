import os
import time
import requests
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional


load_dotenv()


def poll_snapshot_status(
       snapshot_id: str, 
)