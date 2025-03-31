import os, shutil, csv

fromROM = "FE6Localization_v1.2.1.gba"
baseROM = "myHack.gba"
targetROM = "myHackWithMusic.gba"
FEBuilderGBA = "..\\FEBuilderGBA\\FEBuilderGBA.exe --rom="+targetROM

shutil.copy(baseROM, targetROM)

def songExchange(name,fromID,targetID):
    if "0x" not in fromID:
        fromID = hex(int(fromID))
    if "0x" not in targetID:
        targetID = hex(int(targetID))
    print(f"Inserting {name} from ID {fromID} into ID {targetID}")
    os.system('%s --songexchange --fromrom=%s --target=%s --fromsong=%s --tosong=%s' % (FEBuilderGBA, fromROM, targetROM, fromID, targetID))

csvData = []
with open('FE6toFE8Sounds.csv', mode ='r', encoding="utf-8")as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        csvData.append(lines)

fe6ID = "dummy"
fe8ID = "dummy"

for item in csvData:
    name = item["Name"]

    #If the ID is "i", means iterative. Else, actual number.
    if item["FE6 ID"] == "i":
        fe6ID = str(int(fe6ID.replace("0x",""))+1)
    else:
        fe6ID = item["FE6 ID"]

    if item["FE8 Target ID"] == "i":
        fe8ID = str(int(fe8ID.replace("0x",""))+1)
    else:
        fe8ID = item["FE8 Target ID"]
    
    songExchange(name,fe6ID,fe8ID)

input("Done. Enter to exit program...")