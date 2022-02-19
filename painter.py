import cv2
import numpy as np 

def getCountours(img):
    contours,hierarchy =cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>300:
            cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3)
            peri = 0.02*cv2.arcLength(cnt,True)
            approx =cv2.approxPolyDP(cnt,peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y
        
def find_color(img,myColors,myColorValues):
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    count =0
    newPoints= []
    for color,outline in zip(myColors,myColorValues):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(hsv,lower,upper)
        x,y= getCountours(mask)
        cv2.circle(imgResult,(x,y),10,outline,cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count+=1
    return newPoints
        # cv2.imshow(str(color[0]),mask)

def drawArt(myPoints,myColorValues):
    for points in myPoints:
        cv2.circle(imgResult,(points[0],points[1]),10,myColorValues[points[2]],cv2.FILLED)


cap =cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
myColors = [[32,88,112,55,251,255],
            [70,200,60,179,255,255]]
myColorValues = [[157, 235, 14],
                 [235,14, 32]]
myPoint = [] 

while cap.isOpened():
    ret, img= cap.read()
    imgResult =img.copy()
    if ret==True:
        get_points = find_color(img,myColors,myColorValues)
        if len(get_points)!=0:
            for newP in get_points:
                myPoint.append(newP)
        if len(myPoint)!=0:
            drawArt(myPoint,myColorValues)
        cv2.imshow('Output',imgResult)
        if cv2.waitKey(1) & 0xFF==27:
            break
cap.release();
cv2.destroyAllWindows()