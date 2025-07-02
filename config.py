import os

db_config = {
    'host': os.getenv("MYSQLHOST", "localhost"),
    'user': os.getenv("MYSQLUSER", "root"),
    'password': os.getenv("MYSQLPASSWORD", ""),
    'database': os.getenv("MYSQLDATABASE", "crud_db"),
    'port': int(os.getenv("MYSQLPORT", 3306))
}
