import numpy as np

def compute_r_squared(data, predictions):
    # Write a function that, given two input numpy arrays, 'data', and 'predictions,'
    # returns the coefficient of determination, R^2, for the model that produced 
    # predictions.
    # 
    # Numpy has a couple of functions -- np.mean() and np.sum() --
    # that you might find useful, but you don't have to use them.
    denom = []
    numer = []
    for y in range(1,len(data)):
        denom[y] = (data[y] - predictions[y])**2
        numer[y] = (data[y] - np.mean(data)**2
    numer = numer.sum()
    denom = denom.sum()
    r_squared = 1 - numer/denom
    return r_squared