import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3,frameWidth) # (ID,argument)
cap.set(4,frameHeight) # (height ID, frameHeight)
cap.set(10,150) # beightness reduce 150

# mask colour values of hue, sat, and val
myColors = [[5,107,0,19,225,225],                
            [133,56,0,159,159,255],
            [57,76,0,100,255,255]]

myColorValues = [[51,153,255],
                [255,0,255],
                [0,255,0]]

myPoints = []    # x,y colorDI

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y=getContour(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y !=0:
            newPoints.append([x,y,count])
        count += 1
        # cv2.imshow(str(color[0]),mask)
    return newPoints


def getContour(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500: #removes noise
            cv2.drawContours(imgResult,cnt,-1,(255,0,255),3)  #on what frame, contour,index,colour,thickness
            per1 = cv2.arcLength(cnt,True) # contour, is it closed
            approx = cv2.approxPolyDP(cnt,0.02*per1,True)   # approximate the corner poitns
            objCor = len(approx)
            if objCor == 3:
                objectType = "Triangle"
            elif objCor == 4: 
                aspectratio = w/float(h)
                if aspectratio > 0.9 and aspectratio < 1.1: 
                    objectType = "Square"
                else: 
                    objectType = "Rectangle"
            else: 
                objectType = "Ciricle"
            x,y,w,h = cv2.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,myColourValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),10,myColourValues[point[2]],cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    findColor(img, myColors,myColorValues)
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints, myColorValues)


    cv2.imshow("Result",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
