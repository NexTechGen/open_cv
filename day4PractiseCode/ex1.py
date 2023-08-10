import cv2	# importing cv2 library
import imutils	# importing imutils library

img = cv2.imread("smp.jpg") 	# read an image

resizeImge = imutils.resize(img, width=50)	# resize an image

cv2.imwrite("ex1_resizeImage.jpg", resizeImge)	# save an image