import pandas as pd


def load_table(path):

	data_set = pd.read_csv(path)
	positives = data_set.iloc[:,1].values
	negatives = data_set.iloc[:,2].values
	words = data_set.iloc[:,0].values
	p_tweets = data_set.iloc[0,3]
	n_tweets = data_set.iloc[0,4]
	
	return words,positives,negatives,p_tweets,n_tweets



def load_tweets(path):

	data_set = pd.read_csv(path,sep=';')
	data_set = data_set.dropna()
	tweets = data_set.iloc[:,0].values

	return tweets



