import os
from os import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

PATH_TO_TABLE = os.environ.get("PATH_TO_TABLE")
