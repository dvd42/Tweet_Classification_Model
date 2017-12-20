#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:28:50 2017

@author: diego
"""

import sys


def process_runtime_arguments():
    """
    :return: list with runtime parameters
    """
    
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        # TODO: store this in file and add the rest of the instructions
        print "Usage: main.py, data-set.csv"
        print "-k number of splits for the k-fold cross_validation method"
        print "-size size of the training set (in case you want to train with less samples (if you dont want to reduce the training set use -size n)"
        print "-w maximun number of words you want in the dictionary (if you dont want a limited number use -w n)"
        print "-v will show results on the standard output (if this is not entered the results and plots will be stored in the wd)"
        print "NOTE: The default runtime parameters are (-k 5 -w m -size n)"
        print "NOTE The data-set MUST BE the 2nd argument"
        sys.exit(1)

    argvs = []
    for i in range(len(sys.argv)):
        argvs.append(sys.argv[i])

    return argvs

argvs = process_runtime_arguments()

# Get the the values of the runtime parameters
data = argvs[1]
verbose = True if "-v" in argvs else False
k = int(argvs[argvs.index("-k") + 1]) if "-k" in argvs else 5
size = argvs[argvs.index("-size") + 1] if "-size" in argvs else "n"
w = argvs[argvs.index("-w") + 1] if "-w" in argvs else "m"
target = argvs[argvs.index("-target") + 1] if "-target" in argvs else ""
test = True if "-target" in argvs else False
browser = argvs[argvs.index("-bw") + 1] if "-bw" in argvs else "phantomjs"
sp = argvs[argvs.index("-sp") + 1] if "-sp" in argvs else "0.5"
rt = True if "-rt" in argvs else False

