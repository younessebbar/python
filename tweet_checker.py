max_chars = 140
tweet = input("Enter your tweet: ")
tweet_length = len(tweet)

if tweet_length < max_chars:
    print(f"That {tweet_length} char tweet will work")
else:
    print(f"Your {tweet_length} char tweet is {tweet_length - max_chars} too long")