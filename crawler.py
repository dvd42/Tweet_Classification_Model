from splinter import Browser
import csv
import time as t
import sys
from langdetect import detect,lang_detect_exception

def go_spider_go(filename,target, retweets=True,encoding='utf-8',scroll_pause=0.5,headless=False):

    """[summary]
    
    [description]
    """

    tweets_id = 'stream-items-id'
    tweet_css = '.tweet'
    user_css = '.username'
    text_css = '.js-tweet-text-container'
    tweet_id = 'data-tweet-id'

    url,user = filterInput(filename,target, encoding)
    browser = Browser('firefox',headless=headless)                                                     
    browser.visit(url)                                                        

    tweets = {}
    i = 0
    height = 0

    start = t.time()
    while (t.time() - start) < 1000 * scroll_pause :

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

    print "Number of loaded tweets: %d" % len(loaded_tweets)

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

def in_english(text):
    
    """
    Checks if a tweet is in english
        
    Parameters:
        text {[string]} -- [tweet text]
    
    Returns:
        [boolean] -- [True if tweet text is in English False otherwise]
    """

    try:
        return detect(text) == 'en'
    except lang_detect_exception.LangDetectException as e:
        return False
    

def filterInput(filename,target, encoding):

    user = False
    url = 'https://twitter.com/'
    target = target.encode(encoding)

    if '@' not in target:                            
        url += 'hashtag/' + target 
    else:                                     
        url += target.replace('@','')
        user = True

    return url,user
