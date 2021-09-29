# main.bak01.py by CoccaGuo at 2021/09/28 13:07

from DataProcessor import *
import cv2
from ContourDetecter import *
from utils import Color

if __name__ == '__main__':
    image_path = 'data/raw.png'
    image = cv2.imread(image_path)
    binarized = binarize(image)
    contour = contour_detect(binarized)
    center_list,_ = contour_iterator(contour)
    
    data = stat_distance(center_list)
    refLength = maxValueDicider(data)
    numberList = nearestCounter(center_list, refLength)

    for point, num in zip(center_list, numberList):
        cv2.circle(image, point, 2, Color.BISQUE.value, 4)
        cv2.putText(image, str(num), point, cv2.FONT_HERSHEY_SIMPLEX, 0.6, Color.RED.value)

    cv2.imshow("pic", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    # cv2.imwrite("readme.assert/counted_result.png", image)