# test_bordor.py by CoccaGuo at 2021/09/28 15:28
import sys
sys.path.append('./')
import cv2
import random
import numpy as np
from DataProcessor import *
from ContourDetecter import *
from utils import Color
from RingFactoryMaker import getRingFactory

if __name__ == '__main__':
    image_path = 'data/raw.png'
    image = cv2.imread(image_path)
    rf = getRingFactory(image)
    selected_rings = random.choices(rf.ring_list, k=3) # show 3 rings and their neighbor

    for ring in selected_rings:
        pts = ring.bordor(rf)
        pts = np.asarray(pts, dtype=int)
        cv2.fillConvexPoly(image, pts, Color.WHEAT.value)
    cv2.imshow("pic", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    # cv2.imwrite('readme.assert/bordor.png', image)