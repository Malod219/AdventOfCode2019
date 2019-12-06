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

def getNodeParentFromNode(nodeToFind):
    for key, value in Dict.items():
        if nodeToFind in value:
            return key

def generateFromNode(nodeStart):
    nodes = {}
    count = 0
    currentNode = nodeStart
    while currentNode != "COM":
        nodes[count] = currentNode
        count += 1
        currentNode = getNodeParentFromNode(currentNode)
    return nodes
youTravel = generateFromNode("YOU")
sanTravel = generateFromNode("SAN")
youPointOfIntersect = 0
sanPointOfIntersect = 0
for key, value in youTravel.items():
    if value in sanTravel.values():
        youPointOfIntersect = key
        break
for key, value in sanTravel.items():
    if value in youTravel.values():
        sanPointOfIntersect = key
        break
print("Node at sanPointOfIntersect({}) is {}".format(sanPointOfIntersect, sanTravel[sanPointOfIntersect]))
print("Node at youPointOfIntersect({}) is {}".format(youPointOfIntersect, youTravel[youPointOfIntersect]))
# Magic number 2. We want to get to the point San is orbiting(remove 1 for San's position), and we need to ignore our own ship
# as a satellite(remove 1 more)
print("Jumps to get there = {}".format(youPointOfIntersect+sanPointOfIntersect - 2))