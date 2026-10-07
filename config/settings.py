"""
Configuration settings loaded from environment variables.
"""

import os

from dotenv import load_dotenv


load_dotenv()

BASE_URL = os.getenv("BASE_URL")
BASE_API_URL = os.getenv("BASE_API_URL")
USER_ID = os.getenv("USER_ID")