import cv2	# importing cv2 library

vs = cv2.VideoCapture(0)        # initialize camera

while True:     # infinite loop
	_, img = vs.read()      # read the frame from camera
	cv2.imshow("VideoStream", img)   # show a frame
	#print(_)qwww

	# 3 below line, frame will show continusly untill you press "q" button in your keybord
	key = cv2.waitKey(1) & 0xFF # record my key press -Hex
	if key == ord("q"):
		break   # infinite loop will be broken

vs.release()   # release the camera 
cv2.destroyAllWindows() # all opend window will be closed

'''
when you are geting an ~intandation error~
step 1: select All {ctrl+A}
step 2: go to Format Tabify Region
        {alt + 5}
step 3: press ~Ok~
'''
