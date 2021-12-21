import cv2
face_cascade=cv2.CascadeClassifier("haarcascade\haarcascade_frontalface_default.xml")
video=cv2.VideoCapture(0)
i=0
while True:
    check,frame=video.read()
    faces=face_cascade.detectMultiScale(frame)
    output_img=frame
    for x,y,w,h in faces:
        output_img=cv2.rectangle(frame,(x,y),(x+w,y+h),(19, 76, 102),2)
    
    
    cv2.imshow("mypic",output_img)
    key=cv2.waitKey(1)
    print(key)
    if key==27:
        
        break
    elif key==ord("c"):
        cv2.imwrite("mypic"+str(i)+".jpg",frame[y+2:y+h-2,x+2:x+w-2])
        i+=1
        
   
cv2.destroyAllWindows()
video.release()
