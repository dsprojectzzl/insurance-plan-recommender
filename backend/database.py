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


def get_all_plans_with_recommendation(recommend_uid):
    """
    Fetch all insurance plans from the database and mark the recommended plan.
    :param recommend_uid: Plan UID to be marked as recommended
    :return: List of all plans with a recommendation flag
    """
    conn = get_database_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM InsurancePlans"
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    if rows:
        columns = [column[0] for column in cursor.description]

        plans = []
        for row in rows:
            plan = dict(zip(columns, row))
            plan["is_recommended"] = (plan["UID"] == recommend_uid)
            plans.append(plan)

        return plans

    return {"error": "No plans found"}


