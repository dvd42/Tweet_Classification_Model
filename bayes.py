#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 13:03:11 2017

@author: diego
"""

import pandas as pd
from sklearn.model_selection import train_test_split
#from collections import Counter
#import numpy as np
import math as m


def process_data():
    dataset = pd.read_csv("FinalStemmedSentimentAnalysisDataset.csv",sep=';')
    dataset = dataset.dropna()
    X = dataset.iloc[:,1].values
    y = dataset.iloc[:,3].values

    return X,y


def split_data(X,y):
    # TODO implement k-fold
    return train_test_split(X,y,stratify=y,train_size=0.8)



#TODO implement training using the argmax thing
def train():
    pass


def get_samples(X,y):
    return  X[y == 1],X[y== 0]





def compute_likelihood(X,y,samples):
    
    likelihood = 0
    # TOOD iterate for every tuple
    for word in X[0]:
        word_occurences = 0
        for i in range(samples.shape[0]):
            if word in samples[i]:
                word_occurences+=1
        
        likelihood += m.log((word_occurences+1)/float((samples.size + 1*2)))
            
    # Always 0.5 because of stratification??
    likelihood *= samples.size/float(y.size)
    
    return likelihood    
    
    


X,y = process_data()    
X_train,X_test,y_train,y_test = split_data(X,y)

positives, negatives = get_samples(X_test,y_test)


print "Likelyhood of negative: %f" % compute_likelihood(X_train,y_train,negatives)
print "Likelyhood of positive: %f" % compute_likelihood(X_train,y_train,positives)
    