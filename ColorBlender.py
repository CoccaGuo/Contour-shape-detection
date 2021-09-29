# ColorBlender.py by CoccaGuo at 2021/09/29 16:44

from utils import Color
import cv2
import numpy as np
from DataProcessor import distance

def blender(image, contour_item, color, k=3):
    x = y = 0
    for i in contour_item:
        x += i[0][0]
        y += i[0][1]
    x_c = int(x/len(contour_item))
    y_c = int(y/len(contour_item))
    distance_adder = 0
    for i in contour_item:
        distance_adder += distance(i[0], (x_c, y_c))
    distance_adder /= len(contour_item)
    mid_color = tuple(np.aslist((np.array(list(color.value)) + np.array(list(Color.BG_COLOR.value)))/2))
    cv2.circle(image, (x_c, y_c), distance_adder+k,mid_color)
