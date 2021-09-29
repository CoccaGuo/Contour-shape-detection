# test.py by CoccaGuo at 2021/09/27 12:47
import sys
sys.path.append('./')
import cv2
from ContourDetecter import *
from utils import *

if __name__ == '__main__':
    image_path = 'data/raw.png'
    image = cv2.imread(image_path)
    binarized = binarize(image)
    contours = contour_detect(binarized)

    # cv2.drawContours(image=image, contours=contours,
    #  contourIdx=30, color=RED, thickness=2, lineType=cv2.LINE_AA)

    point, _ = calc_center(contours[30])
    pt_list = []
    for item in contours[30]:
        pt_list.append((item[0], item[1]))
    for point in pt_list:
        cv2.circle(image, point, 1, Color.RED.value, 4)

    cv2.imshow("pic", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
