# USAGE
# python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png 

# import the necessary packages
import face_recognition
import argparse
import pickle
import cv2
import matplotlib.pyplot as plt
import os


def main():

    location = os.path.dirname(os.path.realpath(__file__))
    
    cap = cv2.VideoCapture(1)


    # load the known faces and embeddings
    print("[INFO] loading encodings...")
    data = pickle.loads(open(location+'\\encoding.pickle', "rb").read())

    run = True
    while(run):
    # read image from the primary camera of the device
        ret,image = cap.read()
        font = cv2.FONT_HERSHEY_SIMPLEX

        inputkey = cv2.waitKey(1)

        if inputkey == 27:
            run = False


        # detect the (x, y)-coordinates of the bounding boxes corresponding
        # to each face in the input image, then compute the facial embeddings
        # for each face
        # Depending on the computational capability you can use hog or cnn
        boxes = face_recognition.face_locations(image,
        model='cnn')
        encodings = face_recognition.face_encodings(image, boxes)

        # initialize the list of names for each face detected
        names = []

        # loop over the facial embeddings
        for encoding in encodings:
	# attempt to match each face in the input image to our known
	# encodings
            matches = face_recognition.compare_faces(data["encodings"],
		encoding,tolerance = 0.45)
            name = "Unknown"

	# check to see if we have found a match
            if True in matches:
		# find the indexes of all matched faces then initialize a
		# dictionary to count the total number of times each face
		# was matched
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

		# loop over the matched indexes and maintain a count for
		# each recognized face face
                    for i in matchedIdxs:
                            name = data["names"][i]
                            counts[name] = counts.get(name, 0) + 1

		# determine the recognized face with the largest number of
		# votes (note: in the event of an unlikely tie Python will
		# select first entry in the dictionary)
                    name = max(counts, key=counts.get)
	
	# update the list of names
            names.append(name)

        # loop over the recognized faces
        for ((top, right, bottom, left), name) in zip(boxes, names):
	# draw the predicted face name on the image
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
		0.75, (0, 255, 0), 2)

        cv2.imshow('output', image)
# show the output image


    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
