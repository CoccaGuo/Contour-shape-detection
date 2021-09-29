# test_neighbor.py by CoccaGuo at 2021/09/28 14:48
import sys
sys.path.append('./')
import cv2
import random
from DataProcessor import *
from ContourDetecter import *
from utils import Color
from RingFactory import RingFactory

if __name__ == '__main__':
    image_path = 'data/raw.png'
    image = cv2.imread(image_path)
    binarized = binarize(image)
    contour = contour_detect(binarized)
    center_list,_ = contour_iterator(contour)
    
    data = stat_distance(center_list)
    refLength = maxValueDicider(data)
    numberList = nearestCounter(center_list, refLength)

    rf = RingFactory(center_list, numberList, refLength)
    # selected_rings = random.choices(rf.ring_list, k=4) # show 3 rings and their neighbor
    selected_rings = rf.findRingsByID([75])
    for ring in selected_rings:
        print(ring.position)
        cv2.circle(image, ring.position, 2, Color.RED.value, 4)
        neighbor_list_id = rf.nearestNeighbor(ring.id)
        for neighbor in rf.findRingsByID(neighbor_list_id):
            print(neighbor.position)
            cv2.circle(image, neighbor.position, 2, Color.BISQUE.value, 4)
    cv2.imshow("pic", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    # cv2.imwrite('readme.assert/neighbor.png', image)