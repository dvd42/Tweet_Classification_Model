#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:00:20 2017

@author: diego
"""
from sklearn.model_selection import StratifiedKFold
import pandas as pd


def process_data():
    dataset = pd.read_csv("FinalStemmedSentimentAnalysisDataset.csv",sep=';')
    dataset = dataset.dropna()
    X = dataset.iloc[:,1].values
    y = dataset.iloc[:,3].values

    return X,y


def split_data(X,y,n_splits):
    
    return StratifiedKFold(n_splits,shuffle=True)