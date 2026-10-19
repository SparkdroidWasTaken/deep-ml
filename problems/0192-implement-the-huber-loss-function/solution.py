def huber_loss(y_true, y_pred, delta=1.0):
	"""
	Compute the Huber Loss between true and predicted values.

	Args:
		y_true (float | list[float]): Ground truth values
		y_pred (float | list[float]): Predicted values
		delta (float): Transition threshold between MSE and MAE behavior

	Returns:
		float: Average Huber loss
	"""
	# Your code here
	sum = 0
	try:
		for i in range(len(y_true)):
			if abs(y_true[i]-y_pred[i]) <= delta:
				sum += 0.5*((y_true[i]-y_pred[i])**2)
			else:
				sum += delta*(abs(y_true[i]-y_pred[i])-0.5*delta)
		return sum/len(y_true)
	#must be a float
	except:
		return 0.5*((y_true-y_pred)**2) if abs(y_true-y_pred) <= delta else delta*(abs(y_true-y_pred)-0.5*delta)
	pass