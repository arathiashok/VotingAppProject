import mysql.connector
from typing import List, Dict
from src.config import db_config
def get_voter_details() -> List[Dict]:

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Users WHERE Role="Voter"')
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    return results



