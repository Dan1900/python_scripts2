#!/usr/bin/env python

import numpy as np
import cv2
import os



help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    cascade = cv2.CascadeClassifier('/home/qd/Desktop/adaboost_train/dt/cascade.xml')
  
    '''
    img = cv2.imread('/media/qd/306897646897279C/Data/pic/Face_01.jpg',1)
    #img = cv2.imread('/media/qd/306897646897279C/test.bmp',1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    rects = detect(gray, cascade)
    vis = img.copy()
    draw_rects(vis,rects,(255,0,0))
   

    cv2.imshow('facedetect', vis)
    cv2.waitKey(0)
    '''
    rootdir='/media/qd/306897646897279C/Data/face_images/'
    for parent,dirnames,filenames in os.walk(rootdir):
    #for dirname in dirnames:
    #   print "parent is:"+parent
    #   print "dirname is :"+dirname

     for filename in filenames:
        #print "parent is: "+parent
        #print "filename is: "+filename
        #print "the full name of the file is: "+os.path.join(parent,filename)
        picname=parent+'/'+filename  
        print picname 
        img=cv2.imread(picname,1)
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #gray=cv2.equalizeHist(gray)
        #cv2.imshow("src",img)
        #cv2.waitKey(0)
        rects=detect(gray,cascade)
        #vis=img.coppy()
        draw_rects(img,rects,(255,0,0))
        cv2.imshow('facedetect', img)
        cv2.waitKey(0)
    
        

       
    