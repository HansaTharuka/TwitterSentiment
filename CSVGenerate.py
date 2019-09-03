import tweepy
from textblob import TextBlob
import sys
import csv

if len(sys.argv) >= 2:
	topic = sys.argv[1]
else:
	print("By default topic is maithripala sirisena.")
	topic = "Maithripala"

consumer_key= 'OmK1RrZCVJSRmKxIuQqkBExvw'
consumer_secret= 'VWn6OR4rRgSi7qGnZHCblJMhrSvj1QbJmf0f62uX6ZQWZUUx5q'

access_token='4852231552-adGooMpTB3EJYPHvs6oGZ40qlo3d2JbVjqUUWkJ'
access_token_secret='m9hgeM9p0r1nn8IoQWJYBs5qUQu56XmrAhsDSYKjuiVA4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Maithripala Sirisena')

with open('sentiment.csv', 'w', newline='\n') as  f:

	writer = csv.DictWriter(f, fieldnames=['Tweet', 'Sentiment'])
	writer.writeheader()
	for tweet in public_tweets:
		text = tweet.text
		#Cleaning tweet
		cleanedtext = ' '.join([word for word in text.split(' ') if len(word) > 0 and word[0] != '@' and word[0] == '.' and word[0] != '#' and 'http' not in word and word != 'RT'])
		
		analysis = TextBlob(cleanedtext)

		sentiment = analysis.sentiment.polarity
		if sentiment >= 0:
			polarity = 'Positive'
		else:
			polarity = 'Negative'

		#print(cleanedtext, polarity)

		writer.writerow({'Tweet':soup.text, 'Sentiment':polarity})
