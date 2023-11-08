import requests

# Replace this with your actual base URL
base_url = "http://localhost"

# Read endpoints from a 'list.txt' file
with open('list.txt', 'r') as file:
    endpoints = [line.strip() for line in file]

# Send GET request
for endpoint in endpoints:
    get_url = base_url + endpoint
    response = requests.get(get_url)
    print(f"GET {get_url} - Status Code: {response.status_code}")

# Send POST request
for endpoint in endpoints:
    post_url = base_url + endpoint
    response = requests.post(post_url, data={'key': 'value'})
    print(f"POST {post_url} - Status Code: {response.status_code}")

# Send HEAD request
for endpoint in endpoints:
    head_url = base_url + endpoint
    response = requests.head(head_url)
    print(f"HEAD {head_url} - Status Code: {response.status_code}")

# Send OPTIONS request
for endpoint in endpoints:
    options_url = base_url + endpoint
    response = requests.options(options_url)
    print(f"OPTIONS {options_url} - Status Code: {response.status_code}")
