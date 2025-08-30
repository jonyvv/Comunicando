import cv2 #open cv
import os
import time
import uuid

IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'
labels = ['hello','thanks','yes','no','iloveyou']
number_imgs = 15

for label in labels:
    os.mkdir("Tensorflow\\workspace\\images\collectedimages\\"+label)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range (number_imgs):
        ret,frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)

        if cv2.waitkey(1) and 0xFF == ord('q'):
            break
        cap.release()
