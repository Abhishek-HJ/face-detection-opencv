import cv2

cap=cv2.VideoCapture(0)

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:

    a,b=cap.read()

    gray=cv2.cvtColor(b,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,5)

    for(x,y,w,h) in faces:

        cv2.rectangle(b,(x,y),(x+w,y+h),(0,255,0),5)

    cv2.imshow('Face',b)


    if cv2.waitKey(1)==ord('q'):

        break
cap.release()

cv2.destroyAllWindows()    
