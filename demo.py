# -*- coding: utf-8 -*-

import tweepy
from textblob import TextBlob
count = 0
sentimentvalue = 0.0
# Step 1 - Authenticate
consumer_key= 'OmK1RrZCVJSRmKxIuQqkBExvw'
consumer_secret= 'VWn6OR4rRgSi7qGnZHCblJMhrSvj1QbJmf0f62uX6ZQWZUUx5q'

access_token='4852231552-adGooMpTB3EJYPHvs6oGZ40qlo3d2JbVjqUUWkJ'
access_token_secret='m9hgeM9p0r1nn8IoQWJYBs5qUQu56XmrAhsDSYKjuiVA4'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Putin')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself

    

for tweet in public_tweets:
    print(tweet.text)
    count += 1
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("******")
    print(analysis.sentiment.polarity)
    print("******")
    sentimentvalue +=(analysis.sentiment.polarity)
    print("")
    print(sentimentvalue/count)
    
    