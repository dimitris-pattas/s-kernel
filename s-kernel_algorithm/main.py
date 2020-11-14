from edges.point import Point
from edges.edge import Edge
from input_polygon.inputPolygonByCsv import InputPolygonByCsv

def main():
    
    inputPolygon = InputPolygonByCsv('points')
    
    polygon = inputPolygon.read()

    # test input

    edgesOuter = polygon.getOuter()
    holes = polygon.getHoles()
    
    print('outer')
    for o in edgesOuter:
        print('edge')
        print(o.getPoint_1().printPoint())
        print(o.getPoint_2().printPoint())
        
    print('holes length '+str(len(holes)))
    for hole in holes:
        print('\nhole\n')
        for edge in hole:
            print('edge')
            print(edge.getPoint_1().printPoint())
            print(edge.getPoint_2().printPoint())




if __name__ == "__main__":
    main()