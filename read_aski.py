line = int(input("line = "))
file = open("aski_code.txt" , "r")
correct = ""
content = file.readline()
for i in range(line):
    content = file.readline()
for i in content:
    z = ord(i)-5
    z = z//2
    correct += chr(z)
print(content)
print(correct)
file.close()