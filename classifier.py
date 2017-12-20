import math as m
import numpy as np

from nltk.stem.lancaster import LancasterStemmer
 
def classify(tweets,table,positives,negatives,p_tweets,n_tweets):
    """Classify user or hashtag as positive or negative
    
    Args:
        tweets: (:obj: 'str numpy array'): Tweets
        table: (:obj: 'dict'): Words and its negatives and positives appearances (e.g dict['hello']=[5,10])
        positives: (int): positive word appearances
        negatives: (int): negative word appearances
        p_tweets: (int): Positives tweets
        n_tweets: (int): Negatives tweets
    """


    st = LancasterStemmer()

    n_words = len(table)
    in_table = 0
    not_in_table = 0


    y_pred = np.zeros(len(tweets)).astype('int64')

    for i in range(len(tweets)):
        likelihood_pos = 0
        likelihood_neg = 0
        
        # MAP negatives and positives
        for word in tweets[i].split():
            word = st.stem(word.decode('utf-8'))
            if word in table:
                in_table += 1
                likelihood_pos += m.log((table[word][0]+1)/float(positives + 1*n_words))
                likelihood_neg += m.log((table[word][1]+1)/float(negatives + 1*n_words))
                
            else:
                not_in_table += 1
                likelihood_pos +=  m.log(1/float(positives + 1*n_words))
                likelihood_neg += m.log(1/float(negatives + 1*n_words))

        likelihood_pos += m.log(p_tweets/float(p_tweets + n_tweets))
        likelihood_neg += m.log(n_tweets/float(p_tweets + n_tweets))



        # Classify as positive or negative
        if likelihood_neg < likelihood_pos: 
            y_pred[i] = 1

    prediction = np.bincount(y_pred)

    print "Known words: %d" % in_table
    print "Unknown words %d\n" % not_in_table

    return prediction[1],prediction[0]