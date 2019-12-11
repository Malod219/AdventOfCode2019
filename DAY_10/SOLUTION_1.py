import math
import itertools
from collections import defaultdict
import pprint
# part 1 stuff
with open("input1.txt","r") as f:
    data = f.readlines()
points = []
for y in range(len(data)):
    for x in range(len(data[0])-1):
        if data[y][x] == '#':
            points.append([x,y])
maxSighted = 0
keyPoint = [0,0,-1]
for i in range(len(points)):
    point = points[i]
    visible = []
    for j in range(len(points)):
        if i==j:
            continue
        newPoint = points[j]
        angle = math.atan2(point[1]-newPoint[1],point[0]-newPoint[0])+math.pi
        angle = math.degrees(angle)
        if angle not in visible:
            visible.append(angle)
    if len(visible)>maxSighted:
        maxSighted=len(visible)
        keyPoint=[point[0], point[1], i]
print("Base at {}, with sight of {} asteroids".format(keyPoint, maxSighted))
# part 2
roids = defaultdict(list)
# We have to reorganise the data to consider distances too
def getDistToPoint(px, py, px2, py2):
    return math.sqrt((px-px2)**2 + (py-py2)**2)
for j in range(len(points)):
    if keyPoint[2]==j:
        continue
    newPoint = points[j]
    angle = math.atan2(keyPoint[1]-newPoint[1],keyPoint[0]-newPoint[0])+(math.pi*3/2)
    angle = math.degrees(angle)
    if angle>= 360:
        angle-=360
    roids[angle].append([newPoint, getDistToPoint(keyPoint[0], keyPoint[1], newPoint[0], newPoint[1])])
def generateKeysToIterateThrough(roids):
    keys = []
    for key in roids.keys():
        keys.append(key)
    keys.sort()
    return keys
destroyCount = 0
while destroyCount<202:
    keys = generateKeysToIterateThrough(roids)
    for key in keys:
        asteroidSelection = roids[key]
        minIndex = 0
        minDist = 99999
        for asteroid in asteroidSelection:
            if minDist > asteroid[1]:
                minIndex = asteroidSelection.index(asteroid)
                minDist = asteroid[1]
        destroyCount+=1
        if destroyCount == 200:
            print(roids[key][minIndex][0][0]*100+roids[key][minIndex][0][1])
        del roids[key][minIndex]