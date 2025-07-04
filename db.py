import mysql.connector
from config import DB_CONFIG
#config.py contains info related to db connection

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

# ** to unpack all keyword arguments of the DB_CONFIG dictionary 