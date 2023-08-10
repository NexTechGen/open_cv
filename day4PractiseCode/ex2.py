import cv2	# importing cv2 library

img = cv2.imread("smp.jpg")	# reading an image

# cv2.GaussianBlur(src,(kernel),borderType)
gaussianBlurImg = cv2.GaussianBlur(img,(21,21),0)	#  applying GaussianBlur

cv2.imwrite("ex2_gaussianBlurImg.jpg", gaussianBlurImg)	# save an image