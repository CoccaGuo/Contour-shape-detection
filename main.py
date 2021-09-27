import cv2
from ContourDetecter import *
from utils import *

if __name__ == '__main__':
    image_path = 'data/raw.png'
    image = cv2.imread(image_path)
    binarized = binarize(image)
    contour = contour_detect(binarized)
    center_list = contour_iterator(contour)

    for point in center_list:
        cv2.circle(image, point, 2, RED, 4)

    cv2.imshow("pic", image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite("readme.assert/centered.png", image)