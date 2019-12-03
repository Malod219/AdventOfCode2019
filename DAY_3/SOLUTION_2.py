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
                wireSpace[currentPosY][currentPosX+i] = 1
            currentPosX += parameter
        elif(opcode == "L"):
            for i in range(parameter):
                wireSpace[currentPosY][currentPosX-i] = 1
            currentPosX -= parameter
        elif(opcode == "U"):
            for i in range(parameter):
                wireSpace[currentPosY-i][currentPosX] = 1
            currentPosY -= parameter
        elif(opcode == "D"):
            for i in range(parameter):
                wireSpace[currentPosY+i][currentPosX] = 1
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
                        wireSpace[currentPosY][currentPosX+i]=2
                        collisionPoints.append([currentPosX+i,currentPosY,99999,99999])
            currentPosX += parameter
        elif(opcode == "L"):
            for i in range(parameter):
                if(wireSpace[currentPosY][currentPosX-i] == 1):
                    if(currentPosX != centerX & currentPosY != centerY):
                        wireSpace[currentPosY][currentPosX-i]=2
                        collisionPoints.append([currentPosX-i,currentPosY,99999,99999])
            currentPosX -= parameter
        elif(opcode == "U"):
            for i in range(parameter):
                if(wireSpace[currentPosY-i][currentPosX] == 1):
                    if(currentPosX != centerX & currentPosY != centerY):
                        wireSpace[currentPosY-i][currentPosX]=2
                        collisionPoints.append([currentPosX,currentPosY-i,99999,99999])
            currentPosY -= parameter
        elif(opcode == "D"):
            for i in range(parameter):
                if(wireSpace[currentPosY+i][currentPosX] == 1):
                    if(currentPosX != centerX & currentPosY != centerY):
                        wireSpace[currentPosY+i][currentPosX]=2
                        collisionPoints.append([currentPosX,currentPosY+i,99999,99999])
            currentPosY += parameter
    except:
        print("Failed.\nOpcode: {}\nParameter: {}\nCurrent XY Coordinate: {}, {}".format(opcode, parameter, currentPosX, currentPosY))
        break;
def getStepsCountToIntersect(data,pos):
    currentPosX = centerX
    currentPosY = centerY
    steps = 0
    # Plot all wire commands in the first line
    for command in data:
        #print(command)
        opcode, parameter = command[0], int(command[1:])
        try:
            if(opcode == "R"):
                for i in range(parameter):
                    if wireSpace[currentPosY][currentPosX+i] == 2:
                        for j in range(len(collisionPoints)):
                            if( currentPosX+i == collisionPoints[j][0] and currentPosY == collisionPoints[j][1]  ):
                                collisionPoints[j][pos] = min(collisionPoints[j][pos], steps+i)

                currentPosX += parameter
            elif(opcode == "L"):
                for i in range(parameter):
                    if wireSpace[currentPosY][currentPosX-i] == 2:
                        for j in range(len(collisionPoints)):
                            if( currentPosX-i == collisionPoints[j][0] and currentPosY == collisionPoints[j][1]  ):
                                collisionPoints[j][pos] = min(collisionPoints[j][pos], steps+i)

                currentPosX -= parameter
            elif(opcode == "U"):
                for i in range(parameter):
                    if wireSpace[currentPosY-i][currentPosX] == 2:
                        for j in range(len(collisionPoints)):
                            if( currentPosX == collisionPoints[j][0] and currentPosY-i == collisionPoints[j][1]  ):
                                collisionPoints[j][pos] = min(collisionPoints[j][pos], steps+i)

                currentPosY -= parameter
            elif(opcode == "D"):
                for i in range(parameter):
                    if wireSpace[currentPosY+i][currentPosX] == 2:
                        for j in range(len(collisionPoints)):
                            if( currentPosX == collisionPoints[j][0] and currentPosY+i == collisionPoints[j][1]  ):
                                collisionPoints[j][pos] = min(collisionPoints[j][pos], steps+i)
                currentPosY += parameter
            steps+=parameter
        except:
            print("Failed.\nOpcode: {}\nParameter: {}\nCurrent XY Coordinate: {}, {}".format(opcode, parameter, currentPosX, currentPosY))
            break;

getStepsCountToIntersect(data[0],2)
getStepsCountToIntersect(data[1],3)
minSum = 99999
for point in collisionPoints:
    minSum = min(minSum, point[2]+point[3])
print(minSum)
print("Succesfully ended")
