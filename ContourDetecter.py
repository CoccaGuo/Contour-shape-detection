# ContourDetecter.py by CoccaGuo at 2021/09/27 12:12
import cv2
import numpy as np


def binarize(image: np.uint8):
    _, _, selected = cv2.split(image)
    contours3, _ = cv2.findContours(
        image=selected, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    empty_back = np.zeros(image.shape)
    cv2.drawContours(image=empty_back, contours=contours3, contourIdx=-1,
                     color=(255, 255, 255), thickness=-1, lineType=cv2.LINE_AA)
    empty_back = empty_back.astype(np.uint8)
    empty_back = cv2.cvtColor(empty_back, cv2.COLOR_RGB2GRAY)
    empty_back = cv2.bitwise_not(empty_back.copy())
    return empty_back


def contour_detect(binarized: np.uint8):
    binarized = cv2.GaussianBlur(binarized, (5, 5), 0)
    ret, thresh = cv2.threshold(binarized, 150, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(
        image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
    return contours


def calc_center(contour_item):
    x = y = 0
    for i in contour_item:
        x += i[0][0]
        y += i[0][1]
    x_c = int(x/len(contour_item))
    y_c = int(y/len(contour_item))
    return (x_c, y_c)


def contour_iterator(contour):
    _list = []
    for item in contour:
        point = calc_center(item)
        _list.append(point)
    return _list
