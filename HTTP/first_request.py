import requests
try:
    url = "http://www.google.com"
    response = requests.get(url)
except:
    print("Error was encoutered during the request")
else:
    print(f"your request to {url} came back w/ {response.status_code} status code")
