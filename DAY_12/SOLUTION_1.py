import math

with open("input1.txt","r") as f:
    data = f.readlines()

class Planet:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.velX = 0
        self.velY = 0
        self.velZ = 0

    def doTimeStep(self):
        self.x+=self.velX
        self.y+=self.velY
        self.z+=self.velZ

    def getKE(self):
        return abs(self.velX)+abs(self.velY)+abs(self.velZ)
    def getPE(self):
        return abs(self.x)+abs(self.y)+abs(self.z)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getVelX(self):
        return self.velX

    def getVelY(self):
        return self.velY

    def getVelZ(self):
        return self.velZ

    def applyGravity(self, planets):
        for planet in planets:
            if planet.getX()>self.x:
                self.velX+=1
            elif planet.getX()<self.x:
                self.velX-=1

            if planet.getY()>self.y:
                self.velY+=1
            elif planet.getY()<self.y:
                self.velY-=1

            if planet.getZ()>self.z:
                self.velZ+=1
            elif planet.getZ()<self.z:
                self.velZ-=1

    def getData(self):
        return (self.x, self.y, self.z, self.velX, self.velY, self.velZ)

planets = []
for line in data:
    line = line.replace("<","").replace(">","").replace("x=","").replace("y=","").replace("z=","").split(",")
    planets.append(Planet(int(line[0]), int(line[1]), int(line[2]) ))
step = 0
while step < 1001:
    energyCount = 0
    step+=1
    for planet in planets:
        planet.applyGravity(planets)
    for planet in planets:
        planet.doTimeStep()
    for planet in planets:
        energyCount+=planet.getKE()*planet.getPE()
    print("Step {}, ENERGY: {}".format(step, energyCount))
# Part 2

def findPosition(planets, index):
    step = 0
    positionsPast = set()
    while True:
        step+=1
        for planet in planets:
            planet.applyGravity(planets)
        for planet in planets:
            planet.doTimeStep()
        positions = []
        for planet in planets:
            if index == 0:
                positions.append(planet.getX())
                positions.append(planet.getVelX())
            if index == 1:
                positions.append(planet.getY())
                positions.append(planet.getVelY())
            if index == 2:
                positions.append(planet.getZ())
                positions.append(planet.getVelZ())
        value = (positions[0], positions[1], positions[2], positions[3], positions[4], positions[5])
        if value in positionsPast:
            return step-1
        else:
            positionsPast.add(value)
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

planets = []
step = 0
for line in data:
    line = line.replace("<","").replace(">","").replace("x=","").replace("y=","").replace("z=","").split(",")
    planets.append(Planet(int(line[0]), int(line[1]), int(line[2]) ))
step = 0
planetDict = {}
end = False
xRep = findPosition(planets, 0)
yRep = findPosition(planets, 1)
zRep = findPosition(planets, 2)
print("XReps at {}, YReps at {}, ZReps at {}".format(xRep, yRep, zRep))
print(lcm(lcm(xRep,yRep),zRep))
