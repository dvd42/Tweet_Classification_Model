#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:03:11 2017

@author: diego
"""

import data_preprocessing as dp
import train_evaluate as te
import runtime_parser as rp


# Trains and validates the model
def test():
    
    accuracy = []
    precision = []
    recall = []
    f_score = []
    
    
    print "Running model with:\nK = %d\n%s samples\nMax_words: %s\n" % (rp.k,rp.size,rp.w)
    
    X,y = dp.process_data(rp.data)
    size = X.size if rp.size == "n" else int(rp.size)
    
    skf = dp.split_data(X, y,rp.k)
    
    # Train and test with each split
    for train_index, test_index in skf.split(X,y):
        X_train,X_test = X[train_index][:size],X[test_index]
        y_train,y_test = y[train_index][:size],y[test_index]
    
        table,positives,negatives = te.train(X_train,y_train)
    
        a,p,r,f = te.compute_likelihood(X_test,y_test,table,positives,negatives,y_train[y_train == 1].size,y_train[y_train == 0].size)

        # Store metrics for each split
        accuracy.append(a)
        precision.append(p)
        recall.append(r)
        f_score.append(f)
    
    te.evaluate(accuracy,precision,recall,f_score)

