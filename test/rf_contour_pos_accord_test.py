# rf_contour_pos_accord_test.py by CoccaGuo at 2021/09/29 16:20

import sys
sys.path.append('./')
import cv2
import random
import numpy as np
from DataProcessor import *
from ContourDetecter import *
from utils import Color
from RingFactoryMaker import getRingFactory


def print_color(ring, color):
    if ring.colored == False:
        ring.colored = True
        pts = rf.contour_list[ring.id]
        cv2.fillConvexPoly(image, pts, color.value)

if __name__ == '__main__':
    image_path = 'data/raw.png'
    image = cv2.imread(image_path)
    rf = getRingFactory(image)

    for ring in random.choices(rf.ring_list, k=10):
        print_color(ring, Color.BISQUE)
        cv2.putText(image, str(ring.id), ring.position, cv2.FONT_HERSHEY_SIMPLEX, 0.4, Color.RED.value)
    
    cv2.imshow("pic", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite('readme.assert/rf_contour_pos_accord_check.png', image) 

