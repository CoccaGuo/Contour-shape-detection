# ColorBlender.py by CoccaGuo at 2021/09/29 16:44

import cv2
import numpy as np
from DataProcessor import distance


def singleLayerBlender(image, ring, contour_item, color, bg_color, k=3):
    '''draw a circle in the center of the ring, use the mid color of color and bg_color.
    '''
    center = ring.position
    distance_adder = getAvgRadius(center, contour_item)
    mid_color = tuple(
        ((np.array(list(color.value)) + np.array(list(bg_color.value)))/2).tolist())
    cv2.circle(image, center, int(distance_adder) + k, mid_color, -1)


def multiLayerBlender(image, ring, contour_item, color, bg_color, k=5):
    center = ring.position
    avg_rad = getAvgRadius(center, contour_item)
    for i in range(k-1, 0, -1):
        wanted_color = tuple(
            ((i*np.array(list(bg_color.value))/k + (1-i/k)*np.array(list(color.value)))).tolist())
        cv2.circle(image, center, avg_rad + i, wanted_color, -1)


def interpolatedBlender(image, ring, contour_item, color, bg_color, k=5, j=5):
    center = ring.position
    avg_rad = getAvgRadius(center, contour_item)
    for i in range(k-1, -j, -1):
        wanted_color = tuple(
            ((i*np.array(list(bg_color.value))/k + (1-i/k)*np.array(list(color.value)))).tolist())
        cv2.circle(image, center, avg_rad + i, wanted_color, -1)


def getAvgRadius(center, contour_item):
    distance_adder = 0
    for i in contour_item:
        distance_adder += distance(i[0], center)
    distance_adder /= len(contour_item)
    return int(distance_adder)
