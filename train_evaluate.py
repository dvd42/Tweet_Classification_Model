from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
import math as m
import numpy as np
from collections import OrderedDict

import runtime_parser as rp
import file_writer as fw


def train(X_train,y_train):
    """Builds the joint distribution table
    
    Args:
        X_train: (:obj: 'str numpy array'): Tweets for training
        y_train: (:obj: 'int numpy array'): Tweet class (0,1)
    
    Returns:
        new_table (:obj: 'dict'): Words and its total appearances and its negatives and positives appearances (e.g dict['hello']=[15,5,10])
        
        positives (int): All positive word appearances
        negatives (int): All negative word appearances
        
    """


    positives = 0
    negatives = 0
    table = OrderedDict()
    
    print "The model is learning\n"

    for i in range(X_train.size):
        for word in X_train[i].split():
            if word not in table:
                table[word] = [0,0,0]
                
            if y_train[i] == 1:
                table[word][1] += 1
                positives += 1
            else:
                table[word][2] += 1
                negatives += 1
            
            table[word][0] += 1
            
    new_table = table


    # Reduce dictionary size if length has been specified
    if rp.w != "m":
        new_table = {}
       
        # Keep only the m most frequent words
        table = sorted(table.iteritems(), key=lambda (k,v): (v,k),reverse=True)
        table = table[:int(rp.w)]
        for key,value in table:
            new_table[key] = value
            
                 
        # Recalculate amount of positives and negatives appearances
        positives = 0
        negatives = 0
        for key in new_table:
            positives += new_table[key][1]
            negatives += new_table[key][2]
    
    
    return new_table,positives,negatives

def evaluate(accuracy,precision,recall,f_score,verbose=True):

    """Calculate the average metrics

    Args:  
        accuracy: (:obj: 'list'): The accuracy value of each k-fold iteration
        precision: (:obj: 'list'): The precision value of each k-fold iteration
        recall: (:obj: 'list'): The recall value of each k-fold iteration
        f1_score: (:obj: 'list'): The f1_score value of each k-fold iteration
        verbose: (bool): Whether to show the results or store them in wd
    """
    
    accuracy = sum(accuracy)/len(accuracy)
    precision = sum(precision)/len(precision)
    recall = sum(recall)/len(recall)
    f_score = sum(f_score)/len(f_score)    

    
    if verbose:
        print "Accuracy: %.2f " % accuracy
        print "Precision: %.2f " % precision
        print "Recall: %.2f " % recall
        print "f1_score: %.2f " % f_score

        
        
    else:
        fw.store_results("metrics",accuracy,precision,recall,f_score)
        
        
        

def compute_likelihood(X_test,y_test,table,positives,negatives,p_tweets,n_tweets):
    """Classifies tweets into positives or negatives
    
     Args:
        X_test: (:obj: 'str numpy array'): Tweets for validating
        y_test: (:obj: 'int numpy array'): Tweet class (0,1)
        table: (:obj: 'dict'): Words and its negatives and positives appearances (e.g dict['hello']=[5,10])
        positives: (int): All positive word appearances
        negatives: (int): All negative word appearances
        p_tweets: (int): Positives tweets
        n_tweets: (int): Negatives tweets


    Returns:
        float: accuracy score
        float: precision score
        float: recall score
        float: f1_score score
            
    """

    y_pred = np.zeros((y_test.shape))

    n_words = len(table)
        
    for i in range(X_test.size):
        likelihood_pos = 0
        likelihood_neg = 0

        # MAP negatives and positives using laplace smoothing
        for word in X_test[i].split():
            if word in table:
                likelihood_pos += m.log((table[word][1]+1)/float(positives + 1*n_words))
                likelihood_neg += m.log((table[word][2]+1)/float(negatives + 1*n_words))
                
            else:
                likelihood_pos +=  m.log(1/float(positives + 1*n_words))
                likelihood_neg += m.log(1/float(negatives + 1*n_words))

        likelihood_pos += m.log(p_tweets/float(p_tweets + n_tweets))
        likelihood_neg += m.log(n_tweets/float(p_tweets + n_tweets))


        if likelihood_neg < likelihood_pos: 
            y_pred[i] = 1
   
    return accuracy_score(y_test,y_pred),precision_score(y_test,y_pred),recall_score(y_test,y_pred),f1_score(y_test,y_pred)






    
