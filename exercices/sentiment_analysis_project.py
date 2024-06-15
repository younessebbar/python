# install two packages for this project
# pip install -U textblob & pip install pyttsx3
from textblob import TextBlob
import pyttsx3

engine = pyttsx3.init()
engine.say("Hello Employee Younes SEBBAR. we hope you had a great day of work. it's time to submit your employee wellness statement")
engine.runAndWait()

# blob = TextBlob("I really hate you so much moron!")
print("(✦ ‿ ✦)")
print("Enter your employee wellness statement: ")
statement = input("> ")
blob = TextBlob(statement)
while blob.sentiment.polarity < 0.5:
    engine.say("Employee Younes. That was not a positive wellness statement. please try again and be more positive this time.  we know how much you love working here")
    engine.runAndWait()
    print("╥﹏╥")
    print("More positive please: ")
    statement = input("> ")
    blob = TextBlob(statement)

print("(*^‿^*)")
print("We appreciate you too!")
engine.say("Employee Younes. Thank you for such a kind and positive statement, we here the ministry of work appreciate you too! Have a great day")
engine.runAndWait()
