from splinter import Browser
import csv
import time as t
import sys
from langdetect import detect,lang_detect_exception
import itertools, sys

def go_spider_go(filename,target, retweets=True,encoding='utf-8',scroll_pause=0.3,headless=False):


    """Runs the web crawler through Twitter stops when all tweets are found or 1000*scroll_pause seconds have passed
    
    Args:
        filename: (:obj: 'str'): The path to the csv where the tweets will be stored
        target: (:obj: 'str'): The user or hashtag to get the tweets from
        retweets: (boolean, optional): Wheter to scan for user's retweets.
        encoding: (:obj: 'str', optional): Text encoding
        scroll_pause: (float, optional): Time interval between web crawler scrolls
        headless: (boolean, optional): Wheter to show the browser while crawling
    """

    tweets_id = 'stream-items-id'
    tweet_css = '.tweet'
    user_css = '.username'
    text_css = '.js-tweet-text-container'
    tweet_id = 'data-tweet-id'

    url,user = filterInput(target, encoding)
    browser = Browser('firefox',headless=headless)                                                     
    browser.visit(url)                                                        

    tweets = {}
    i = 0
    height = 0

    start = t.time()

   
    spinner = itertools.cycle(['[-]','[/]','[|]','[\\]'])

    print "Reading Tweets...",
    while (t.time() - start) < 1000 * scroll_pause :

        sys.stdout.write(spinner.next())
        sys.stdout.flush()
        sys.stdout.write('\b\b\b')

        current_height = height

        height = browser.driver.execute_script('return document.body.scrollHeight')
        t.sleep(scroll_pause)
        if current_height == height: 
            i += 1
        else:
            i = 0
        
        if i >= 5: break            
                
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    
    loaded_tweets = browser.find_by_id(tweets_id).find_by_css(tweet_css)

    for _ in range(len("Reading Tweets...") + 3):
        sys.stdout.write('\b')

    print "Number of loaded tweets: %d" % len(loaded_tweets)


    # Filter tweets
    for tweet in loaded_tweets:    
        if not retweets and user:
            content = tweet.find_by_css(user_css)[0].text.encode(encoding)
            if target.lower() in content.lower():
                tweets[tweet[tweet_id]] = tweet
        else:
            tweets[tweet[tweet_id]] = tweet

    if len(tweets) == 0:
        print "This user has no tweets"
        sys.exit(1)

    print "Number of related tweets: %d" % len(tweets)

    # Store tweets in csv file
    with open(filename, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Tweets"])
        rows = 0

        for tweet in tweets.values():
            text = tweet.find_by_css(text_css).text            
            if in_english(text):
                rows += 1
                wr.writerow([text.encode(encoding)])
           

                    
    print "Number of tweets in english: %d\n" % rows
                
        
    browser.quit()

    if rows == 0:
        print "This user has no tweets in English"
        sys.exit(1)


def in_english(text):
    """Checks if a tweet is in english
        
    Args:
        text: (:obj: 'str'): Text in the tweet
    
    Returns:
        bool: True if tweet text is in English, False otherwise
    """

    try:
        return detect(text) == 'en'
    except lang_detect_exception.LangDetectException as e:
        return False
    

def filterInput(target, encoding):
    """Determines wheter the target is an user or a hashtag"

    Args:
        target: (:obj: 'str'): The user or hashtag to get the tweets from
        encoding: (:obj: 'str'): Text encoding
    
    Returns:
        url: (:obj: 'str'): The complete URL to get the tweets (e.g: https://twitter.com/user)
        user: (bool): True if we are analyzing an user, False if we are analyzing a hashtag 
    """

    user = False
    url = 'https://twitter.com/'
    target = target.encode(encoding)

    if '@' not in target:                            
        url += 'hashtag/' + target 
    else:                                     
        url += target.replace('@','')
        user = True

    return url,user
