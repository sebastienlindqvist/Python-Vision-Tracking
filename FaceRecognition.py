import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(r'C:\Users\SebastienL\Dropbox\Code\Python\CameraStuff\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\SebastienL\Dropbox\Code\Python\CameraStuff\haarcascade_eye.xml')
#https://github.com/opencv/opencv/tree/master/data/haarcascades

cap = cv2. VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap. read()
    # Convert into grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]


        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



    cv2. imshow('webcam feed' , frame)

    if cv2.waitKey(10) & 0xFF == ord("q"): 
        break 
cap.release() 
cv2.destroyAllWindows() 