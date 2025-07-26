import requests

id_to_delete = 4  # যেটা ডিলিট করতে চাও
URL = f"http://127.0.0.1:8000/aiinfo/{id_to_delete}/"

r = requests.delete(url=URL)

print("Status Code:", r.status_code)
print("Raw Response:", r.text)

try:
    data = r.json()
    print("JSON Response:", data)
except requests.exceptions.JSONDecodeError:
    print("Response is not valid JSON or is empty.")
