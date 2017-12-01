#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:38:21 2017

@author: diego
"""

from __future__ import print_function
import runtime_parser as rp
import os

# Create directories to store results
def create_dir():

    path = "Metrics"

    if not os.path.exists(path):
        os.makedirs(path)
    
    return path



def store_results(path,accuracy,precision,recall,f_score):
    
    print("Running model with:\nk = %d\n\nAccuracy: %.2f\nPrecsion: %.2f\nRecall: %.2f\nf1_score: %.2f\n\n " 
          % (rp.k,accuracy,precision,recall,f_score),file=open(path + "/Results.txt", "a+"))
