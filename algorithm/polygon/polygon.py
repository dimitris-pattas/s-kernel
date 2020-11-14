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

    # (x2 − x1)(y2 + y1)
    def isClockwise(self):
        sum = 0
        for edges in self.outer:
            x1 = edges.getPoint_1().getX()
            x2 = edges.getPoint_2().getX()
            y1 = edges.getPoint_1().getY()
            y2 = edges.getPoint_2().getY()
            sum = (x2 - x1) * (y2 + y1)
        return sum > 0

    def OrthogonallyConvexPolygon(self):
        start = 0
        end = len(self.outer)
        lowermost_Ndent = None
        rightmost_Wdent = None
        topmost_Sdent = None
        leftmost_Edent = None

        if (self.isClockwise()):
            print ("allagi gia aristerostrofa")
            start = len(self.outer)-1
            end = 0
        for i in range(start, end):
            neightbor_prev = i-1
            neightbor_next = i+1
            if( i==0 ):
                neightbor_prev = len(self.outer)-1
            if ( i==len(self.outer)-1 ):
                neightbor_next = 0
            # check W-dent, E-dent
            if ( self.outer[i].getPoint_1().getX() == self.outer[i].getPoint_2().getX() ):
                if ( self.outer[i].getPoint_1().getY() > self.outer[i].getPoint_2().getY() ): # down
                    if ( (self.outer[neightbor_prev].getPoint_1().getX() < self.outer[i].getPoint_1().getX()) &
                         (self.outer[neightbor_next].getPoint_2().getX() < self.outer[i].getPoint_2().getX())
                    ):
                        self.outer[i].setDescription("W-dent")
                        if (rightmost_Wdent == None):
                            rightmost_Wdent =  self.outer[i]
                        elif(rightmost_Wdent.getPoint_1().getX() < self.outer[i].getPoint_1().getX()):
                            rightmost_Wdent =  self.outer[i]
                else: # up
                    if ( (self.outer[neightbor_prev].getPoint_1().getX() > self.outer[i].getPoint_1().getX()) &
                         (self.outer[neightbor_next].getPoint_2().getX() > self.outer[i].getPoint_2().getX())
                    ):
                        self.outer[i].setDescription("E-dent")
                        if (leftmost_Edent == None):
                            leftmost_Edent =  self.outer[i]
                        elif (leftmost_Edent.getPoint_1().getX() > self.outer[i].getPoint_1().getX()):
                            leftmost_Edent =  self.outer[i]

             # check S-dent, N-dent
            if ( self.outer[i].getPoint_1().getY() == self.outer[i].getPoint_2().getY() ):
                if ( self.outer[i].getPoint_1().getX() < self.outer[i].getPoint_2().getX() ): # right
                    if ( (self.outer[neightbor_prev].getPoint_1().getY() < self.outer[i].getPoint_1().getY()) &
                         (self.outer[neightbor_next].getPoint_2().getY() < self.outer[i].getPoint_2().getY())
                    ):
                        self.outer[i].setDescription("S-dent")
                        if (topmost_Sdent == None):
                            topmost_Sdent =  self.outer[i]
                        elif (topmost_Sdent.getPoint_1().getY() < self.outer[i].getPoint_1().getY()):
                            topmost_Sdent =  self.outer[i]
                else: # left
                    if ( (self.outer[neightbor_prev].getPoint_1().getY() > self.outer[i].getPoint_1().getY()) &
                         (self.outer[neightbor_next].getPoint_2().getY() > self.outer[i].getPoint_2().getY())
                    ):
                        self.outer[i].setDescription("N-dent")
                        if (lowermost_Ndent == None):
                            lowermost_Ndent =  self.outer[i]
                        elif (lowermost_Ndent.getPoint_1().getY() > self.outer[i].getPoint_1().getY()):
                            lowermost_Ndent =  self.outer[i]

        print ("lowermost_Ndent "+str(lowermost_Ndent.getPoint_1().getY()))
       # print ("rightmost_Wdent "+str(rightmost_Wdent.getPoint_1().getX()))
        print ("topmost_Sdent "+str(topmost_Sdent.getPoint_1().getY()))
       # print ("leftmost_Edent "+str(leftmost_Edent.getPoint_1().getX()))    
        

