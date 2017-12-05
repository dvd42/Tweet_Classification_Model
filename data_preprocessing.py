#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 15:00:20 2017

@author: diego
"""
from sklearn.model_selection import StratifiedKFold
import pandas as pd


def process_data(data):

    """
    :param data: path to the csv file holding the data
    :return: tweets,classes
    :rtype 1D numpy_array,1D numpy_array
    """

    dataset = pd.read_csv(data,sep=';')
    dataset = dataset.dropna()
    X = dataset.iloc[:,1].values
    y = dataset.iloc[:,3].values


    return X,y
    

def split_data(X,y,n_splits):
    """
    
    :param X: tweets 
    :param y: classes
    :param n_splits: number of splits for the k-fold
    :return: k-fold iterator
    """
    return StratifiedKFold(n_splits,shuffle=True)