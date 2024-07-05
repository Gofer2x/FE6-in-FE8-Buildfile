def Funny(i):
    j = hex(i)
    j = j.upper()
    j = j.replace("X", "x")
    return str(j)

names = ["Mercenary",
         "Hero"

]

output = []


i = 176
for name in names:
    output.append("#define "+name+"ClassCard"+" "+Funny(i)+"\n")
    output.append("setCardEntry("+Funny(i)+", "+name+"CardData, "+name+"CardPalette)\n")
    output.append("\n")
    i += 1
    
with open("GeneratedCardInstaller.event", "w") as writeCardInstaller:
    writeCardInstaller.writelines(output)