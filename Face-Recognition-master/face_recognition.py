# Import OpenCV2 for image processing
import cv2
import attendanceDB
import sqlite3 as db
from time import sleep
# Import numpy for matrices calculations
import numpy as np

import os
count = 0
li = []

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("trainer/")

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Database
con = db.connect("project.db")

l=0
# Loop
while (l <4):

    # Initialize and start the video frame capture
    cam = cv2.VideoCapture(0)

    for i in range (1,50):
        # Read the video frame
        ret, im = cam.read()

    cv2.imwrite("User"+str(l)+".jpg", im)

    # Stop the camera
    cam.release()

    #Static Image
    #im = cv2.imread("User.jpg")


    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:
        # Recognize the face belongs to which ID
        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        confi = round(100 - confidence, 2)
        print(confi)
        if  confi > 35  :
            if (Id in li):
                attendanceDB.inc(Id)
                print(Id)
            else:
                attendanceDB.enter(Id)
                li.append(Id)
            a = set(li)
            i = list(a)

    """
    for o in range(0,count):
        # Create rectangle around the face
        cv2.rectangle(im, (x - 20, y - 20), (x + w + 20, y + h + 20), (0, 255, 0), 4)
        # Find NAme
        name = con.execute("Select * from Users where id = ?", (Id,))
        data = name.fetchall()
        # Check the ID if exist
        Id = "{1} {0:.2f}%".format(round(100 - confidence, 2), data[0][1])

        # Put text describe who is in the picture
        cv2.rectangle(im, (x - 22, y - 90), (x + w + 22, y - 22), (0, 255, 0), -1)
        cv2.putText(im, str(Id), (x, y - 40), font, 1, (255, 255, 255), 3)     """

    # Display the video frame with the bounded rectangle
    #cv2.imshow('im',im)
    l = l+1
    sleep(2)
    # If 'q' is pressed, close program
    #if cv2.waitKey(10) & 0xFF == ord('q'):
     #    break


# Close all windows
cv2.destroyAllWindows()
