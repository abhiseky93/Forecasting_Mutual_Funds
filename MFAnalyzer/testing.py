import requests
import concurrent.futures

URL = "https://ckra.cvlindia.com"  # Replace with the URL you want to send requests to

def send_request(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Request to {url} successful")
        else:
            print(f"Request to {url} failed. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending request to {url}: {e}")

# Number of requests to send concurrently
NUM_REQUESTS = 1000

# Create a ThreadPoolExecutor with max_workers set to the number of requests
with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_REQUESTS) as executor:
    # Submit NUM_REQUESTS tasks to the executor
    # Each task will send a request to the URL
    futures = [executor.submit(send_request, URL) for _ in range(NUM_REQUESTS)]

    # Wait for all tasks to complete
    concurrent.futures.wait(futures)

print("All requests completed.")
