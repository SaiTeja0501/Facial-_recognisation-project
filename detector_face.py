import cv2
font=cv2.FONT_HERSHEY_SIMPLEX

face_cascade=cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
a=1
rollno=int(input("enter the rollno : "))
name=input("enter the name : ")
while True:
    check,frame=video.read()
   
    faces=face_cascade.detectMultiScale(frame,scaleFactor=1.05, minNeighbors=5)
    
    imageop2=frame
    cropimage=frame
    for x,y,w,h in faces:
        imageop=cv2.rectangle(frame, (x, y), (x+w,y+h), (99, 255, 3), 2)
        imageop2=cv2.putText(imageop, str("detected face"),(x+w//3,y+h+15),font,0.5,(125, 255, 255),2)
        cropimage = imageop2[y + 2:y + h - 2, x + 2:x + w - 2]
        resizeimg = cv2.resize(cropimage, (400, 400))
        
        if cropimage is frame:
            pass
        else:
            a+=1
            cv2.imwrite("detected_face/"+name+str('.')+str(rollno) +str('.')+ str(a)+ ".jpg", resizeimg)
        
    cv2.imshow("vid", imageop2)
    key=cv2.waitKey(10)
    if key==ord("q"):
        break
    elif a==100:
        break
    
video.release()
cv2.destroyAllWindows()
