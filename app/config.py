import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
CLOUD_SQL_PUBLIC_IP_ADDRESS = os.environ['CLOUD_SQL_PUBLIC_IP_ADDRESS']
DB_NAME = os.environ['DB_NAME']