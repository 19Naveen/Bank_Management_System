import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="C:\\Users\\Naveen\\Desktop\\DS_Project\\Banking_Managment\\.env")

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": "bank_db",
}