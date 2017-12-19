#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:01:30 2017

@author: diego
"""

from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
import math as m
import numpy as np
from collections import OrderedDict

import runtime_parser as rp
import file_writer as fw


# Builds the joint distribution table
def train(X_train,y_train):
    """
    :param X_train: tweets in training set 
    :type 1D numpy array
    :param y_train: classes in training set
    :type 1D numpy array
    :return: how many times each word appears in positives and negatives tweets,number of positives words
             number of negatives words   
    :rtype dict key:word value: [positive appearances,negative appearances],int,int
    """

    positives = 0
    negatives = 0
    table = OrderedDict()
    
    print "The model is learning\n"

    for i in range(X_train.size):
        for word in X_train[i].split():

            if word not in table:
                table[word] = [0,0]
                
            if y_train[i] == 1:
                table[word][0] += 1
                positives += 1
            else:
                table[word][1] += 1
                negatives += 1
                        
            
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
            positives += new_table[key][0]
            negatives += new_table[key][1]
    
    
    return new_table,positives,negatives


# Prints the metrics or stores them in wd
def evaluate(accuracy,precision,recall,f_score):

    """
    :param accuracy: list with the accuracy values of each training iteration
    :param precision: list with the precision values of each training iteration
    :param recall: list with the recall values of each training iteration
    :param f_score: list with the f_score values of each training iteration
    
    """

    accuracy = sum(accuracy)/len(accuracy)
    precision = sum(precision)/len(precision)
    recall = sum(recall)/len(recall)
    f_score = sum(f_score)/len(f_score)    

    
    if rp.verbose:
        print "Accuracy: %.2f " % accuracy
        print "Precision: %.2f " % precision
        print "Recall: %.2f " % recall
        print "f1_score: %.2f " % f_score

        
        
    else:
        fw.store_results("metrics",accuracy,precision,recall,f_score)
        
        
        
# Classifies tweets into positives or negatives
def compute_likelihood(X_test,y_test,table,positives,negatives,p_tweets,n_tweets):

    """
    :param X_test: tweets in the test set
    :type 1D numpy array
    :param y_test: class of each tweet
    :type 1D numpy array with 0 or 1 
    :param table: how many times each word appears in positives and negatives tweets
    :type dict key:word value: [positive appearances,negative appearances]
    :param positives: number of positives words
    :param negatives: number of negatives words
    :param p_tweets: number of positives tweets
    :param n_tweets: number of negatives tweets
    :return: accuracy, precision,recall,f1_score
    """

    y_pred = np.zeros((y_test.shape))

    n_words = len(table)
        
    in_table = 0
    not_in_table = 0
    
    for i in range(X_test.size):
        likelihood_pos = 0
        likelihood_neg = 0

        # MAP negatives and positives using laplace smoothing
        for word in X_test[i].split():
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
    
    print(in_table)
    print(not_in_table)

    return accuracy_score(y_test,y_pred),precision_score(y_test,y_pred),recall_score(y_test,y_pred),f1_score(y_test,y_pred)






    
