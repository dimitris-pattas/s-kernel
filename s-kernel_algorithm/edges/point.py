class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def printPoint(self):
        return('( ' + str(self.x) + ',' + str(self.y) + ' )')