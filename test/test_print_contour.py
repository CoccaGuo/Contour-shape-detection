# test_print_contour.py by CoccaGuo at 2021/09/28 18:13

import sys
sys.path.append('./')
import cv2
import numpy as np
from DataProcessor import *
from ContourDetecter import *
from utils import Color
from RingFactoryMaker import getRingFactory


def print_color(ring, color):
    if ring.colored == False:
        pts = rf.contour_list[ring.id]
        cv2.fillConvexPoly(image, pts, color.value)
        ring.colored = True

if __name__ == '__main__':
    image_path = 'data/raw.png'
    image = cv2.imread(image_path)
    rf = getRingFactory(image)

    for ring in rf.ring_list:
        if ring.sides == 7:
            print_color(ring, Color.WHEAT)

            for nnRing in rf.findRingsByID(rf.nearestNeighbor(ring.id)):
                if nnRing.sides == 6:
                    print_color(nnRing, Color.SLATEBLUE)

        if ring.sides == 5:
            print_color(ring, Color.SEAGREEN)

            for nnRing in rf.findRingsByID(rf.nearestNeighbor(ring.id)):
                if nnRing.sides == 6:
                    print_color(nnRing, Color.SLATEBLUE)
            
        if ring.sides == 6:
            print_color(ring, Color.YELLOW)
            
    cv2.imshow("pic", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite('readme.assert/bordor1.png', image)