import pyodbc
import os

def get_database_connection():
    conn = pyodbc.connect(
        f"DRIVER={os.getenv('DB_DRIVER')};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_NAME')};"
        f"UID={os.getenv('DB_USER')};"
        f"PWD={os.getenv('DB_PASSWORD')};"
        f"Authentication={os.getenv('DB_AUTHENTICATION')};"
    )
    conn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
    conn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
    conn.setencoding(encoding='utf-8')
    return conn


def get_plan_by_uid(uid):
    """
    Fetch insurance plan details from the database by UID.
    :param uid: Plan UID
    :return: Plan details as a dictionary or an error message
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM InsurancePlans WHERE UID = ?"
    cursor.execute(query, uid)
    row = cursor.fetchone()
    conn.close()

    if row:
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, row))

    return {"error": "Plan not found"}

