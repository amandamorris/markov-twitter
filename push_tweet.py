import markov
import os
import twitter
import sys

API = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                      consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                      access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                      access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
def push_tweet(tweets):

    
    #print API.VerifyCredentials()
    status = API.PostUpdate(tweets)
    print status.text
    return API


def tweet_loop():

    while True:
        random_text = markov.make_text(chains, ngram_num)
        if len(random_text) <= 140:
            if random_text not in get_all_tweets(API):
              push_tweet(random_text)
              print "\n"
              retweet = raw_input("Press Enter if you'd like to tweet another line or q to quit. ")
              if retweet == "q":
                  break


def get_all_tweets(API):
    status = API.GetUserTimeline(819333494757150721)
    prev_tweets_only = []
    for i in range(len(prev_tweets)):
        prev_tweets_only.append(prev_tweets[i].text)
    return prev_tweets_only

input_path = sys.argv[1]
ngram_num = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = markov.open_and_read_file(input_path)
#print input_text

# Get a Markov chain
chains = markov.make_chains(input_text, ngram_num)
#print chains

#tweet_loop()
prev_tweets = get_all_tweets(API)
#print prev_tweets
