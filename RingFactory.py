# RingFactory.py by CoccaGuo at 2021/09/28 13:02

from Ring import Ring
from DataProcessor import distance

class RingFactory:
    def __init__(self, data_list, counter_list, refLength, shreshold=0.7) -> None:
        self.count = 0
        self.ring_list = []
        self.refLength = refLength
        self.shreshold = shreshold
        for pt, ct in zip(data_list, counter_list):
            self.ring_list.append(Ring(position=pt, sides=ct, id=self.count))
            self.count += 1

    def findRingByID(self, id: int) -> Ring:
        return self.ring_list[id]

    def findRingsByID(self, id_list):
        return [self.findRingByID(id) for id in id_list]

    def nearestNeighbor(self, id: int) -> list:
        this = self.ring_list[id]
        nn_id_list = []
        for that in self.ring_list:
            dis = distance(this.position, that.position)
            if dis/self.refLength > self.shreshold and self.refLength/dis > self.shreshold:
                nn_id_list.append(that.id)
        return nn_id_list
