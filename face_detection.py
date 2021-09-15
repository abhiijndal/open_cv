import cv2 as cv
img= cv.imread(r"C:\Users\91821\OneDrive\Pictures/group.jpg")

#resize=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
#cv.imshow('img',resize)

gray=cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

haar_cas=cv.CascadeClassifier('haar_cas.xml')
face_react=haar_cas.detectMultiScale(gray,minNeighbors=3)
print(f'number of face detected:{len(face_react)}')
for (x,y,w,h) in face_react:

    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),thickness=2)
    
cv.imshow('detected_face',img)
cv.waitKey(0)

