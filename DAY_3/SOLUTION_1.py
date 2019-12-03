with open("input1.txt","r") as f:
    data = f.readlines()
data[0] = data[0].split(',')
data[1] = data[1].split(',')

# Might need to change w if too big
w = 22000
h = w
# 2000x2000 Wirespace
wireSpace = [[0 for x in range(w)] for y in range(h)]

centerX = w//2
centerY = h//2

currentPosX = centerX
currentPosY = centerY

# Plot all wire commands in the first line
for command in data[0]:
    #print(command)
    opcode, parameter = command[0], int(command[1:])
    try:
        if(opcode == "R"):
            for i in range(parameter):
                wireSpace[currentPosY][currentPosX+i+1] = 1
            currentPosX += parameter
        elif(opcode == "L"):
            for i in range(parameter):
                wireSpace[currentPosY][currentPosX-i-1] = 1
            currentPosX -= parameter
        elif(opcode == "U"):
            for i in range(parameter):
                wireSpace[currentPosY-i-1][currentPosX] = 1
            currentPosY -= parameter
        elif(opcode == "D"):
            for i in range(parameter):
                wireSpace[currentPosY+i+1][currentPosX] = 1
            currentPosY += parameter
    except:
        print("Failed.\nOpcode: {}\nParameter: {}\nCurrent XY Coordinate: {}, {}".format(opcode, parameter, currentPosX, currentPosY))
        break;
currentPosX = centerX
currentPosY = centerY
collisionPoints = []

for command in data[1]:
    #print(command)
    opcode, parameter = command[0], int(command[1:])
    try:
        if(opcode == "R"):
            for i in range(parameter):
                if(wireSpace[currentPosY][currentPosX+i] == 1):
                    if(currentPosX != centerX & currentPosY != centerY):
                        collisionPoints.append([currentPosX+i, currentPosY])
            currentPosX += parameter
        elif(opcode == "L"):
            for i in range(parameter):
                if(wireSpace[currentPosY][currentPosX-i] == 1):
                    if(currentPosX != centerX & currentPosY != centerY):
                        collisionPoints.append([currentPosX-i, currentPosY])
            currentPosX -= parameter
        elif(opcode == "U"):
            for i in range(parameter):
                if(wireSpace[currentPosY-i][currentPosX] == 1):
                    if(currentPosX != centerX & currentPosY != centerY):
                        collisionPoints.append([currentPosX, currentPosY-i])
            currentPosY -= parameter
        elif(opcode == "D"):
            for i in range(parameter):
                if(wireSpace[currentPosY+i][currentPosX+i] == 1):
                    if(currentPosX != centerX & currentPosY != centerY):
                        collisionPoints.append([currentPosX, currentPosY+i])
            currentPosY += parameter
    except:
        print("Failed.\nOpcode: {}\nParameter: {}\nCurrent XY Coordinate: {}, {}".format(opcode, parameter, currentPosX, currentPosY))
        break;
distances = 9223372036854775807
for point in collisionPoints:
    distance = 0
    if(point[0] > centerX):
        distance += point[0]-centerX
    else:
        distance += centerX-point[0]

    if(point[1] > centerY):
        distance+= point[1]-centerY
    else:
        distance+= centerY-point[1]
    distances = min(distances, distance)

print(distances)

print("Succesfully ended")
print(collisionPoints)
