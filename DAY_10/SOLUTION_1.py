import math

with open("input1.txt","r") as f:
    data = f.readlines()
points = []

for y in range(len(data)):
    for x in range(len(data[0])):
        points.append([x,y])

# Defaults
maxSighted = 0
keyPoint = [0,0]

for i in range(len(points)):
    point = points[i]
    # We will use a dict with lengths
    # Maps ANGLE-> List[Distance, Point index]
    visible = {}
    #Find gradient, distance to(pythag) and point index
    for j in range(len(points)):
        if i==j:
            continue
        newPoint = points[j]
        for k in range(len(points)):
            if k == i or k == j:
                continue
            newPoint2 = points[k]
            # (y2-y1)(x3-x1)=(y3-y1)*(x2-x1)
            grad1 = (newPoint[1] - point[1])*(newPoint2[0]-point[0])
            grad2 = (newPoint2[1]-point[1])*(newPoint[0]-point[0])
