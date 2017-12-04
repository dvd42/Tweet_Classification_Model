#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:01:30 2017

@author: diego
"""

from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score
import math as m
import numpy as np

import runtime_parser as rp
import file_writer as fw

def train(X_train,y_train):
    
    positives = 0
    negatives = 0
    table = {}
    
        
    
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
                
    return table,positives,negatives #TODO 



def evaluate(accuracy,precision,recall,f_score):
    
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
        path = fw.create_dir()
        fw.store_results(path,accuracy,precision,recall,f_score)
        
        
        
        
def compute_likelihood(X_test,y_test,table,positives,negatives):
    
    y_pred = np.zeros((y_test.shape))
    likelihood_pos = 0
    likelihood_neg = 0
    n_words = len(table)
    
    
    for i in range(X_test.size):
        for word in X_test[i].split():
            if word in table:
                likelihood_pos += m.log((table[word][0]+1)/float(positives + 1*n_words))
                likelihood_neg += m.log((table[word][1] + 1)/float(negatives + 1*n_words))
                
            else:
                 likelihood_pos +=  m.log(1/float(positives + 1*n_words))
                 likelihood_neg += m.log(1/float(negatives + 1*n_words))
            
        likelihood_pos += m.log(0.52)
        likelihood_neg += m.log(0.48)
        
          
        if likelihood_neg < likelihood_pos: 
            y_pred[i] = 1
    
    
    
    return accuracy_score(y_test,y_pred),precision_score(y_test,y_pred),recall_score(y_test,y_pred),f1_score(y_test,y_pred)
    