import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
import face_recognition

read = []

def  create_data_sets():
    face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cam = cv2.VideoCapture(0)
    sample = 0
    id = 'Gajendra'
    while (True):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detect.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            sample = sample + 1
            print("Saved")
            cv2.imwrite('/users/gajendrasinghrathore/Desktop/HackathonProject/datasetFolder/' + str(id) + '.' + str(sample) + '.jpeg', gray[y:y + h,x:x + w ])
            path = '/users/gajendrasinghrathore/Desktop/HackathonProject/datasetFolder/' + str(id) + '.' + str(sample) + '.jpeg'
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            text1 = checkIfGajendra(path)
            text2 = checkIfAvinash(path)
            if text1=='Gajendra':
                final_text = 'Gajendra'
            elif text2=='Avinash':
                final_text = 'Avinash'
            else:
                final_text = 'GUEST'
            cv2.putText(img, final_text, (0, 130), font, 3, (200, 0, 155))
            plt.imshow(img)
            plt.show()
            # 50 decides the number of pics




    cam.release()
    cv2.destroyAllWindows()

def checkIfGajendra(path):
     path_of_unknown_data = path
     unknown_image_path = cropping_and_resizing_images(path_of_unknown_data)

     known_image = face_recognition.load_image_file("/users/gajendrasinghrathore/Desktop/HackathonProject/other.jpg")
     unknown_image = face_recognition.load_image_file(unknown_image_path)
     biden_encoding = face_recognition.face_encodings(known_image)[0]
     unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
     results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
     if results == [True]:
         return 'Gajendra'
     else:
         return ' '

def checkIfAvinash(path):
     path_of_unknown_data = path
     unknown_image_path = cropping_and_resizing_images(path_of_unknown_data)

     known_image = face_recognition.load_image_file("/users/gajendrasinghrathore/Desktop/HackathonProject/Avinash.jpg")
     unknown_image = face_recognition.load_image_file(unknown_image_path)
     biden_encoding = face_recognition.face_encodings(known_image)[0]
     unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
     results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
     if results == [True]:
         return 'Avinash'
     else:
         return ' '

def cropping_and_resizing_images(path):
    # set the path where u have ur cropped images
    #path = "/home/abhishek/Downloads/Hackathon 4.0 Datasets/"
    sample = 0

    sample += 1
    read_ = Image.open(path)
    basewidth = 190
    hsize = 190
    img = read_.resize((basewidth, hsize), Image.ANTIALIAS)
    # Set the path where u want the cropped image to save
    img.save('/users/gajendrasinghrathore/Desktop/HackathonProject/{}_{}.jpg'.format("check", sample))
    path_ = '/users/gajendrasinghrathore/Desktop/HackathonProject/{}_{}.jpg'.format("check", sample)
    return path_

# def converting_data_into_numpy_arrays():
#     try:
#         path = "/home/abhishek/testdatasets/abhishek"
#         for file in os.listdir(path):
#
#     except FileNotFoundError:
#         print("Wrong path for images")


if __name__ == "__main__":
    if __name__ == '__main__':
        switcher = {
            1: create_data_sets,
            2: cropping_and_resizing_images,
            }

        while True:
            menu = "\n1. Create Dataset \n2. Cropping and resizing "
            print(menu)
            choice = int(input("Print choice:"))
            func = switcher.get(choice, lambda: "Invalid choice")
            func()
