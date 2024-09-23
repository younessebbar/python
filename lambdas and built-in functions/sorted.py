users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"], "color": "purple"},
	{"username": "jeff", "tweets": [], "num": "13", "color": "teal"},
	{"username": "bob123", "tweets": []},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

#sort list of users by username alphabeticaly
print(sorted(users, key=lambda user: user['username']))

#sort list of users by number of tweets
print(sorted(users, key=lambda user: len(user['tweets']), reverse=True))