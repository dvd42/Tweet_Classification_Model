from splinter import Browser
import csv


def go_spider_go(target, retweetsOfUser=True,browserType='phantomjs', filename=None, encodeText='utf-8', number_of_tweets=100):
    id_list_of_tweets = 'stream-items-id'
    css_of_tweet = '.tweet'
    css_of_user_in_tweet = '.username'
    css_of_text_in_tweet = '.js-tweet-text-container'

    completeUrl, filename, target, user = filterInput(filename,target, encodeText)
    browser = Browser(browserType)                                                     
    browser.visit(completeUrl)                                                        

    tweets = {}
    while len(tweets) < number_of_tweets:
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        for tweet in browser.find_by_id(id_list_of_tweets)[0].find_by_css(css_of_tweet):

            # TODO: get only tweets in english
            # TODO: refresh page when limit is hit
            # TODO: break when no more tweets can be found
            #FIXME: phantomjs does not scrap hashtags properly

            if user: 
                element = tweet.find_by_css(css_of_user_in_tweet)[0].text[1:].encode(encodeText)
            else:
                element = tweet.find_by_css(css_of_text_in_tweet).text

            if target in element:
                tweets[tweet['data-tweet-id']] = tweet


    print "Number of loaded Tweets: %d\n" % len(tweets)

    
    with open(filename, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(["Tweets"])

        for tweet in tweets.values():                                                
            wr.writerow([tweet.find_by_css(css_of_text_in_tweet).text.encode(encodeText)])
            
            

    browser.quit()



def filterInput(filename,target, encodeText):
    user = False
    completeUrl = 'https://twitter.com/'
    arg0 = target.encode(encodeText)
    name = str(arg0).replace('#','').replace('@','')

    if '#' in arg0:                             #Check if Its a Hashtag.
        completeUrl += 'hashtag/' + name
    else:                                       #Its an User
        completeUrl += name
        user = True

    if filename == None:                        #If no filename is given
        filename = name + 'tweets'

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