
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
    vL = 0
    LL = 0
    for i in range(len(v)):
        vL += v[i]*L[i]
        LL += L[i]*L[i]
    for i in range(len(L)):
        L[i] *= (vL/LL)
    return L
	pass
