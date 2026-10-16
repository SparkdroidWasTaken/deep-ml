from math import cos as c, sin as s
def rotation_layer(X, angle):
    points = []
    for i in range(len(X)):
        points.append([X[i][0]*c(angle)-X[i][1]*s(angle),X[i][0]*s(angle)+X[i][1]*c(angle)])
    return points
    pass