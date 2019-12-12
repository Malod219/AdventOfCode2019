from enum import Enum
from itertools import permutations
from collections import defaultdict
import pprint

class Opcodes(Enum):
    ADD = 1
    MULTIPLY = 2
    INPUT = 3
    OUTPUT = 4
    JTRUE = 5
    JFALSE = 6
    LESSTHAN = 7
    EQUALS = 8
    OFFSET = 9
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
    return m3, m2, m1, opcode

def getValue(dataDict, pc, mode, relativeBase):
    if mode == 0:
        val = dataDict.get(dataDict.get(pc))
    if mode == 1:
        val = dataDict.get(pc)
    if mode == 2:
        #print("Relative base is {}".format(relativeBase))
        val = dataDict.get(dataDict.get(pc)+relativeBase)
    if val is None:
        return 0
    return val

def getValueLiteral(dataDict, pc, mode, relativeBase):
    if mode == 0:
        return dataDict[pc]
    if mode == 1:
        raise Exception("Not allowed")
    if mode == 2:
        return dataDict[pc]+relativeBase

def add(dataDict, pc, modes, relativeBase):
    value = getValue(dataDict, pc+1, modes[0], relativeBase)+getValue(dataDict, pc+2, modes[1], relativeBase)
    loc = getValueLiteral(dataDict, pc+3, modes[2], relativeBase)
    result = {loc: value}
    dataDict.update(result)
    pc+=4
    return dataDict, pc

def multiply(dataDict, pc, modes, relativeBase):
    value = getValue(dataDict, pc+1, modes[0], relativeBase)*getValue(dataDict, pc+2, modes[1], relativeBase)
    loc = getValueLiteral(dataDict, pc+3, modes[2], relativeBase)
    result = {loc: value}
    dataDict.update(result)
    pc+=4
    return dataDict, pc

def jtrue(dataDict, pc, modes, relativeBase):
    result = getValue(dataDict, pc+1, modes[0], relativeBase)
    if result !=0:
        pc = getValue(dataDict, pc+2, modes[1], relativeBase)
    else:
        pc+=3
    return pc

def jfalse(dataDict, pc, modes, relativeBase):
    result = getValue(dataDict, pc+1, modes[0], relativeBase)
    if result ==0:
        pc = getValue(dataDict, pc+2, modes[1], relativeBase)
    else:
        pc+=3
    return pc

def lessthan(dataDict, pc, modes, relativeBase):
    result  = getValue(dataDict, pc+1, modes[0], relativeBase)
    result2 = getValue(dataDict, pc+2, modes[1], relativeBase)
    loc = getValueLiteral(dataDict, pc+3, modes[2], relativeBase)
    if result < result2:
        value = {loc: 1}
    else:
        value = {loc: 0}
    pc+=4
    dataDict.update(value)
    return dataDict, pc

def equals(dataDict, pc, modes, relativeBase):
    result  = getValue(dataDict, pc+1, modes[0], relativeBase)
    result2 = getValue(dataDict, pc+2, modes[1], relativeBase)
    loc = getValueLiteral(dataDict, pc+3, modes[2], relativeBase)
    if result == result2:
        value = {loc: 1}
    else:
        value = {loc: 0}
    pc+=4
    dataDict.update(value)
    return dataDict, pc

# Output defined as datDict, pc, value
def compute(dataDict, pc, relativeBase, inputs):
    while(True):
        m3, m2, m1, opcode = getOperation(dataDict[pc])
        modes = [m1, m2, m3]
        converted = [m1, m2, m3, opcode]
        #print("Got {}, converted: {}".format(dataDict[pc], converted))
        #print("Opcode: {}, PC: {}, RELATIVE BASE {}, MODES: {}".format(Opcodes(opcode), pc, relativeBase, modes))
        if Opcodes(opcode) == Opcodes.HALT:
            return dataDict, pc, relativeBase, None
            #return dataDict, pc, None
        elif Opcodes(opcode) == Opcodes.INPUT:
            loc = getValueLiteral(dataDict, pc+1, modes[0], relativeBase)
            value = {loc: inputs[0]}
            inputs.pop(0)
            dataDict.update(value)
            pc+=2
        elif Opcodes(opcode) == Opcodes.OUTPUT:
            value = getValue(dataDict, pc+1, modes[0], relativeBase)
            pc+=2
            return dataDict, pc, relativeBase, value
            #print(value)
        elif Opcodes(opcode) == Opcodes.ADD:
            dataDict, pc = add(dataDict, pc, modes, relativeBase)
        elif Opcodes(opcode) == Opcodes.MULTIPLY:
            dataDict, pc = multiply(dataDict, pc, modes, relativeBase)
        elif Opcodes(opcode) == Opcodes.JTRUE:
            pc = jtrue(dataDict, pc, modes, relativeBase)
        elif Opcodes(opcode) == Opcodes.JFALSE:
            pc = jfalse(dataDict, pc, modes, relativeBase)
        elif Opcodes(opcode) == Opcodes.LESSTHAN:
            dataDict, pc = lessthan(dataDict, pc, modes, relativeBase)
        elif Opcodes(opcode) == Opcodes.EQUALS:
            dataDict, pc = equals(dataDict, pc, modes, relativeBase)
        elif Opcodes(opcode) == Opcodes.OFFSET:
            relativeBase += getValue(dataDict, pc+1, modes[0], relativeBase)
            pc+=2
        else:
            print("INVALID OPCODE!")
halted=False
pc = 0
relativeBase = 0
inputs = []
panelWidth = 800
panelHeight = 800

panel = [[0 for x in range(panelWidth)] for y in range(panelHeight)]

class Directions(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

botPosition = [panelWidth//2, panelHeight//2]
botDirection = 0
positionsPainted = []
while not halted:
    inputs.append(panel[botPosition[1]][botPosition[0]])
    dataDict, pc, relativeBase, value = compute(dataDict, pc, relativeBase, inputs)
    if value is None:
        halted = True
        break
    panel[botPosition[1]][botPosition[0]] = value
    if (botPosition[0], botPosition[1]) not in positionsPainted:
        positionsPainted.append((botPosition[0], botPosition[1]))
    dataDict, pc, relativeBase, value2 = compute(dataDict, pc, relativeBase, inputs)
    if value2 is None:
        halted = True
        break
    botDirection+=value2

    if Directions(botDirection%4) == Directions.UP:
        botPosition[1] = botPosition[1]-1
    if Directions(botDirection%4) == Directions.DOWN:
        botPosition[1] = botPosition[1]+1
    if Directions(botDirection%4) == Directions.LEFT:
        botPosition[0] = botPosition[0]-1
    if Directions(botDirection%4) == Directions.RIGHT:
        botPosition[0] = botPosition[0]+1

pprint.pprint(panel)
