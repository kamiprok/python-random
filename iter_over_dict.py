import requests
import praw
import time
import random

reddit = praw.Reddit(user_agent='',
                     client_id='',
                     client_secret='',)

var1: str = 'word1'
var2: str = 'word2'

dict = {"rand_words": ['word', var1, var2]}

i = 0

while True:
    i += 1
    print(i)
    item = random.choice(dict['rand_words'])
    print(f'random choice: {item}')
    if item == var1:
        response = requests.get('https://en.wikipedia.org/wiki/Special:Random')
        item = response.url
        print(item)
    elif item == var2:
        for submission in reddit.subreddit('random').top('day', limit=1):
            item = submission.shortlink
            print(item)
            continue
    else:
        print(item)
    time.sleep(2)

# iterate over dictionary to pick at random either str, random wiki article or random submission from random subreddit
