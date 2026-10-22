def sparse_dot_product(vec1, vec2):
    # vec1 and vec2 are lists of numbers of equal length
    # return their dot product
    #can I really just:
    sum = 0
    for i in range(len(vec1)):
        sum += vec1[i]*vec2[i]
    return sum
    #turn into sparse vectors
    # sparse_vec1 = []
    # sparse_vec2= []
    # for i in range(len(vec1)):
    #     if vec1[i] != 0:
    #         sparse_vec1.append(i,vec1[i])
    #     if vec2[i] != 0:
    #         sparse_vec2.append(i,vec2[i])
    pass