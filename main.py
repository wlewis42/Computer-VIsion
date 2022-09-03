import os
import cv2
import datetime


def openCam():

    cap = cv2.VideoCapture(0)

    #Check whether user selected camera is opened successfully.

    # if not (cap.isOpened()):

    #     print("could not open")

    # ret, frame = cap.read()
    # frame = cv2.resize(frame, (640, 480))
    # cv2.imshow("test", frame)
    # cv2.waitKey(0)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()






if __name__=='__main__':

    print("Start!")
    openCam()
    
