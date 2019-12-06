with open("input1.txt","r") as f:
    data = f.readlines()
# Data Formats
# List of lines
# Lines are a list, size 2
# Line Format
#    - Index 0 = Parent
#    - Index 1 = Node
# Dict format:
#   Key   = Child Node
#   Value = Parent Node
Dict = {}
# Loop over every piece of data
for line in data:
    line = line.replace("\n","").split(")")
    check = Dict.get(line[0])
    if check is not None:
        Dict[line[0]].append(line[1])
    if check is None:
        Dict[line[0]] = [line[1]]
checkSum = 0

countingTotal = {}

def getOrbits(parentNode, count):
    countingTotal[parentNode] = count
    if Dict.get(parentNode) is not None:
        for child in Dict[parentNode]:
            getOrbits(child, count+1)

getOrbits("COM", 0)
checkSum = sum(countingTotal.values())

print(checkSum)