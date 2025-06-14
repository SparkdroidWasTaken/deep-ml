import math
def calculate_brightness(img):
	# Write your code here
    if img == []:
        return -1
    size = 0
    brightness = 0
    for i in range(len(img)):
        for j in range(len(img[i])):
            size += 1
            if img[i][j] > 255:
                return -1
            else:
                brightness += img[i][j]
    if math.sqrt(size).is_integer():
        return brightness/size
    else:
        return -1

	pass
