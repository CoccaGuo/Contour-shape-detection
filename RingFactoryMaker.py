# RingFactoryMaker.py by CoccaGuo at 2021/09/28 15:00
from DataProcessor import *
from ContourDetecter import *
from RingFactory import RingFactory


def getRingFactory(image):
    binarized = binarize(image)
    contour = contour_detect(binarized)
    center_list = contour_iterator(contour)
    
    data = stat_distance(center_list)
    refLength = maxValueDicider(data)
    numberList = nearestCounter(center_list, refLength)

    rf = RingFactory(center_list, numberList, refLength)
    rf.contour_list = contour
    return rf
