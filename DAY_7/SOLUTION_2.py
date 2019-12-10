from enum import Enum
from itertools import permutations
from collections import defaultdict
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

with open("input1.txt","r") as f:
    data = f.readlines()[0].replace("\n","").split(',')

dataDict = defaultdict(int)

for i in range(len(data)):
    dataDict.update({i: int(data[i])})

def getOperation(value):
    m1 = 0
    m2 = 0
    m3 = 0
    opcode = 0
    value = str(value).zfill(5)
    opcode = int(value[3:])
    m1 = int(value[2])
    m2 = int(value[1])
    m3 = int(value[0])
    # In order, I.E. 01104
    # m1 is 1, m2 is 1, m3 is 0, opcode is 04
    return m3, m2, m1, opcode

def getValue(dataDict, pc, mode):
    if mode == 0:
        return dataDict.get(dataDict.get(pc))
    elif mode == 1:
        return dataDict.get(pc)

def add(dataDict, pc, modes):
    result = {dataDict[pc+3]: getValue(dataDict, pc+1, modes[0])+getValue(dataDict, pc+2, modes[1])}
    dataDict.update(result)
    pc+=4
    return dataDict, pc

def multiply(dataDict, pc, modes):
    result = {dataDict[pc+3]: getValue(dataDict, pc+1, modes[0])*getValue(dataDict, pc+2, modes[1])}
    dataDict.update(result)
    pc+=4
    return dataDict, pc

def jtrue(dataDict, pc, modes):
    result = getValue(dataDict, pc+1, modes[0])
    if result !=0:
        pc = getValue(dataDict, pc+2, modes[1])
    else:
        pc+=3
    return pc

def jfalse(dataDict, pc, modes):
    result = getValue(dataDict, pc+1, modes[0])
    if result ==0:
        pc = getValue(dataDict, pc+2, modes[1])
    else:
        pc+=3
    return pc

def lessthan(dataDict, pc, modes):
    result  = getValue(dataDict, pc+1, modes[0])
    result2 = getValue(dataDict, pc+2, modes[1])
    if result < result2:
        value = {dataDict[pc+3]: 1}
    else:
        value = {dataDict[pc+3]: 0}
    pc+=4
    dataDict.update(value)
    return dataDict, pc

def equals(dataDict, pc, modes):
    result  = getValue(dataDict, pc+1, modes[0])
    result2 = getValue(dataDict, pc+2, modes[1])
    if result == result2:
        value = {dataDict[pc+3]: 1}
    else:
        value = {dataDict[pc+3]: 0}
    pc+=4
    dataDict.update(value)
    return dataDict, pc
# Output defined as datDict, pc, value
def compute(dataDict, pc, inputs):
    while(True):
        m3, m2, m1, opcode = getOperation(dataDict[pc])
        modes = [m1, m2, m3]
        converted = [m1, m2, m3, opcode]
        #print("Got {}, converted: {}".format(dataDict[pc], converted))
        #print("Opcode: {}, PC: {}, MODES: {}".format(Opcodes(opcode), pc, modes))
        if Opcodes(opcode) == Opcodes.HALT:
            return dataDict, pc, None
        elif Opcodes(opcode) == Opcodes.INPUT:
            value = {dataDict[pc+1]: inputs[0]}
            inputs.pop(0)
            dataDict.update(value)
            pc+=2
        elif Opcodes(opcode) == Opcodes.OUTPUT:
            return dataDict, pc+2, dataDict[dataDict[pc+1]]
        elif Opcodes(opcode) == Opcodes.ADD:
            dataDict, pc = add(dataDict, pc, modes)
        elif Opcodes(opcode) == Opcodes.MULTIPLY:
            dataDict, pc = multiply(dataDict, pc, modes)
        elif Opcodes(opcode) == Opcodes.JTRUE:
            pc = jtrue(dataDict, pc, modes)
        elif Opcodes(opcode) == Opcodes.JFALSE:
            pc = jfalse(dataDict, pc, modes)
        elif Opcodes(opcode) == Opcodes.LESSTHAN:
            dataDict, pc = lessthan(dataDict, pc, modes)
        elif Opcodes(opcode) == Opcodes.EQUALS:
            dataDict, pc = equals(dataDict, pc, modes)
        else:
            print("INVALID OPCODE!")

phaseSettings = permutations([5,6,7,8,9])
maxThrusterSignal = 0

for phaseConfig in phaseSettings:
    amplifierData = [dataDict.copy() for x in range(5)]
    amplifierPcs = [0 for x in range(5)]
    amplifierInputs = [[phaseConfig[x]] for x in range(5)]
    amplifierInputs[0].append(0)
    halted = False
    finalVal = 0
    while not halted:
        for x in range(4):
            amplifierData[x], amplifierPcs[x], value = compute(amplifierData[x], amplifierPcs[x], amplifierInputs[x])
            amplifierInputs[x+1].append(value)
        amplifierData[4], amplifierPcs[4], outputVal = compute(amplifierData[4], amplifierPcs[4], amplifierInputs[4])
        if outputVal is None:
            halted = True
        else:
            finalVal = outputVal
            amplifierInputs[0].append(outputVal)
    maxThrusterSignal = max(maxThrusterSignal, finalVal)

print(maxThrusterSignal)
