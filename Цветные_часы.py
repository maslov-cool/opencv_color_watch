import cv2
import numpy as np
import random
import time

img = np.zeros((1080, 1920, 3), dtype='uint8')

# RGB - стандарт
# BGR - формат в OpenCV(r, b поменять местами)
'''print('Как часто вы хотите, чтобы менялись цвета(в миллисекундах)?')
ms = int(input())'''
while True:
    img[:] = random.randint(0, 256), random.randint(0, 256), random.randint(0, 256)
    img[200:600, 560:1060] = 0, 255, 255

    cv2.putText(img, f'{time.ctime()}', (560, 400), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 0, 0), 3)

    cv2.imshow('img', img)
    if cv2.waitKey(1000) == ord('q'):
        break



