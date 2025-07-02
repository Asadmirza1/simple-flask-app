import mysql.connector
import os

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get("mysql.railway.internal"),
        user=os.environ.get("root"),
        password=os.environ.get("FYWQTURfpVkVfWBfgWIydXmylFCdgqIb"),
        database=os.environ.get("railway"),
        port=int(os.environ.get("MYSQLPORT", 3306))
    )
