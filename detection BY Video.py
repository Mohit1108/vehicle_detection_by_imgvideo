import cv2   #pip install opencv-python

carcascade = cv2.CascadeClassifier('car.xml')
cap = cv2.VideoCapture('cars3.mp4')

while cap.isOpened():
    flag,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars = carcascade.detectMultiScale(gray, 1.05, 10)
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Car Detector',img)
    cv2.waitKey(1)

u
