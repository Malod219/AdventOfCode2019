from enum import Enum
from itertools import permutations
from collections import defaultdict

with open("input1.txt","r") as f:
    data = f.readlines()

dataDict = {}

for line in data:
    line=line.split("=>")
    line[0]=line[0].split(",")
    for value in line[0]:
        value = value.split(" ")

for line in data:
    print(line)