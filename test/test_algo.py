# test_algo.py by CoccaGuo at 2021/09/27 13:22
# from itertools import combinations
import sys
sys.path.append('./')
import cv2
import matplotlib.pyplot as plt
from collections import Counter
from ContourDetecter import *
from DataProcessor import *

if __name__ == '__main__':
    image_path = 'data/raw.png'
    image = cv2.imread(image_path)
    binarized = binarize(image)
    contours = contour_detect(binarized)
    points = contour_iterator(contours)
    data = stat_distance(points)
    ind = dice_dealer(data)
    c = Counter(ind)
    print(c.most_common(10))
    length = maxValueDicider(data)
    print(length)
    # plt.hist(data, 400)
    # plt.show()



