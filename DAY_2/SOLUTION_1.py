with open("input1.txt","r") as f:
    data = f.readlines()[0].replace("\n","").split(',')

data = list(map(int, data))

data[1] = 12
data[2] = 2

# Compute up to halt opcode
# OPCODES:
# Opcode 1(adds next 2 addresses' values and puts it in 3rd address)
# Opcode 2(multiplies next 2 addresses' values and puts it in the 3rd address)
# Opcode 99(halt)
# After reading an opcode, move opcode reading address up by 4
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
print(data[0])
