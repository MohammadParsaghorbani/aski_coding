line = int(input("line = "))
file = open("aski_code.txt" , "r")
ordd = []
chr = []
correct = ""
content = file.readline()
for i in range(line):
    content = file.readline()
for i in content:
    x = ord(i)-11
    ordd.append(x)
for i in ordd:
    correct += chr(i)
print(content)
print(correct)
file.close()