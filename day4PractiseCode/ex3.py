import cv2	# importing cv2 library

img = cv2.imread("smp.jpg")	# reading an image

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	# conver to BGR to Gray image

tresImg = cv2.threshold(grayImg, 50, 255, cv2.THRESH_BINARY)[1] 

cv2.imwrite("ex3_thresholdImg.jpg", tresImg)	# save an image