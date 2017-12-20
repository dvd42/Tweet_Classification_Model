from splinter import Browser
import csv
import time as t
import sys

def go_spider_go(filename,target, retweets=True,browser='phantomjs', encode_text='utf-8',scroll_pause=0.5):
    tweets_id = 'stream-items-id'
    tweet_css = '.tweet'
    user_css = '.username'
    text_css = '.js-tweet-text-container'
    tweet_id = 'data-tweet-id'
    end = 'timeline'

    url,user = filterInput(filename,target, encode_text)
    browser = Browser(browser)                                                     
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

        # TODO: get only tweets in english
        # FIXME: phantomjs does not scrap hashtags properly
        
        if not retweets and user:
            content = tweet.find_by_css(user_css)[0].text.encode(encode_text)
            if target in content:
                tweets[tweet[tweet_id]] = tweet
        else:
            tweets[tweet[tweet_id]] = tweet

    if len(tweets) == 0:
        print "This user has no tweets"
        sys.exit(1)

    print "Number of related tweets: %d\n" % len(tweets)


    with open(filename, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Tweets"])

        for tweet in tweets.values():
            wr.writerow([tweet.find_by_css(text_css).text.encode(encode_text)])
    
    browser.quit()       

def filterInput(filename,target, encode_text):
    user = False
    url = 'https://twitter.com/'
    target = target.encode(encode_text)

    if '@' not in target:                            
        url += 'hashtag/' + target 
    else:                                     
        url += target.replace('@','')
        user = True

    return url,user
