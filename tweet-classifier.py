
# This program makes use of the tweepy library to interact with the Twitter API and pull tweets, as well as the TextBlob library
# Which is used to classify the tweets by measuring their polarity, subjectivity, and intensity

# With TextBlob, each word in the lexicon has scores for:
# 1) polarity: negative vs. positive    (-1.0 => +1.0)
# 2) subjectivity: objective vs. subjective (+0.0 => +1.0)
# 3) intensity: modifies next word?      (x0.5 => x2.0)

# TextBlob returns something like this:
# Sentiment(polarity=0.8, subjectivity=0.75)
# We can see that polarity is 0.8, which means that the statement is positive and 0.75 subjectivity refers that mostly it is a public opinion and not a factual information.

# This program pulls tweets from twitter based on a user defined keyword and sorts them based on their polarity
# >= 0.5 is considered a positive tweet
# < 0.5 is considered a negative tweet
# These values can be easily modified by simply changing the hardcoded value in the sortTweets function

from textblob import TextBlob
import tweepy

positiveTweets = []
negativeTweets = []

keyword = input('Enter a keyword to search on Twitter: ')

def getSentiment(sentimentString):
    return float(sentimentString.split('Sentiment(polarity=',1)[1].split(',')[0])

def sortTweets(tweet,sentiment):
    if(sentiment>=0.5):
        positiveTweets.append(tweet)
    else:
        negativeTweets.append(tweet)


def printTweets(tweet_array):
    for tweet in tweet_array:
        analysis = TextBlob(tweet.text)
        sentiment = getSentiment(str(analysis.sentiment))
        sortTweets(tweet.text,sentiment)

    print("Positive Tweets:\n")
    print(*positiveTweets, sep = "\n")
    print("Negative Tweets:\n")
    print(*negativeTweets, sep = "\n")


# Tweepy interaction with Twitter API
consumer_key = 'These are unique values to your twitter app which need to be hardcoded here!'
consumer_secret = 'These are unique values to your twitter app which need to be hardcoded here!'

access_token = 	'These are unique values to your twitter app which need to be hardcoded here!'
access_token_secret = 'These are unique values to your twitter app which need to be hardcoded here!'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

# Pulling tweets based on user-entered keyword and stored in list
public_tweets = api.search(keyword)

# Printing tweets
printTweets(public_tweets)
