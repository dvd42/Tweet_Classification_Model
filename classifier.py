import math as m
import numpy as np
import time as t


from nltk.stem.lancaster import LancasterStemmer


# Classify user or hashtag as positive or negative
def classify(tweets,table,positives,negatives,p_tweets,n_tweets):

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


        if likelihood_neg < likelihood_pos: 
            y_pred[i] = 1

    prediction = np.bincount(y_pred)

    print "Known words: %d" % in_table
    print "Unknown words %d\n" % not_in_table

    return 0 if prediction[0] > prediction[1] else 1,prediction[1],prediction[0]
