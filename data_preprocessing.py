from sklearn.model_selection import StratifiedKFold
import pandas as pd


def process_data(data):
    """Extract the data from csv file

    Args:
        data: (:obj: 'str'): The path to the csv where the tweets are stored
    
    Returns:
        X: (:obj: 'str numpy array'): Tweets
        y: (:obj: 'int numpy array'): Tweet classes (0,1)
    
    """

    dataset = pd.read_csv(data,sep=';')
    dataset = dataset.dropna()
    X = dataset.iloc[:,1].values
    y = dataset.iloc[:,3].values


    return X,y
    

def split_data(X,y,n_splits):
    """Prepares the data for k-fold

    Args:
        X: (:obj: 'str numpy array'): Tweets
        y: (:obj: 'int numpy array'): Tweet classes (0,1)
    
    Returns:
        (:obj: 'StratifiedKFold')
        
    """

    return StratifiedKFold(n_splits,shuffle=True)