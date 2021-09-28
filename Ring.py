# Ring.py by CoccaGuo at 2021/09/28 12:19

from itertools import combinations
from RingFactory import RingFactory
from DataProcessor import distance
from utils import perpendicularBisector, getCrossPoint

class Ring:
    def __init__(self, position, sides, id) -> None:
        self.position = position
        self.sides = sides
        self.id = id

    def bordor(self, all_rings: RingFactory):
        neighbors = all_rings.findRingsByID(all_rings.nearestNeighbor(self.id))
        pb_line_list = []
        cross_point_list = []
        distance_list = []
        for ring in neighbors:
            pb_line_list.append(perpendicularBisector(self.position, ring.position))
        for combinator in combinations(pb_line_list, 2):
            cross_point_list.append(getCrossPoint(*combinator))
        for cpts in cross_point_list:
            distance_list.append(distance(self.position, cpts))
