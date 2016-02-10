###LANE DETECTION PROJECT#####

import numpy as np
import cv2
import os
from PIL import Image

#Reading all the images from dataset file
Im = []
for file in os.listdir("cordova1"):#Reading all the training images
    Im.append(np.array(Image.open(os.path.join("cordova1",file))))

    
#print np.shape(Im)
#img = cv2.imread('WashLane.png')
#while(True):
for i in range(len(Im)):
    img = Im[i]
    #ret, img = cap.read()
    if img is None:
        break


    I = img
    gray = img
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),3)
    edge = cv2.Canny(gray,1,150,3)#Canny edge detection
    lines = cv2.HoughLinesP(edge,1,np.pi/180,100,1,10)#Hough transform on the image to detect lines
    if lines is None:
        lines = []
    for line in lines:
        for obj in line:
            #print obj
            [x1,y1,x2,y2] = obj
            dx,dy = x2-x1,y2-y1
            angle = np.arctan2(dy,dx) * (180/np.pi)
            #print angle
            if abs(angle)>20:
                cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)


    img = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    for line in lines:
        for obj in line:
            [x1,y1,x2,y2] = obj
            dx,dy = x2-x1,y2-y1
            angle = np.arctan2(dy,dx) * (180/np.pi)
            if abs(angle)>20:#for removing horizontal lines
                cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    #cv2.imshow('Houghlines_edge',img)
    #cv2.waitKey(1)

    ht,wd,dp = img.shape

    img[0:int(ht/2.25),:] = [0,0,0]
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(5,5),3)

    edge = cv2.Canny(gray,0,5,3)
    lines = cv2.HoughLinesP(edge,1,np.pi/180,100,1,10)
    if lines is None:
        lines = []
    for line in lines:
        for obj in line:
            #print obj
            [x1,y1,x2,y2] = obj
            dx,dy = x2-x1,y2-y1
            angle = np.arctan2(dy,dx) * (180/np.pi)
            #print angle
            if abs(angle)>20:
                cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

    img = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    for line in lines:
        for obj in line:
            [x1,y1,x2,y2] = obj
            dx,dy = x2-x1,y2-y1
            angle = np.arctan2(dy,dx) * (180/np.pi)
            if abs(angle)>20:
                #print x1, x2
                #if x1>200 and x2<500:
                    #cv2.line(I,(x1,y1),(x2,y2),(0,255,0),5)
                    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),5)
                    

    cv2.imshow('image',I)
    #cv2.imshow('binaryimage',img)
    cv2.waitKey(1)
    

    #video = cv2.VideoWriter('video.avi',-1,1,(Shape[0],Shape[1]))
    #video.write(I)
    
#cv2.imshow('image',gray)
#cv2.waitKey(10000)
print "over"
cv2.destroyAllWindows()
