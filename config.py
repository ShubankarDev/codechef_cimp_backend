'''this config.py is used to load the cimp_portal MySQL database with its credentials
in .env file which isn't added to the github repo (refer to .gitignore)
'''
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}
