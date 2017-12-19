#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:03:11 2017

@author: diego
"""

import data_preprocessing as dp
import train_evaluate as te
import runtime_parser as rp
import sys
import os


import file_writer as fw
import load_data as ld
import crawler
import classifier

# Trains and validates the model
def validate():

    fw.create_dirs()

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




def test():

    fw.create_dirs()

    if not os.path.exists("table/table.csv"):
        X,y = dp.process_data(rp.data)
        table,_,_ = te.train(X,y)
        fw.store_table(table,y[y == 1].size,y[y == 0].size)
    
   

    table,positives,negatives,p_tweets,n_tweets = ld.load_table("table/table.csv")

    #Scrap Tweets and store them in csv file
    crawler.go_spider_go(rp.target,filename= rp.target + "/tweets.csv",browserType=rp.browser,retweetsOfUser=True,number_of_tweets=100)

    tweets = ld.load_tweets(rp.target +"/tweets.csv")

    group,p_class,n_class = classifier.classify(tweets,table,positives,negatives,p_tweets,n_tweets)


    return group,p_class/float(p_class + n_class)










    


