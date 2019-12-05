import copy
from enum import Enum

class Opcodes(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JTRUE = 5
    JFALSE = 6
    LESSTHAN = 7
    EQUALS = 8
    HALT = 99

class Mode(Enum):
    POSITION = 0,
    IMMEDIATE = 1,

instructionCount = {
        Opcodes.JTRUE: 3,
        Opcodes.JFALSE: 3,
        Opcodes.LESSTHAN: 4,
        Opcodes.EQUALS: 4,
        Opcodes.ADD: 4,
        Opcodes.MULTIPLY: 4,
        Opcodes.INPUT: 2,
        Opcodes.OUTPUT: 2,
        Opcodes.HALT: 1
        }
# Get data, and save it
with open("input1.txt","r") as f:
    data = f.readlines()[0].replace("\n","").split(',')

data = list(map(int, data))

originalMemory = copy.deepcopy(data)

def readOpcodeInfo(opcode):
    # It will be an integer at this point, so for convenience
    # Of slicing we make it a string
    result = ["0", "0", "0", "-1"]
    opcode = str(opcode)
    #print("\tOPCODE READ: {}".format(opcode))
    if len(opcode) <= 2:
        result[3] = int(opcode)
    if len(opcode) >= 3:
        result[3] = int(opcode[1]+opcode[2])
        result[2] = int(opcode[0])
    if len(opcode) >=4:
        result[3] = int(opcode[2]+opcode[3])
        result[2] = int(opcode[1])
        result[1] = int(opcode[0])
    if len(opcode) == 5:
        result[3] = int(opcode[3]+opcode[4])
        result[2] = int(opcode[2])
        result[1] = int(opcode[1])
        result[0] = int(opcode[0])
    return result

def getValue(mode, readPosition):
    if mode == Mode.POSITION:
        return data[data[readPosition]]
    elif mode == Mode.IMMEDIATE:
        return data[readPosition]


# Compute with opcodes
def compute(data, readPoint):
    while(True):
        addInstructionCount = True
        statusMode = [Mode.POSITION for x in range(3)]
        # Need to get OPCODE data
        opcodeData = readOpcodeInfo(data[readPoint])
        print("STEP\n\tOpcode:{}\n\tReadpoint:{}\n\tNext 4 data values: {}, {}, {}, {}".format(opcodeData[3], readPoint, data[readPoint], data[readPoint+1], data[readPoint+2], data[readPoint+3]))
        opcode = Opcodes(opcodeData[3])
        # Set status mode enums
        # Parameter 3
        if opcodeData[0] == 1:
            statusMode[2] = Mode.IMMEDIATE
        # Parameter 2
        if opcodeData[1] == 1:
            statusMode[1] = Mode.IMMEDIATE
        # Parameter 1
        if opcodeData[2] == 1:
            statusMode[0] = Mode.IMMEDIATE

        # We now have the mode. Must rewrite below opcodes into their own functions taking in the opcodeData as input
        result = None
        if (opcode == Opcodes.HALT):
            break
        elif (opcode == Opcodes.ADD):
            result = getValue(statusMode[0], readPoint+1) + getValue(statusMode[1], readPoint+2)
            data[data[readPoint+3]] = result

        elif (opcode == Opcodes.MULTIPLY):
            result = getValue(statusMode[0], readPoint+1) * getValue(statusMode[1], readPoint+2)
            data[data[readPoint+3]] = result

        elif (opcode == Opcodes.INPUT):
            data[data[readPoint+1]] = int(input("INTCOMPUTER INPUT > "))

        elif (opcode == Opcodes.OUTPUT):
            print(data[data[readPoint+1]])

        elif opcode == Opcodes.JTRUE:
            result = getValue(statusMode[0], readPoint+1)
            if result != 0:
                addInstructionCount = False
                readPoint = getValue(statusMode[1],readPoint+2)#data[readPoint+2]

        elif opcode == Opcodes.JFALSE:
            result = getValue(statusMode[0], readPoint+1)
            if result == 0:
                addInstructionCount = False
                readPoint = getValue(statusMode[1], readPoint+2)#data[readPoint+2]

        elif opcode == Opcodes.LESSTHAN:
            result = getValue(statusMode[0], readPoint+1) < getValue(statusMode[1], readPoint+2)
            if result:
                data[data[readPoint+3]] = 1
            else:
                data[data[readPoint+3]] = 0

        elif opcode == Opcodes.EQUALS:
            result = getValue(statusMode[0], readPoint+1) == getValue(statusMode[1], readPoint+2)
            if result:
                data[data[readPoint+3]] = 1
            else:
                data[data[readPoint+3]] = 0

        else:
            #pass
            print("ERROR, Invalid opcode!")

        if addInstructionCount:
            readPoint+=instructionCount.get(opcode)
    return data[0]
data = copy.deepcopy(originalMemory)
compute(data, 0)
