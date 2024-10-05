import requests

url = "https://icanhazdadjoke.com/search"
query = input("what topic would you like the joke to be ?")
response = requests.get(url, headers={"accept": "application/json"}, params={"term": query, "limit": 1})

data = response.json()
print(data)
# print(response.text)
# print(f"status: {data["status"]}")
# print(f"joke: {data["joke"]}")
