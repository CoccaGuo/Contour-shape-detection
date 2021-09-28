# DataProcessor.py by CoccaGuo at 2021/09/27 13:19
import math
from itertools import combinations
from collections import Counter


def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)


def stat_distance(points):
    _list = []
    for combinator in combinations(points, 2):
        _list.append(distance(*combinator))
    return sorted(_list)


def dice_dealer(data_list, space=1):
    indices = [int(x)//space for x in data_list]
    return indices


def maxValueDicider(data_list):
    indices = dice_dealer(data_list)
    counter = Counter(indices)
    _min = 400
    for item in counter.most_common(8):
        _min = min(item[0], _min)
    return _min


def nearestCounter(points, refLength, shreshold=0.7):
    _list = []
    for point in points:
        counter = 0
        for oPoint in points:
            dis = distance(point, oPoint)
            if dis/refLength > shreshold and refLength/dis > shreshold:
                counter += 1
        _list.append(counter)
    return _list



