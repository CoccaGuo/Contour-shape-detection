# utils.py by CoccaGuo at 2021/09/27 12:28
from enum import Enum
import cmath, math
import heapq

# should bigger than the biggest distance in the picture
INF = 1000

# I want to use it, but it's too late.
def getInfPoint(image):
    x, y, _ = image.shape
    return int(2*math.sqrt(x*x + y*y))

# some colors
class Color(Enum):
    # RGB => BGR
    RED = (0, 0, 255)
    BLUE = (255, 0, 0)
    GREEN = (0, 255, 0)
    BISQUE = (196, 228, 255)
    SLATEBLUE = (205, 90, 106)
    SEAGREEN = (87, 139, 46)
    YELLOW = (0, 255, 255)
    WHEAT = (179, 222, 245)
    PURPLE = (240, 32, 160)
    IVORY = (240, 255, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)


# deal with lines
# utils.py by CoccaGuo at 2021/09/28 13:30
def perpendicularBisector(pt1, pt2):
    # return 2 points on the line
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    # special lines
    if x1 == x2:
        return [x1, (y1+y2)/2, x1+1, (y1+y2)/2]
    if y1 == y2:
        return [(x1+x2)/2, y1, (x1+x2)/2, y1+1]
    mx, my = (x1+x2)/2, (y1+y2)/2
    k = (y1-y2)/(x1-x2)
    kk = -1/k
    return [mx, my, mx+1, my+kk]


def reformatLine(x0, y0, x1, y1):
    a = y0 - y1
    b = x1 - x0
    c = x0*y1 - x1*y0
    return a, b, c


def getCrossPoint(line1, line2):
    a0, b0, c0 = reformatLine(*line1)
    a1, b1, c1 = reformatLine(*line2)
    D = a0 * b1 - a1 * b0
    if D == 0:
        return None
    x = (b0 * c1 - b1 * c0) / D
    y = (a1 * c0 - a0 * c1) / D
    return (x, y)


# utils.py by CoccaGuo at 2021/09/28 14:43
# return n-min and their indices
def nMin(_list, n):
    min_number = heapq.nsmallest(n, _list)
    min_index = []
    for t in min_number:
        index = _list.index(t)
        min_index.append(index)
        _list[index] = INF
    return min_number, min_index


# utils.py by CoccaGuo at 2021/09/28 16:23
# deal with angles and their sequences
def orderedPoints(point_list, center):
    angle_list = []
    for point in point_list:
        phase = cmath.phase(complex(point[0]-center[0], point[1]-center[1]))
        if phase < 0:
            phase += 2*math.pi
        angle_list.append(phase)
    zipped = list(zip(angle_list, point_list))
    zipped.sort(key=lambda x: x[0])
    sorted = list(zip(*zipped))[1]
    return sorted

