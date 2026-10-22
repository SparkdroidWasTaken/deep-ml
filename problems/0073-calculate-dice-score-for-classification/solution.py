
import numpy as np

def dice_score(y_true, y_pred):
	TP = 0
	FP = 0
	FN = 0
	for i in range(len(y_pred)):
		if y_true[i] == 1 and y_pred[i] == 1:
			TP += 1
		elif y_true[i] == 0 and y_pred[i] == 1:
			FP += 1
		elif y_true[i] == 1 and y_pred[i] == 0:
			FN += 1
	denominator = (2*TP+FP+FN)
	if denominator == 0:
		return 0
	else:
		return round((2*TP)/denominator,3)