import cv2 #importing opencv library
import time #import time library
import imutils #import imutils library

cam = cv2.VideoCapture(0) #initialized camera
time.sleep(1) #giving 1 second delay for initializing camera

firstFrame=None #make first frame is nothing
area = 800 #threshold for how much change can be noticed in moving object

while True: #infinite loop
    img = cam.read()[1] #reading frame from the camera
    text = "Normal" #no moving object detection
    
    #pre-processing
    img = imutils.resize(img, width=600) #resize the frame to 500 w
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert color to gray scale image
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0) #smoothening

    #save the first frame, into the firstframe variable
    #from the 2nd iteration it wont go inside this if condition
    if firstFrame is None:
            firstFrame = gaussianImg
            continue
    
    imgDiff = cv2.absdiff(firstFrame, gaussianImg) #difference b/w first bg frame with current frame
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1] #detected region will be converted into binary
    threshImg = cv2.dilate(threshImg, None, iterations=2)# dilate the frame

    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)    # finding objec border
    cnts = imutils.grab_contours(cnts)

    # drowing rectangle whith in loop
    for c in cnts:
            if cv2.contourArea(c) < area: 
                    continue
            (x, y, w, h) = cv2.boundingRect(c) # returning start point and width and height
            # x,y is start point
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            text = "Moving Object detected"
    print(text)

    # puting text in frame
    cv2.putText(img, text, (10, 20),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.imshow("cameraFeed",img)

    # exiting
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()
