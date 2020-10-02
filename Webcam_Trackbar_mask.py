import cv2 
import numpy as np

# Using the webcam
cap = cv2.VideoCapture(0)
cap.set(3,640) #width id is 3
cap.set(4,480) #height id is 4
cap.set(10,100) #brightness id is 10

#Trackbar 
def empty(a):
    pass 
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty) # name of the bar, TrackBar, min, max, function
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",0,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",0,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)

while True:
    _,img = cap.read()    # first parameter True or False and the second parameter set of images which forms a video
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min","TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max","TrackBars")
    v_min = cv2.getTrackbarPos("Val Min","TrackBars")
    v_max = cv2.getTrackbarPos("Val Max","TrackBars")
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    success, img = cap.read()
    cv2.imshow("Video",img)
    cv2.imshow("mask",mask)
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break