from pyfiglet import figlet_format
from termcolor import colored
from random import choice
import requests

print(colored(figlet_format("Dad Joke 3000"), color="magenta"))

url = "https://icanhazdadjoke.com/search"
keyword = input("Let me tell you a joke, give me a topic: ")
response = requests.get(url, headers={"accept": "application/json"}, params={"term": keyword}).json()
num_jokes = len(response["results"])

if num_jokes == 1:
    print(f"I've got one joke about {keyword}, Here it is: ")
    print(response["results"][0]["joke"])
elif num_jokes > 1:
    print(f"I've got {num_jokes} about {keyword}. Here is one: ")
    print(choice(response["results"])["joke"])
else:
    print(f"Sorry i don't have any jokes about {keyword}! please try again.")
