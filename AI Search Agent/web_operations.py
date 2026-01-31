from dotenv import load_dotenv
import os
import requests
from urllib.parse import quote_plus
from snapshot_operations import download_snapshot, poll_snapshot_status


load_dotenv()

dataset_id = "gd_lvz8ah06191smkebj4"
