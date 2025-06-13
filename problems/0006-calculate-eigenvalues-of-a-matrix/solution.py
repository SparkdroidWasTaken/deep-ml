import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    #b^2-4ac
    b24ac =((-(matrix[0][0]+matrix[1][1]))**2)-4*((matrix[0][0]*matrix[1][1])-(matrix[1][0]*matrix[0][1]))
    #b
    b=(matrix[0][0]+matrix[1][1])
    e1 = (b+math.sqrt(b24ac))/2
    e2 = (b-math.sqrt(b24ac))/2
    eigenvalues = [e1,e2]
	return eigenvalues