# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    
    startPoints = list()
    endPoints = list()
    
    #write your code here
    for s in segments:
        startPoints.append(s.start)
        endPoints.append(s.end)
        pass
    
    pivotPoints = list()
    
    while len(startPoints)>0:
        minEnd = min(endPoints)
        excludeStart = list()
        for h,j in enumerate(startPoints):
            if j <= minEnd:
                excludeStart.append(h)
                pivotPoints.append(endPoints[endPoints.index(minEnd)])
        startPoints = [ i for j,i in enumerate(startPoints) if j not in excludeStart]
        endPoints = [ i for j,i in enumerate(endPoints) if j not in excludeStart]
        if len(startPoints)==0:
            break
        excludeStart = list()
    
    return list(set(pivotPoints))
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')


# =============================================================================
# a = [0,1,1,1,1,2,1,3,2,4,3,4,4,4,5,5]
# a[::2]
# a[1::2]
# 
# segments = list(map(lambda x: Segment(x[0], x[1]), zip(a[::2], a[1::2])))
# 
# for i,j in zip(a[::2], a[1::2]):
#     print(i,j)
# points = list()
# 
# for s in segments:
#     points.append(s.start)
#     points.append(s.end)
#     
# type(points)
# 
# 
# b = [1,2,3,4,5]
# del b[0,2]
# 
# segments = list(map(lambda x: Segment(x[0], x[1]), zip(a[::2], a[1::2])))
# print(segments)
# optimal_points(segments)
# 
# =============================================================================






