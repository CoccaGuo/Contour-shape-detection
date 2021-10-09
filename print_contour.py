# test_print_contour.py by CoccaGuo at 2021/09/28 18:13

import cv2
import numpy as np
from DataProcessor import *
from ContourDetecter import *
from utils import Color
from ColorBlender import *
from RingFactoryMaker import getRingFactory


def result_plot(image_path: str):
    def print_color(ring, color):
        if ring.colored == False:
            ring.colored = True
            pts = rf.contour_list[ring.id]
            # singleLayerBlender(image, ring, rf.contour_list[ring.id], color, Color.BG_COLOR, k=3)
            multiLayerBlender(image, ring, rf.contour_list[ring.id], color, Color.BG_COLOR, k=4)
            cv2.fillConvexPoly(image, pts, color.value)
        

    image = cv2.imread(image_path)
    rf = getRingFactory(image)

    for ring in rf.ring_list:

        if ring.sides == 7:
            print_color(ring, Color.SLATEBLUE)

            for nnRing in rf.findRingsByID(rf.nearestNeighbor(ring.id)):
                if nnRing.sides == 6:
                    print_color(nnRing, Color.IVORY)

        if ring.sides == 5:
            print_color(ring, Color.WHEAT)

            for nnRing in rf.findRingsByID(rf.nearestNeighbor(ring.id)):
                if nnRing.sides == 6:
                    print_color(nnRing, Color.IVORY)
                
                
        if ring.sides == 6:
            flag = True
            for nnRing in rf.findRingsByID(rf.nearestNeighbor(ring.id)):
                if nnRing.sides != 6:
                    flag = False
            if flag:
                print_color(ring, Color.YELLOW)
        
        # cv2.putText(image, str(ring.id), ring.position, cv2.FONT_HERSHEY_SIMPLEX, 0.4, Color.RED.value)
         
    cv2.imshow("pic", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    # cv2.imwrite('readme.assert/repaired_bordor.png', image)

if __name__ == '__main__':
    image_path = 'data/raw.png'
    result_plot(image_path)