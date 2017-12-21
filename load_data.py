import pandas as pd
from collections import defaultdict


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
	positives = data_set.iloc[:,2].values
	negatives = data_set.iloc[:,3].values
	words = data_set.iloc[:,0].values
	p_tweets = data_set.iloc[0,4]
	n_tweets = data_set.iloc[0,5]
	
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



