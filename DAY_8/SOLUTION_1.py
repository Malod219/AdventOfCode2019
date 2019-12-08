with open("input1.txt","r") as f:
    data = f.readlines()[0]
layers=[]
for i in range((25*6)//len(data)):
    layerToAdd = []
    for j in range(25*6):
        layerToAdd.append(data[j])
    layers.append(layerToAdd)

minCount = 999999
minIndex = -1
for i in range(len(layers)):
    layer = layers[i]
    count = 0
    for character in layer:
        if int(character) == 0:
            count+=1
    if count<minCount:
        minCount = count
        minIndex = i
print(minIndex)

layerToCalculate = layers[minIndex]
twoCount = 0
oneCount = 0
for character in layer:
    if int(character) == 1:
        oneCount+=1
    if int(character) == 2:
        twoCount+=1
print(oneCount*twoCount)