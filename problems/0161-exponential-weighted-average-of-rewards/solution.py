def exp_weighted_average(Q1, rewards, alpha):
    """
    Q1: float, initial estimate
    rewards: list or array of rewards, R_1 to R_k
    alpha: float, step size (0 < alpha <= 1)
    Returns: float, exponentially weighted average after k rewards
    """
    # Your code here
    sum = 0
    k = len(rewards)
    for i in range(k):
        a = (1-alpha)
        sum += rewards[i]*alpha*(a**(k-i-1))
    return (a**k)*Q1+sum
    pass
