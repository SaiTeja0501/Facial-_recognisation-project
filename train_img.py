import cv2
from PIL import Image
import os
import numpy as np
def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f)for f in os.listdir(path)] 
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        print(Id)
        Ids.append(Id)        
    return faces,Ids

def trainimage():
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    harcascadePath ="haarcascade/haarcascade_frontalface_default.xml" 
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("detected_face")
    recognizer.train(faces, np.array(Id))
    recognizer.save("Trainner.yml")


trainimage()
