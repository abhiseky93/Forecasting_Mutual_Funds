import json
import mysql.connector
import requests

def fetch_data_from_mysql_stored_proc():
    try:
        conn = mysql.connector.connect(
             host="127.0.0.1",
            user="root",
            password="root",
            database="mfcentral",
            port= 3307
        )
        cursor = conn.cursor()

        cursor.callproc("usp_getSchemeData5")
        
        # Fetch all rows from the result set
        for result in cursor.stored_results():
            result_set = result.fetchall()
            for row in result_set:
                scheme_code = row[1]
                call_api_and_insert_data(scheme_code)
                # Process each row here
                print(row)  # Example: Print each row
        cursor.close()
        
    except mysql.connector.Error as err:
        print("MySQL Error:", err)
    except Exception as e:
        print("Error:", e)
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

def call_api_and_insert_data(scheme_code):
    try:
        api_url = f"https://api.mfapi.in/mf/{scheme_code}"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            mf_data = response.json()
            insert_data_into_mysql_stored_proc(mf_data)
        else:
            print(f"Failed to fetch data from the API for scheme code: {scheme_code}")
    except Exception as e:
        print("Error:", e)

def insert_data_into_mysql_stored_proc(json_data):
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="mfcentral",
            port= 3307
        )
        cursor = conn.cursor()

        cursor.callproc("usp_InsertMFJsonData", [json.dumps(json_data)])
        
        conn.commit()
        print("Data inserted successfully using stored procedure usp_InsertMFJsonData")
    except Exception as e:
        print("Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == "__main__":
    fetch_data_from_mysql_stored_proc()
