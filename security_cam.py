import cv2 as cv
import winsound
cam=cv.VideoCapture(0)

while cam.isOpened():

    ret,frame1=cam.read()
    ret,frame2=cam.read()

    dff=cv.absdiff(frame1,frame2)
    gray=cv.cvtColor(dff,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),0)

    _,thresh=cv.threshold(blur,20,255,cv.THRESH_BINARY)
    dilate=cv.dilate(thresh,None,iterations=2)
    contour,_ =cv.findContours(dilate,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
   
    for i in contour:
        if cv.contourArea(i)<5000:
            continue
        x,y,w,h=cv.boundingRect(i)
        cv.rectangle(frame1,(x,y),(x+w,y+h),(0,0,255),2)
        
        winsound.Beep(500,300)
        
      
    
    if cv.waitKey(10)==ord('q'):
        break


    cv.imshow('cam',frame1)
    print(frame1)
    
