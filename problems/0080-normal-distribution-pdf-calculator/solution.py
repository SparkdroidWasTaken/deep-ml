import math

def normal_pdf(x, mean, std_dev):
	"""
	Calculate the probability density function (PDF) of the normal distribution.
	:param x: The value at which the PDF is evaluated.
	:param mean: The mean (μ) of the distribution.
	:param std_dev: The standard deviation (σ) of the distribution.
	"""
	# Your code here
	norm_d = math.sqrt(2*math.pi*(std_dev**2))
	exp_n = -((x-mean)**2)
	exp_d = 2*(std_dev**2)
	exp = math.exp(exp_n/exp_d)
	val = (1/norm_d)*exp
	return round(val,5)