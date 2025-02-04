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
    try:
        mydb = ConnectorMysql()
        cursor = mydb.cursor()
        sql = "SELECT * FROM users;"

        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()
        mydb.close()

        status_code = 200
        newdata = []
        for i in data:
            newdata.append({
                "id": i[0],
                "name": i[1],
                "age": i[2]
            })
        result = {
            "status": "Success",
            "result": newdata
        }
    except:
        status_code = 500
        result = {
            "status": "Internal error",
            "result": ""
        }

    return status_code,result

def get_user_by_id(id):
    try:
        mydb = ConnectorMysql()
        cursor = mydb.cursor()
        sql = f"SELECT * FROM users WHERE uid='{id}';"

        cursor.execute(sql)
        data = cursor.fetchall()

        cursor.close()
        mydb.close()

        status_code = 200

        print(len(data))

        if len(data) == 1:
            result = {
                "status": "Success",
                "result": {
                    "id": data[0][0],
                    "name": data[0][1],
                    "age": data[0][2]
                }
            } 
        elif len(data) == 0:
            status_code = 404
            result = {
            "status": "Not Found",
            "result": ""
            }
        else:
            raise Exception("Number of ID is wrong")
         
    except:
        status_code = 500
        result = {
            "status": "Internal error",
            "result": ""
        }
    return status_code,result


def create_user(data : dict):
    try:
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
    
        status_code = 201
        result = {
            "status": "Success",
        }
    except:
        status_code = 500
        result = {
            "status": "Internal error",
        }
    return status_code,result

def update_user(id,data : dict):
    try:
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

        status_code = 200
        result = {
            "status": "Success",
        }
    except:
        status_code = 500
        result = {
            "status": "Internal error",
        }
    return status_code,result

def delete_user(id):
    try:
        mydb = ConnectorMysql()
        cursor = mydb.cursor()
        sql = f"DELETE FROM users WHERE uid='{id}';"

        cursor.execute(sql)
        mydb.commit()

        cursor.close()
        mydb.close()

        status_code = 200
        result = {
            "status": "Success",
        }
    except:
        status_code = 500
        result = {
            "status": "Internal error",
        }
    return status_code,result
