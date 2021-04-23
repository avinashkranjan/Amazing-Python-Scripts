import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path('./credential_variables.env')
load_dotenv(dotenv_path=dotenv_path)

# candidate for Twitter Api
candidate_key = os.getenv("candidate_key")
candidate_sec = os.getenv("candidate_sec")
access_key = os.getenv("access_key")
access_sec = os.getenv("access_sec")
