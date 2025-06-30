import requests
import json
import mysql.connector

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data from the API")
        return None

def call_stored_procedure(json_data):
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="mfcentral",
            port= 3307
        )
        cursor = conn.cursor()

        cursor.callproc("usp_schemeInsert", [json.dumps(json_data)])
        
        conn.commit()
        print("Data inserted successfully using stored procedure")
    except Exception as e:
        print("Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    api_url = "https://api.mfapi.in/mf"
    data = fetch_data_from_api(api_url)
    if data:
        call_stored_procedure(data)
