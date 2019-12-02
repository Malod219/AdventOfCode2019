import copy

# Get data, and save it
with open("input1.txt","r") as f:
    data = f.readlines()[0].replace("\n","").split(',')

data = list(map(int, data))

originalMemory = copy.deepcopy(data)

# Compute with opcodes
def compute(data):
    readPoint = 0
    while(True):
        opcode = data[readPoint]
        if (opcode == 99):
            break
        elif (opcode == 1):
            data[data[readPoint+3]] = data[data[readPoint+2]]+data[data[readPoint+1]]
        elif (opcode == 2):
            data[data[readPoint+3]] = data[data[readPoint+2]]*data[data[readPoint+1]]
        else:
            print("ERROR, Invalid opcode!")
        readPoint+=4
    return data[0]
# Loop through inputs from 0-100 for both
loop = True

for i in range(100):
    for j in range(100):
        data = copy.deepcopy(originalMemory)
        data[1] = i
        data[2] = j
        # Check if it's found
        if(compute(data) == 19690720):
            print(100*i + j)
            loop = False
        if(loop==False):
            break
    if(loop==False):
        break

