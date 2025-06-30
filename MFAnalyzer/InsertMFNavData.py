import requests
import mysql.connector

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

        cursor.callproc("usp_getSchemeData")
        
        # Fetch all rows from the result set
        result_set = cursor.fetchall()
        
        return result_set
        
    except Exception as e:
        print("Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
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
    scheme_data = fetch_data_from_mysql_stored_proc()
    if scheme_data:
        for row in scheme_data:
            scheme_code = row[0]  # Assuming the first column contains the schemeCode
            call_api_and_insert_data(scheme_code)
