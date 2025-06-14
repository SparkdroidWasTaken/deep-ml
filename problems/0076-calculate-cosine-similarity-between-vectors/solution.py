
import numpy as np

def cosine_similarity(v1, v2):
	# Implement your code here
	pass
    v = np.array(v1)
    u = np.array(v2)
    Magv = np.sqrt(np.sum(v**2))
    Magu = np.sqrt(np.sum(u**2))
    return round((np.dot(v,u)/(Magv*Magu)),3)