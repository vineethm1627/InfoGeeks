import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import config

def TwitterClient():

    # attempt authentication
    try:
        
        # create OAuthHandler object
        auth = OAuthHandler(config.consumer_key, config.consumer_secret)
        
        # set access token and secret
        auth.set_access_token(config.access_token, config.access_token_secret)
        
        # create tweepy API object to fetch tweets
        api = tweepy.API(auth)
        
        return api
        
    except:
        print("Error: Authentication Failed")

def clean_tweet(tweet):
    
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    
    return ' '.join(re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    
    else:
        return 'negative'

def get_tweets(api, query, count = 10):
    
    '''
    Main function to fetch tweets and parse them.
    '''
    # empty list to store parsed tweets
    tweets = []

    try:
        # call twitter api to fetch tweets
        fetched_tweets = api.search(q = query, count = count, lang='en')

        # parsing tweets one by one
        for tweet in fetched_tweets:
            
            # empty dictionary to store required params of a tweet
            parsed_tweet = {}

            # saving text of tweet
            parsed_tweet['text'] = tweet.text
            
            # saving sentiment of tweet
            parsed_tweet['sentiment'] = get_tweet_sentiment(tweet.text)

            # appending parsed tweet to tweets list
            if tweet.retweet_count > 0:
                
                # if tweet has retweets, ensure that it is appended only once
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
                    
            else:
                tweets.append(parsed_tweet)

        # return parsed tweets
        return tweets

    except tweepy.TweepError as e:
        # print error (if any)
        print("Error : " + str(e))


def get_tweets_main(query):
    api = TwitterClient()
    tweet_results = list(get_tweets(api,query=query,count=50))
    return tweet_results
    