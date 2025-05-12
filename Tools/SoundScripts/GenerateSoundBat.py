import sys, csv

generatedBatPath = sys.argv[1]
csvPath = sys.argv[2]
febPath = sys.argv[3]
fromROMPath = sys.argv[4]
targetROMPath = sys.argv[5]
soundPrioFixPath = sys.argv[6]
#generatedBatPath = "_GeneratedFE6SoundInsertionAndFix.bat"
#csvPath = "FE6toFE8Sounds.csv"
#febPath = "Tools\\FEBuilderGBA\\FEBuilderGBA.exe"
#fromROMPath = "FE6.gba"
#targetROMPath = "myHackWithMusicTest.gba"
#soundPrioFixPath = "Tools\\SoundScripts\\SoundPriorityFixEA.event"

def intToHex(i):
    j = hex(i)
    j = j.upper()
    j = j.replace("X", "x")
    return str(j)

def formatCmd(fromSongID, toSongID):
    return(f"%febPath% --rom=%targetROMPath% --songexchange --fromrom=%fromROMPath% --target=%targetROMPath% --fromsong={fromSongID} --tosong={toSongID}\n")

csvData = []
with open(csvPath, mode ='r', encoding="utf-8")as file:
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        csvData.append(lines)

fe6ID = None
fe8ID = None
cmdOutput = []
cmdOutput.append(f"set febPath={febPath}\n")
cmdOutput.append(f"set fromROMPath={fromROMPath}\n")
cmdOutput.append(f"set targetROMPath={targetROMPath}\n")
cmdOutput.append(f"set soundPrioFixPath={soundPrioFixPath}\n")



for item in csvData:
    name = item["Name"]

    #If the ID is "i", means iterative. Else, actual number.
    if item["FE6 ID"] == "i":
        fe6ID = int(fe6ID,16)
        fe6ID += 1
        fe6ID = intToHex(fe6ID)
    else:
        fe6ID = item["FE6 ID"]

    if item["FE8 Target ID"] == "i":
        fe8ID = int(fe8ID,16)
        fe8ID += 1
        fe8ID = intToHex(fe8ID)
    else:
        fe8ID = item["FE8 Target ID"]
    
    cmdOutput.append(formatCmd(fe6ID,fe8ID))

# Move to EA folder and run the priority fix EA.
cmdOutput.append("cd %~dp0EventAssembler\n")
cmdOutput.append(f"ColorzCore A FE8 -output:%~dp0%targetROMPath% -input:%~dp0%soundPrioFixPath% --build-times\n")
cmdOutput.append("cd %~dp0")

with open(generatedBatPath,"w") as w:
    w.writelines(cmdOutput)