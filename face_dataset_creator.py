import os
import cv2
import time

# For the algorithm to work properly around 20 photos of a person from different angles are required 


def main():
    cap = cv2.VideoCapture(0)

    run = True
    getname= True

    # No is used to track no of photos taken
    no = 0
    # Obtains path of pwd
    path = os.path.dirname(os.path.realpath(__file__)) + '\\Dataset\\'

    # Creates the dataset folder in pwd if it does not exist
    try :
        os.mkdir(path)
    except:
        print('Dataset folder exits')
    # Creates folder inside dataset with the name of the person    
    while(getname):
        name = input('Enter your name :')
        if not os.path.exists(path + name):
            os.mkdir(path + name)
            getname = False
        else:
            print('Name Taken')
    # From the devices primary camera screen shots are taken and saved in the dataset folder
    while(run):
        ret,frame = cap.read()
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(no), (600, 20), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Dataset Generator',frame)
        inputkey = cv2.waitKey(1)
        location = path + name + '\\' + str(no) + ".jpg"
        if inputkey == 27:
            run = False
        if inputkey == ord('q'):
            print(location)
            cv2.imwrite(location, frame)
            no = no + 1
    
 
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
