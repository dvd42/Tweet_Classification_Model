#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:48:33 2017

@author: diego
"""

import bayes
import runtime_parser as rp

def main():
	if not rp.test:
		bayes.validate()


	else:
		positive_ratio = bayes.test()
		print "%s Positive Ratio: %.2f\n" % (rp.target,positive_ratio)



if __name__ == "__main__":
	main()