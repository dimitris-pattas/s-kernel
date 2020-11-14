class Edge:
    def __init__(self, point_1, point_2, description):
        self.point_1 = point_1
        self.point_2 = point_2
        self.description = description

    def getPoint_1(self):
        return self.point_1

    def getPoint_2(self):
        return self.point_2
