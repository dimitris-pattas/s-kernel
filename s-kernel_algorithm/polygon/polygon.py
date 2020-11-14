class Polygon:
    def __init__(self, outer, holes):
        self.outer = outer  
        self.holes = holes

    def addHole(self, hole):
        self.holes.push(hole)

    def getOuter(self):
        return self.outer

    def getHoles(self):
        return self.holes