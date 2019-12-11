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
