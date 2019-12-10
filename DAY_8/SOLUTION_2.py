with open("input1.txt","r") as f:
    data = f.readlines()[0]
layers=[]
for i in range(len(data)//(25*6)):
    print("On {}".format(i))
    info = data[i*25*6:i*25*6+25*6]
    print(info)
    layers.append(info)

# Get a string of appropiate length to begin manipulating
currentString = None
for layer in layers:
    if currentString == None:
        currentString = ["2" for x in range(len(layer))]
    for i in range(len(layer)):
        if currentString[i] == "2":
            currentString[i] = layer[i]
outputMessage = []

for y in range(6):
    for x in range(25):
        if currentString[x+y*25] == "1":
            outputMessage.append("#")
        else:
            outputMessage.append(" ")
    outputMessage.append("\n")
print("".join(outputMessage))



