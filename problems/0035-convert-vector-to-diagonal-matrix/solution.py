import numpy as np

def make_diagonal(x):
	# Your code here
    #matrix
    m = np.empty((len(x),len(x)))
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i==j:
                m[i][j]=x[i]
    return m
	pass