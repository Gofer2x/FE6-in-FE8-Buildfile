def intToHex(i):
    j = hex(i)
    j = j.upper()
    j = j.replace("X", "x")
    return str(j)
	
with open("RawItemAnimsTable.txt", "r") as r:
    data = r.readlines()

output = []
i = 0
for line in data:
    numline = line.replace("XYZ",intToHex(i))
    output.append(numline)
    i += 1

with open("GeneratedItemAnimsTable.event","w") as w:
    w.writelines(output)

input("Done. Enter to exit.")