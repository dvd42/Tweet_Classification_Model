from splinter import Browser
import csv


def go_spider_go(tweetsOf, retweetsOfUser = True,dataFileExtension='.csv', 
    browserType='phantomjs', filename=None, encodeText='utf-8', howManyTweets = 100):
    id_list_of_tweets = 'stream-items-id'
    css_of_tweet = '.tweet'
    css_of_user_in_tweet = '.username'
    css_of_text_in_tweet = '.js-tweet-text-container'

    completeUrl, filename, name, user = filterInput(filename, dataFileExtension, tweetsOf, encodeText)
    browser = Browser(browserType)                                                      #Open Browser
    browser.visit(completeUrl)                                                          #Visit TwitterURL

    tweetNum = 0
    tweets = {}
   
    while len(tweets) < howManyTweets:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        for tweet in browser.find_by_id(id_list_of_tweets)[0].find_by_css(css_of_tweet):
            tweets[tweet['data-tweet-id']] = tweet

        print len(tweets)


    print 'Number of Tweets Loaded:', len(tweets)
    
    with open(filename, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Tweets"])

        if user:
            for tweet in tweets.values():                                                   #Foreach tweet save the data we want.
                tweetUser = tweet.find_by_css(css_of_user_in_tweet)[0].text[1:].encode(encodeText)
                if not retweetsOfUser:
                    if name == tweetUser:
                        tweetData = tweet.find_by_css(css_of_text_in_tweet).text
                        wr.writerow([tweetData.encode(encodeText)])
                        tweetNum += 1
                else:
                    tweetData = tweet.find_by_css(css_of_text_in_tweet).text
                    wr.writerow([tweetData.encode(encodeText)])
                    tweetNum += 1
        else:

            for tweet in tweets:
                tweetUser = tweet.find_by_css(css_of_user_in_tweet)[0].text[1:].encode(encodeText)
                tweetText = tweet.find_by_css(css_of_text_in_tweet).text
                if name in tweetText:
                    tweetData = tweet.find_by_css(css_of_text_in_tweet).text
                    wr.writerow([tweetData])
                    tweetNum += 1

    browser.quit()  # Close the browser.
    print 'Related to ' + name + ': ' + str(tweetNum)



def filterInput(filename,dataFileExtension, tweetsOf, encodeText):
    user = False
    completeUrl = 'https://twitter.com/'
    arg0 = tweetsOf.encode(encodeText)
    name = str(arg0).replace('#','').replace('@','')

    if '#' in arg0:                             #Check if Its a Hashtag.
        completeUrl += 'hashtag/' + name
    else:                                       #Its an User
        completeUrl += name
        user = True

    if filename == None:                        #If no filename is given
        filename = name + 'Tweets' + dataFileExtension
    else:
        filename += dataFileExtension

    return completeUrl, filename, name, user


'''
Obligatory:
    tweetsOf: UserName --> '@Avengers' or hashtag --> '#InfinityWar'.
Opcional:
    scrollPauseTime: Time Between Scrolls.
    timesToScroll: How Many Times to Scroll (More Scrolls = More Tweets).
    dataFileExtension: Extension of the data file.
    browserType: Wich Browser To Use (look in splinter for more info)
    filename: Name for the data file.
    encodeText: Encode of the text.
'''