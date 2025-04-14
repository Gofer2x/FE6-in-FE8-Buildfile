output = []

maxX = 48
maxY = 48

output.append("ALIGN 4\n")

for x in range(maxY):
    for y in range(maxY):
        output.append("REDA_"+str(x)+"_"+str(y)+":\n")
        output.append("REDA ["+str(x)+","+str(y)+"] 0x0 0x0 0x0 0x0\n")

with open("REDAs.event","w") as write:
    write.writelines(output)