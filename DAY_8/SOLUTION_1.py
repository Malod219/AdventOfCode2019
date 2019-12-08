with open("input1.txt","r") as f:
    data = f.readlines()[0]
layers=[]
for i in range(len(data)//(25*6)):
    print("On {}".format(i))
    info = data[i*25*6:i*25*6+25*6]
    print(info)
    layers.append(info)

minCount = 999999
minIndex = -1
for i in range(len(layers)):
    layer = layers[i]
    count = layer.count("0")
    if count<minCount:
        minCount = count
        minIndex = i
print(minIndex)

layer = layers[minIndex]
print(layer.count("1")*layer.count("2"))
