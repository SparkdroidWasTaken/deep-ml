import numpy as np 
def descriptive_statistics(data):
	# Your code here
    d = np.array(data)
    #find the most common value
    values, counts = np.unique(d, return_counts=True)
    mode = values[np.argmax(counts)]
	stats_dict = {
        "mean": np.mean(d),
        "median": np.median(d),
        "mode": mode,
        "variance": np.round(np.var(d),4),
        "standard_deviation": np.round(np.std(d),4),
        "25th_percentile": np.percentile(d,25),
        "50th_percentile": np.percentile(d,50),
        "75th_percentile": np.percentile(d,75),
        "interquartile_range": np.percentile(d,75) - np.percentile(d,25)
    }
	return stats_dict