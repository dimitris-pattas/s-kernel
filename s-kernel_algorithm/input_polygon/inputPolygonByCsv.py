from edges.point import Point
from edges.edge import Edge
from polygon.polygon import Polygon

import csv

class InputPolygonByCsv:
    def __init__(self, name):
        self.name = name
        
    def read(self):        
        with open('/home/dp/Desktop/degree/s-kernel/input_polygon/points.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            outerFlag = True
           
            # points
            pointsOuter = []
            pointsHole = []
            holesList = []
           
            # edges
            edgesOuter = []
            hole = []
            holes = []
           
            # set points
            for row in reader:
                if ( (row['x'] == '-') & (row['y'] == '-') ):
                    if len(pointsHole) > 0 :
                        holesList.append(pointsHole)
                        pointsHole = []
                        
                    outerFlag = False
                    continue
                if( outerFlag ):
                    pointsOuter.append(Point(int(row['x']), int(row['y'])))
                else:
                    pointsHole.append(Point(int(row['x']), int(row['y'])))

            
            if  ( len(pointsOuter) % 2 == 1 ) & ( len(pointsOuter) > 4 ) :
                print ("number of outer's vertices must be even and more than 4")
                exit()
            for h in holesList:
                 if  ( len(h) % 2 == 1 ) & ( len(h) > 4 ) :
                    print ("number of hole's vertices must be even and more than 4")
                    exit()
            
            # set edges
            for i in range(1, len(pointsOuter)+1, 1):
                if (i == len(pointsOuter)):
                    edgesOuter.append( Edge(pointsOuter[i-1], pointsOuter[0], 'simple') )
                    break
                edgesOuter.append( Edge(pointsOuter[i-1], pointsOuter[i], 'simple') )

            
            for holeList in holesList: 
                for i in range(1, len(holeList)+1, 1):
                    if (i == len(holeList)):
                        hole.append( Edge(holeList[i-1], holeList[0], 'simple') )
                        break
                    hole.append( Edge(holeList[i-1], holeList[i], 'simple') )
                holes.append(hole)
                hole = []
            
            # testing input
            # print('outer')
            # for o in edgesOuter:
            #     print('edge')
            #     print(o.getPoint_1().printPoint())
            #     print(o.getPoint_2().printPoint())
             
            # print('holes length '+str(len(holes)))
            # for hole in holes:
            #     print('\nhole\n')
            #     for edge in hole:
            #         print('edge')
            #         print(edge.getPoint_1().printPoint())
            #         print(edge.getPoint_2().printPoint())

            return Polygon(edgesOuter, holes)

            
            