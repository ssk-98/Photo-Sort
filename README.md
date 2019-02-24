# Photo-Sort
Photo  sorting based on face with ML

## Step to use the above code:

1. Run dataset generator. This opens the webcam of the computer and allows you to take pictures that are used to train the face recognition model. Take about 25 pictures of the face from different angles.
2. Run enconding.py. This converts the above face into a number which is used to identify faces. The output is stored in the encoding.pickle file.
3. Run video.py to see face identification from the webcam feed.
4. Run photosort.py. Enter the location of the images to be sorted. At the code location an output folder is generated which contains photos sorted based on all the faces the model has been traiend on.
