from random import choice
import sys
import os
import twitter


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    txt_string = open(file_path).read()

    return txt_string


def make_chains(text_string, ngram_num):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    words = text_string.split()
    for index in range(0, len(words) - ngram_num):
        bigram = tuple(words[index:(index + ngram_num)])
        chains.setdefault(bigram, [])
        chains[bigram].append(words[index + ngram_num])

    return chains


def make_text(chains, ngram_num):
    """Takes dictionary of markov chains; returns random text."""


    list_key_cap = [key for key in chains.keys() if key[0][0].isupper()]
    text = choice(list_key_cap)
    sentence = ""
    for index in range(ngram_num):
        sentence = sentence + text[index] + " "

    max_length = 140
    terminal_punct = [".", "?", "!"]

    while True:
        # your code goes here
        if len(sentence) <= max_length:
            try:
                follow_word = choice(chains[text])
            except Exception:
                return sentence

            bigram_list = list(text)[1:ngram_num]
            bigram_list.append(follow_word)
            text = tuple(bigram_list)
            sentence += " " + follow_word
        else:
            for i in range(1, len(sentence)):
                if sentence[-i-1] == " ":#in terminal_punct:
                    return sentence[:-i-1]
            print "Our randomly-generated text has no terminal punctuation in the first {} characters.".format(max_length)
            return


def push_tweet(tweets):

    api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                      consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                      access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                      access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    print api.VerifyCredentials()
    status = api.PostUpdate(tweets)
    print status.text

input_path = sys.argv[1]
ngram_num = int(sys.argv[2])

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)
#print input_text

# Get a Markov chain
chains = make_chains(input_text, ngram_num)
#print chains
# # Produce random text
while True:
    random_text = make_text(chains, ngram_num)
    print random_text
    push_tweet(random_text)
    retweet = raw_input("Press Enter if you'd like to tweet another line or q to quit. ")
    if retweet == "q":
        break
# print random_text
