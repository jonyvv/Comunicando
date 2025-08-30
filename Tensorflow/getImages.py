import cv2 #open cv
import os
import time
import uuid

import os
IMAGES_PATH = 'Tensorflow/workspace/images/collectedimages'
labels = ['hello','thanks','yes','no','iloveyou']
number_imgs = 5

for label in labels:
    os.makedirs(r"Tensorflow\workspace\images\collectedimages\\" + label, exist_ok=True)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    count = 0
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
        if ret and frame is not None and frame.size != 0:
            cv2.imwrite(imagename, frame)
            cv2.imshow('frame', frame)
            count += 1
        else:
            print("No se capturó imagen")
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print(f"Se capturaron {count} imágenes para la etiqueta: {label}")
    cap.release()
