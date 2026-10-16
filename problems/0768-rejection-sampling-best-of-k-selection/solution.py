def rejection_sampling_best_of_k(candidates, scores):
    """
    Select the highest-scoring candidate per prompt.

    Args:
        candidates: list of N lists, each containing K candidate outputs.
        scores: list of N lists, each containing K reward scores.

    Returns:
        List of N selected candidates.
    """
    accepted =[]
    for i in range(len(scores)):
        best_score = -999
        best_idx = 0
        for j in range(len(scores[i])):
            if scores[i][j] > best_score:
                best_score = scores[i][j]
                best_idx = j
        accepted.append(candidates[i][best_idx])
    return accepted
    pass