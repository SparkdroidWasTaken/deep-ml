import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
    #max value
    Max = np.max(scores)
    return scores -  Max - np.log(np.sum(np.exp(scores-Max)))
	pass