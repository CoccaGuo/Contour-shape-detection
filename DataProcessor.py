# DataProcessor.py by CoccaGuo at 2021/09/27 13:19
import math
from itertools import combinations


def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)


def stat_distance(points):
    _list = []
    for combinator in combinations(points, 2):
        _list.append(distance(*combinator))
    return _list
