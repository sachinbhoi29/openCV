import cv2
import numpy as np

path = "Resources/shapes.jpg"


def getContour(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print('Area',area)
        if area>500: #removes noise
            cv2.drawContours(imgContour,cnt,-1,(255,0,255),3)  #on what frame, contour,index,colour,thickness
            per1 = cv2.arcLength(cnt,True) # contour, is it closed
            print('Perimeter',per1)
            approx = cv2.approxPolyDP(cnt,0.02*per1,True)   # approximate the corner poitns
            print('Number of corners',len(approx))
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
            print('x',x,'y',y,'w',w,'h',h)
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.4,
                        (0,0,0),1)             
                        #on which image, what to write, x and y, font, scale, color, fontscale

img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)    #image, kernal, sigma
imgCanny = cv2.Canny(imgBlur,50,50) #image, threshold, threshold
imgContour = img.copy()
getContour(imgCanny)

cv2.imshow("Orignal",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Image contour",imgContour)

cv2.waitKey(10000)


