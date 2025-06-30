# write a asyncronous api call from 5 api code in python 

import requests 

async def call_api_and_insert_data(scheme_code):
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
