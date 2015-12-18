import os
import re
import sys
import cv2
from optparse import OptionParser
import numpy as np


def rotateImage(image, angel,factor):#parameter angel in degrees
    height = image.shape[0]
    width = image.shape[1]
##    height_big = height * 2
##    width_big = width * 2
    height_big = height
    width_big = width
    image_big = cv2.resize(image, (width_big, height_big))
    image_center = (width_big/2, height_big/2)#rotation center
##    rot_mat = cv2.getRotationMatrix2D(image_center,angel, 0.5)
    rot_mat = cv2.getRotationMatrix2D(image_center,angel, factor)
    result = cv2.warpAffine(image_big, rot_mat, (width_big, height_big), flags=cv2.INTER_LINEAR)
    return result

dirpath="/media/qd/306897646897279C/Data/neg"
savepath='/media/qd/306897646897279C/Data/neg/aNeg/'
i=0
f=open("/media/qd/306897646897279C/Data/neg/Path_Images_old.txt")
fi=f.read()
list1=fi.split()
count=len(list1)
print count
for ls in range(0,count):   
    picname=list1[ls]
    im=cv2.imread(picname,cv2.cv.CV_LOAD_IMAGE_GRAYSCALE)
    im2=cv2.flip(im,1)
    im3=cv2.flip(im,-1)
    im4=cv2.flip(im,0)
    im5=cv2.equalizeHist(im)
    im6=cv2.GaussianBlur(im2,(3,3),3.0)
    savename=savepath+str(i)+'.jpg'
    #print savename
    cv2.imwrite(savename,im)
    i=i+1
    cv2.imwrite(savepath+str(i)+'.jpg',im2)
    i=i+1;
    cv2.imwrite(savepath+str(i)+'.jpg',im3)
    i=i+1
    cv2.imwrite(savepath+str(i)+'.jpg',im4)
    i=i+1;
    cv2.imwrite(savepath+str(i)+'.jpg',im5)
    i=i+1
    cv2.imwrite(savepath+str(i)+'.jpg',im6)
    i=i+1
print i
    


