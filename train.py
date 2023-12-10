import cv2,os
import numpy as np
from PIL import Image
from training import TakeImages

def check_haarcascadefile():
    exists = os.path.isfile("haar_face.xml")
    if exists:
        pass
    else:
        print("haar_cascade file missing")
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids



def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haar_face.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        print("Please Register first........")
        return
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Profile Saved Successfully"
    print(res)
    print('Total Registrations till now  : ' + str(ID[0]))
    
    
TakeImages()
check_haarcascadefile()
assure_path_exists("TrainingImageLabel/")
recognizer = cv2.face_LBPHFaceRecognizer.create()
harcascadePath = "haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(harcascadePath)
faces, ID = getImagesAndLabels("TrainingImage")
try:
    recognizer.train(faces, np.array(ID))
except:
    print("Please Register first........")
recognizer.save("TrainingImageLabel\Trainner.yml")
res = "Profile Saved Successfully"
print(res)
print('Total Registrations till now  : ' + str(ID[0]))