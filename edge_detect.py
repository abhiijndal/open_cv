import cv2 as cv
import numpy as np

img=cv.imread(r'C:\Users\91821\OneDrive\Pictures/baby.jpg')



gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur=cv.GaussianBlur(gray,(7,7),0)
lap=cv.Laplacian(gray,cv.CV_64F)
sobel_x=cv.Sobel(gray,cv.CV_64F,1,0)
sobel_y=cv.Sobel(gray,cv.CV_64F,0,1)
canny=cv.Canny(gray,150,170)

cv.imshow('img',sobel_x)
cv.imshow("img",sobel_y)
cv.imshow('img',canny)
cv.waitKey(0) 

