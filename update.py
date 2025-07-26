import requests
import json

URL = "http://127.0.0.1:8000/aicreate/"

data = {
    'id': 3,  # যেটা update করতে চাও, সেই object-এর ID
    'teacher_name': 'Tanha Sayed Ahona',
    'course_name': 'Data Science',
    'course_duration': '5',
    'seat': 40
}

headers = {'Content-Type': 'application/json'}

# PUT request পাঠানো হচ্ছে
r = requests.put(url=URL, data=json.dumps(data), headers=headers)

print("Status Code:", r.status_code)
print("Raw Response:", r.text)

try:
    response_data = r.json()
    print("JSON Response:", response_data)
except ValueError:
    print("Invalid JSON response from server.")
