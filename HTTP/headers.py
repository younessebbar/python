import requests

url = "https://icanhazdadjoke.com/"
response = requests.get(url, headers={"accept": "application/json"})

data = response.json()
# print(type(response.text))
print(f"status: {data["status"]}")
print(f"joke: {data["joke"]}")
