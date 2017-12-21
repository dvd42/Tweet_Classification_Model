import os
import csv

import runtime_parser as rp

def create_dirs():
	"""Create directories to store results"""

   
	if not os.path.exists("table"):
		os.makedirs("table")

	
	if not os.path.exists(rp.target):
		os.makedirs(rp.target)



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
		for key,value in table.iteritems():
			if i == 0:
				row = [key,value[0],value[1],p_tweets,n_tweets]
			else:
				row = [key,value[0],value[1]]

			i += 1
			wr.writerow(row)




