import mysql.connector
from os import getenv
from dotenv import load_dotenv

load_dotenv(dotenv_path='../.env')

def ConnectorMysql():
    mydb = mysql.connector.connect(
            host=getenv("DB_HOST"),
            user=getenv("DB_USER"),
            passwd=getenv("DB_PASSWORD"),
            database=getenv("DB_DATABASE"),
            auth_plugin='mysql_native_password'
    )
    return mydb

def get_all():
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    sql = "SELECT * FROM users;"

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    mydb.close()

    return result

def get_user_by_id(id):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    sql = f"SELECT * FROM users WHERE uid='{id}';"

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    mydb.close()

    return result

def create_user(data : dict):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()

    columns = ', '.join(data.keys())
    values = ', '.join(f"'{value}'" 
                        if isinstance(value, str) else str(value)
                        for value in data.values()
                        )

    sql = f"INSERT INTO users ({columns}) VALUES ({values});"

    cursor.execute(sql)
    mydb.commit()

    cursor.close()
    mydb.close()

    return

def update_user(id,data : dict):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()

    updateData = ", ".join(f"{key} = '{value}'" 
                            if isinstance(value, str)
                            else f"{key} = {value}"
                            for key, value in data.items()
                            )

    sql = f"UPDATE users SET {updateData} WHERE uid='{id}';"

    cursor.execute(sql)
    mydb.commit()

    cursor.close()
    mydb.close()

    return

def delete_user(id):
    mydb = ConnectorMysql()
    cursor = mydb.cursor()
    sql = f"DELETE FROM users WHERE uid='{id}';"

    cursor.execute(sql)
    mydb.commit()

    cursor.close()
    mydb.close()

    return