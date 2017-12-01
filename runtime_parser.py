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
        print "Usage: main.py, data-set.csv"
        print "-k number of splits for the k-fold cross_validation method"
        print "-v will show results on the standard output (if this is not entered the results and plots will be stored in the wd)"
        print "NOTE: The default runtime parameters are (-k 5)"
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
