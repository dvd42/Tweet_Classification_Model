import pandas as pd
from collections import defaultdict


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



def load_table(path):
	"""Loads the joint distribution table
	
	Args:
		data: (:obj: 'str'): The path to the csv where the table is stored
	
	Returns:
		table: (:obj: 'dict'): Words and its negatives and positives appearances (e.g dict['hello']=[5,10])
        (int): positive word appearances
        (int): negative word appearances
      	p_tweets: (int): Positives tweets
        n_tweets: (int): Negatives tweets
	"""	

	data_set = pd.read_csv(path)
	positives = data_set.iloc[:,1].values
	negatives = data_set.iloc[:,2].values
	words = data_set.iloc[:,0].values
	p_tweets = data_set.iloc[0,3]
	n_tweets = data_set.iloc[0,4]
	
	table = defaultdict(list)
	for i in range(len(words)):
	    table[words[i]] = [positives[i],negatives[i]]

	return table,sum(positives),sum(negatives),p_tweets,n_tweets


def load_tweets(path):
	"""Loads the joint distribution table
	
	Args:
		data: (:obj: 'str'): The path to the csv where the tweets is stored
		
	Returns:
        tweets: (:obj: 'str numpy array'): Tweets
	"""	

	data_set = pd.read_csv(path,sep=';')
	data_set = data_set.dropna()
	tweets = data_set.iloc[:,0].values

	return tweets



