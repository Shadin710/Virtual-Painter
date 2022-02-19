import cv2
import numpy as np

## Making a tracker
def empty(a):
    pass

cv2.namedWindow("Trackbar")
cv2.resizeWindow('Trackbar',(500,500))
cv2.createTrackbar('Hue Min','Trackbar',0,179,empty)
cv2.createTrackbar('Hue Max','Trackbar',179,179,empty)
cv2.createTrackbar('Sat Min','Trackbar',0,255,empty)
cv2.createTrackbar('Sat Max','Trackbar',255,255,empty)
cv2.createTrackbar('Value Min','Trackbar',0,2555,empty)
cv2.createTrackbar('Value Max','Trackbar',255,255,empty)


cap = cv2.VideoCapture(0)

cap.set(3,640)
cap.set(4,480)


while (cap.isOpened()):
    ret,img =cap.read()
    h_min =cv2.getTrackbarPos('Hue Min','Trackbar')
    h_max =cv2.getTrackbarPos('Hue Max','Trackbar')
    s_min =cv2.getTrackbarPos('Sat Min','Trackbar')
    s_max =cv2.getTrackbarPos('Sat Max','Trackbar')
    v_min =cv2.getTrackbarPos('Value Min','Trackbar')
    v_max =cv2.getTrackbarPos('Value Max','Trackbar')
    if ret==True:
        lower = np.array([h_min,s_min,v_min])
        upper = np.array([h_max,s_max,v_max])
        hsv  = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv,lower,upper)
        
        imgResult= cv2.bitwise_and(img,img,mask=mask)
        cv2.imshow('Real Video',img)
        cv2.imshow('Mask',mask)
        cv2.imshow('Extract Color',imgResult)
        if cv2.waitKey(1) & 0xFF==27:
            break
cap.release()
cv2.destroyAllWindows()