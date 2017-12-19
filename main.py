#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:48:33 2017

@author: diego
"""

import bayes
import runtime_parser as rp

if not rp.test:
	bayes.validate()

else:
	group,positive_ratio = bayes.test()

	group = "Positive" if group  else "Negative"
	element = "Hashtag" if '#' in rp.target else "User"


	print "%s is a %s %s" % (rp.target,group,element)
	print "Positive Ratio: %.2f" % positive_ratio
