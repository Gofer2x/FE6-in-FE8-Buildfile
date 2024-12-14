with open("Supports.txt","r") as r:
    data = r.readlines()


pass
output = []
for line in data:
    if ("[X]" in line) or (line == "\n") or ("##" in line):
        output.append(line)
    elif ("[A]" in line):
        newline = line.replace("[A]","[AN]")
        output.append(newline)
    elif (line.strip()[-1] != "]"):
        newline = line.replace("\n","")
        newline = newline+"[A]\n"
        output.append(newline)
    else:
        output.append(line)

with open("Supports2.txt","w") as w:
    w.writelines(output)