# Ring.py by CoccaGuo at 2021/09/28 12:19

from itertools import combinations
from DataProcessor import distance
from utils import INF, perpendicularBisector, getCrossPoint, nMin, orderedPoints

class Ring:
    def __init__(self, position, sides, id) -> None:
        self.position = position
        self.sides = sides
        self.id = id
        self.colored = False

    def bordor(self, all_rings):
        neighbors = all_rings.findRingsByID(all_rings.nearestNeighbor(self.id))
        pb_line_list = []
        cross_point_list = []
        distance_list = []
        for ring in neighbors:
            pb_line_list.append(perpendicularBisector(self.position, ring.position))
        for combinator in combinations(pb_line_list, 2):
            cross_point_list.append(getCrossPoint(*combinator))
        for cpts in cross_point_list:
            try:
                distance_list.append(distance(self.position, cpts))
            except TypeError:
                distance_list.append(INF)
        _, indices = nMin(distance_list, self.sides)
        bordor_pts = [cross_point_list[i] for i in indices] # return bordor crossing points
        return orderedPoints(bordor_pts, self.position)
 