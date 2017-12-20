from __future__ import print_function
import os
import csv

import runtime_parser as rp


def create_dirs():
	"""Create directories to store results"""


    if not os.path.exists("metrics"):
        os.makedirs("metrics")
   

    if not os.path.exists("table"):
    	os.makedirs("table")

    if rp.test:
    	if not os.path.exists(rp.target):
    		os.makedirs(rp.target)



def store_results(path,accuracy,precision,recall,f_score):
	"""Store the results in .txt file  
	
	Args:
		path: (:obj: 'str'): The path were the results will be stored
		accuracy: (float): Accuracy Score
		precision: (float): Precision Score
		recall: (float): Recall Score
		f_score: (float): f1_score
	"""

    print("Running model with:\nK = %d\n%s samples\nMax_words: %s\n\nAccuracy: %.2f\nPrecision: %.2f\nRecall: %.2f\nf1_score: %.2f\n\n"
          % (rp.k,rp.size,rp.w,accuracy,precision,recall,f_score),file=open(path + "/results.txt", "a+"))





def store_table(table,p_tweets,n_tweets):

	"""Stores the joint distribution table in .csv file
	
	Args:
 		table (:obj: 'dict'): Words and its negatives and positives appearances (e.g dict['hello']=[5,10])    
    	p_tweets (int): Positive tweets
    	n_tweets (int): Negative tweets
	"""

	with open("table/table.csv", 'a') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		row0 = ["Words","Positives","Negatives","Positive Tweets","Negatives Tweets"]
		wr.writerow(row0)


		i = 0
		for key in table:
			if i == 0:
				row = [key,table[key][0],table[key][1],p_tweets,n_tweets]
			else:
				row = [key,table[key][0],table[key][1]]

			i += 1
			wr.writerow(row)




