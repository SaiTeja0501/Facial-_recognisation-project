import cv2
from PIL import Image
import os
import numpy as np


def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainner.yml")
    harcascadePath="haarcascade/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    cam = cv2.VideoCapture(0)
    
    font = cv2.FONT_HERSHEY_SIMPLEX

    tt='' 
    while True:
        ret,im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            
            conf=int(conf)
            Id=int(Id)
            print(Id, conf)
            if(30< conf <300):
                
              
                if Id==301:
                    nam='Nithya'
                    tt=str(Id)+"-"+nam
               
                    
                elif Id==300:
                    nam='ppr'
                    tt=str(Id)+"-"+nam
                elif Id==1:
                    nam='sai'
                    tt=str(Id)+"-"+nam
                
             
            elif(conf>300 or conf<30):
                Id='Unknown'                
                tt=str(Id)
                
                    
            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
                    
        cv2.imshow('image Detected',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
            
    cam.release()
    cv2.destroyAllWindows()
TrackImages()
