import re
regexStr = r"00|11|22|33|44|55|66|77|88|99"

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

print("Succesfully ended")
print("Answer: {}".format(len(passwords)))
