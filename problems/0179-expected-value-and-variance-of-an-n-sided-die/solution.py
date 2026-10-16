def dice_statistics(n: int) -> tuple[float, float]:
	"""
	Compute the expected value and variance of a fair n-sided die roll.

	Args:
		n (int): Number of sides of the die

	Returns:
		tuple: (expected_value, variance)
	"""
	# Your code here
	nums = 0
	for i in range(1,n+1):
		nums += i
	
	exp_val = nums/n
	var = 0
	for i in range(1,n+1):
		var += (i-exp_val)**2
	
	return (exp_val,var/n)
	pass