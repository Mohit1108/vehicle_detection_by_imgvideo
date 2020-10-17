import cv2

car_cascade = cv2.CascadeClassifier('car.xml')

cap = cv2.VideoCapture('img1.jpg')

while cap.isOpened():
    flag,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 3)
    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Car Detector',img)
    cv2.waitKey(0)



