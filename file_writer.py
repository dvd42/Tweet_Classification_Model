#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 1 17:38:21 2017

@author: diego
"""

from __future__ import print_function
import os

import runtime_parser as rp

# Create directories to store results
def create_dir():
    """
    :return: path to store the results in  
    """

    path = "Metrics"

    if not os.path.exists(path):
        os.makedirs(path)
    
    return path


# Store the results in path/Results.txt
def store_results(path,accuracy,precision,recall,f_score):

    print("Running model with:\nK = %d\n%s samples\nMax_words: %s\n\nAccuracy: %.2f\nPrecision: %.2f\nRecall: %.2f\nf1_score: %.2f\n\n"
          % (rp.k,rp.size,rp.w,accuracy,precision,recall,f_score),file=open(path + "/Results.txt", "a+"))
