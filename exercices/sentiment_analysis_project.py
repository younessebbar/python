# install two packages for this project
# pip install -U textblob & pip install pyttsx3
from textblob import TextBlob
import pyttsx3


name = input("What is your name ? ")
engine = pyttsx3.init()
engine.say(f"Hello Employee {name}. we hope you had a great day of work. it's time to submit your wellness statement")
engine.runAndWait()

# blob = TextBlob("I really hate you so much moron!")
print("(✦ ‿ ✦)")
print("Enter your employee wellness statement: ")
statement = input("> ")
blob = TextBlob(statement)
while blob.sentiment.polarity < 0.5:
    print(blob.sentiment.polarity)
    if blob.sentiment.polarity < 0.2:
         engine.say(f"{name}. That was a rude statement. please try again and be more positive this time.")
         engine.runAndWait()
    elif blob.sentiment.polarity > 0.2  and blob.sentiment.polarity < 0.5:
         engine.say(f"{name}. Better than before.though try to be a little bit more positive.")
         engine.runAndWait()
    print("╥﹏╥")
    print("More positive please: ")
    statement = input("> ")
    blob = TextBlob(statement)

print("(*^‿^*)")
print("We appreciate you too!")
engine.say(f"{name}. Thank you for such a kind and positive statement, Have a great day")
engine.runAndWait()
