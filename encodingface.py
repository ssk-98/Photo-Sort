from imutils import paths
import face_recognition
import pickle
import cv2
import os
import sys

def main():
        #make sure that the images to be encoded are stored in the location of the py file inside folders with folder name as the name of the person
        location = os.path.dirname(os.path.realpath(__file__)) 

        print("[INFO] quantifying faces...")
        imagePaths = list(paths.list_images(location))
        if not len(imagePaths):
                print('No images were found in the folder')
                sys.exit()

        # initialize the list of known encodings and known names
        knownEncodings = []
        knownNames = []

        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
                # extract the person name from the image path
                print("[INFO] processing image {}/{}".format(i + 1,len(imagePaths)))
                name = imagePath.split('\\')[-2]

                image = cv2.imread(imagePath)

                # detect the (x, y)-coordinates of the bounding boxes
                # corresponding to each face in the input image
                # Depending on the computers computaional capabilities you can choose hog or cnn
                boxes = face_recognition.face_locations(image,model='cnn')

                # compute the facial embedding for the face
                encodings = face_recognition.face_encodings(image, boxes)

                # loop over the encodings
                for encoding in encodings:
                        # add each encoding + name to our set of known names and
                        # encodings
                        knownEncodings.append(encoding)
                        knownNames.append(name)

        # create pickle file containing encodings and names
        print("[INFO] serializing encodings...")
        data = {"encodings": knownEncodings, "names": knownNames}
        f = open(location+'encoding.pickle', "wb")
        f.write(pickle.dumps(data))
        f.close()

if __name__ == '__main__':
        main()
