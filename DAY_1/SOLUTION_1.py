inputFile = str(input("Input file"))
f = open(inputFile,"r")
data = f.readlines()
f.close()

runningFuelSum = 0

for line in data:
    line = line.replace("\n","")
    mass = int(line)
    fuelNeeded = (mass//3)-2
    runningFuelSum += fuelNeeded

print(runningFuelSum)