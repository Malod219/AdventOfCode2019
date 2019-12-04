import re

with open("input1.txt","r") as f:
    data = f.readlines()[0].split("-")
print("Ranges")
print(data[0])
print(data[1])
passwords = []
print("---")
for a in range(10):
    if a < int(data[0][0]):
        continue
    if a > int(data[1][0]):
        continue
    for b in range(10):
        if b < a:
            continue
        for c in range(10):
            if c < b:
                continue
            for d in range(10):
                if d < c:
                    continue
                for e in range(10):
                    if e < d:
                        continue
                    for f in range(10):
                        if f < e:
                            continue
                        # Construct it as a string then do a regex check for the 2 consecutive digits
                        password = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                        if int(password) >= int(data[0]) and int(password) <= int(data[1]):
                            for i in range(len(password)-1):
                                if password[i] == password[i+1]:
                                    passwords.append(password)
                                    break
actualPasswords = []

for password in passwords:
    x = re.findall(r'0{2,6}|1{2,6}|2{2,6}|3{2,6}|4{2,6}|5{2,6}|6{2,6}|7{2,6}|8{2,6}|9{2,6}', password)
    #print(password)
    for value in x:
        if len(value) == 2:
            actualPasswords.append(password)
            break



print("Succesfully ended")
print("Answer: {}".format(len(actualPasswords)))
