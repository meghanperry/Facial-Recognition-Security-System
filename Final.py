import numpy as np
import cv2
import glob

cap = cv2.VideoCapture(0)
database = []

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
for file in glob.glob('C:\Users\megan\Desktop/faces/*.jpg'):
    im = cv2.imread(file)
    database.append(im)



while(cap.isOpened()):
    ret, frame = cap.read()


    for face in database:

        # get face's dimensions
        (faceH, faceW) = face.shape[:2]

        # find the face in the frame using Template Matching
        result = cv2.matchTemplate(frame, face, cv2.TM_CCOEFF_NORMED)
        (_, max_val, min_loc, max_loc) = cv2.minMaxLoc(result)
        top_left = max_loc

        if max_val>=0.65:
            print max_val

            # extract face from the image
            topLeft = max_loc
            botRight = (topLeft[0] + faceW, topLeft[1] + faceH)
            roi = frame[topLeft[1]:botRight[1], topLeft[0]:botRight[0]]


                # Put a red border around face
            RED = [0, 0, 255]
            constant = cv2.copyMakeBorder(roi, 4, 4, 4, 4, cv2.BORDER_CONSTANT, value=RED)
            face_box = cv2.resize(constant, (faceW, faceH))

                # put face back in the image
            frame[topLeft[1]:botRight[1], topLeft[0]:botRight[0]] = face_box
            break

    if ret==True:

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()