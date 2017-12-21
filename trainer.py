def train(X_train,y_train):
    """Builds the joint distribution table
    
    Args:
        X_train: (:obj: 'str numpy array'): Tweets for training
        y_train: (:obj: 'int numpy array'): Tweet class (0,1)
    
    Returns:
        new_table (:obj: 'dict'): Words and its negatives and positives appearances (e.g dict['hello']=[5,10])
        
    """

    table = {}
    
    print "The model is learning\n"

    for i in range(X_train.size):
        for word in X_train[i].split():
            if word not in table:
                table[word] = [0,0]
                
            if y_train[i] == 1:
                table[word][0] += 1
            else:
                table[word][1] += 1
    
    return table







    
