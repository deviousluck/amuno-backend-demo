import urllib.request
import json
import time

url = "http://127.0.0.1:8000/api/v1/predict"
payload = {
    "field_id": "Field_A",
    "sample_values": [0.4, 0.6, 0.3]
}
data = json.dumps(payload).encode('utf-8')
headers = {
    "Content-Type": "application/json"
}

req = urllib.request.Request(url, data=data, headers=headers, method='POST')

print("Waiting for service to start...")
for i in range(10):
    try:
        with urllib.request.urlopen(req) as response:
            print(f"Status Code: {response.getcode()}")
            print(f"Response Body: {response.read().decode('utf-8')}")
            break
    except urllib.error.URLError as e:
        print(f"Attempt {i+1}: Service not ready yet ({e})")
        time.sleep(1)
    except Exception as e:
        print(f"Error: {e}")
        break
