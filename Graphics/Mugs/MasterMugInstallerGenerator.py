#this file is an abomination lol

def Funny(i):
    j = hex(i)
    j = j.upper()
    j = j.replace("X", "x")
    return str(j)

mugsData = {
    "Roy":[2,6,3,4],
    "Marcus":[2,5,2,3],
    "Alen":[2,5,3,3],
    "Lance":[2,5,3,3],
    "Wolt":[2,6,3,4],
    "Bors":[2,4,3,2],
    "Merlinus":[2,5,2,3],
    "Elen":[2,6,3,4],
    "Dieck":[2,5,2,3],
    "Ward":[2,5,2,3],
    "Lot":[2,5,3,3],
    "Shanna":[2,6,3,4],
    "Chad":[2,6,3,4],
    "Lugh":[2,6,3,4],
    "Clarine":[2,6,3,4],
    "Rutger":[2,5,2,3],
    "Saul":[2,5,3,3],
    "Dorothy":[2,5,3,3],
    "Sue":[2,5,3,3],
    "Zelot":[2,5,3,3],
    "Trec":[2,5,3,3],
    "Noah":[2,5,3,3],
    "Astolfo":[2,5,2,3],
    "Lilina":[2,6,3,4],
    "Barthe":[2,4,2,2],
    "Ogier":[2,6,3,4],
    "Gwendolyn":[2,6,3,4],
    "Fir":[2,6,3,4],
    "Sin":[2,5,3,3],
    "Geese":[2,5,3,3],
    "Gonzalez":[2,5,2,3],
    "Klein":[2,5,3,3],
    "Thea":[2,5,3,4],
    "Larum":[2,6,3,4],
    "Elffin":[2,5,2,3],
    "Echidna":[2,5,3,3],
    "Bartre":[2,5,2,2],
    "Raigh":[2,6,3,4],
    "Cath":[2,6,3,4],
    "Melady":[2,5,4,3],
    "Perceval":[2,5,2,3],
    "Cecilia":[2,5,3,3],
    "Sophia":[2,6,3,4],
    "Igrene":[2,5,3,3],
    "Garrett":[2,4,3,2],
    "Fae":[3,7,3,5],
    "Hugh":[2,5,3,3],
    "Zeiss":[2,5,2,3],
    "Douglas":[2,5,3,3],
    "Niime":[2,6,2,4],
    "Juno":[2,5,3,3],
    "Dayan":[2,5,3,3],
    "Yoder":[2,5,3,3],
    "Karel":[2,5,3,3],
    "Hector":[2,5,3,2],
    "Eliwood":[2,5,3,3],
    "Guinivere":[3,6,3,4],
    "Damas":[2,5,2,3],
    "Ruud":[3,5,4,3],
    "Slater":[3,5,3,3],
    "Erik":[2,5,3,3],
    "Dory":[2,5,3,3],
    "Wagner":[2,6,3,4],
    "Debias":[2,5,2,3],
    "Legance":[2,5,2,3],
    "Henning":[2,5,3,3],
    "Scott":[2,5,3,3],
    "Nord":[2,6,3,4],
    "Orlo":[3,5,3,3],
    "Roberts":[2,5,3,3],
    "Zinque":[2,5,3,3],
    "Scollan":[2,5,2,3],
    "Morgan":[2,5,2,3],
    "Ein":[2,5,3,3],
    "Guerrero":[2,5,3,3],
    "Flaer":[2,5,3,3],
    "Randy":[2,5,3,3],
    "Maggie":[2,5,3,3],
    "Rose":[2,5,3,3],
    "Oates":[2,6,2,3],
    "Raith":[2,5,3,3],
    "Narcian":[2,5,3,3],
    "Windham":[3,5,3,3],
    "Arcardo":[2,5,3,3],
    "Martel":[3,5,3,3],
    "Sigune":[2,5,3,3],
    "Roartz":[2,5,2,3],
    "Tick":[2,5,3,3],
    "Monke":[2,5,3,3],
    "Kel":[2,5,3,3],
    "SacaeGaidenBosses":[2,5,3,3],
    "Galle":[2,5,3,3],
    "Murdock":[2,4,3,2],
    "Peres":[2,6,2,4],
    "Zephiel":[4,4,4,2],
    "Brunnya":[2,5,3,3],
    "Jahn":[3,5,3,3],
    "IdunnHuman":[2,6,3,4],
    "IdunnDragon":[2,10,3,4], #0x63
    "Anna":[2,5,3,3],
    "Armory":[3,2,0,0],
    "Vendor":[3,3,0,0],
    "Arena":[3,2,0,0],
    "SecretShop":[3,3,0,0],
    "BanditKid":[2,6,2,4],
    "IdunnHood":[2,6,3,4],
    "HectorBlood":[2,5,3,2],
    "Mordred":[3,6,4,4],
    "GenericPegasusKnight":[2,6,3,4],
    "Priest":[2,5,2,3],
    "SacaeanVillager":[2,6,3,4],
    "Soldier1":[4,6,4,4],
    "Soldier2":[4,6,4,4],
    "Soldier3":[4,6,4,4],
    "Soldier4":[4,6,4,4],
    "Soldier5":[4,6,4,4],
    "Soldier6":[4,6,4,4],
    "Soldier7":[4,6,4,4],
    "Mary":[2,5,3,3],
    "Mieu":[2,7,3,5],
    "Villager1":[2,6,3,4],
    "Villager2":[4,6,3,4],
    "Villager3":[2,5,3,3],
    "Villager4":[2,6,3,4],
    "Villager5":[2,6,3,4],
    "Villager6":[2,7,2,4],
    "Villager7":[2,6,3,4],
    "Villager8":[2,6,3,4],
    "Villager9":[2,5,3,3],
    "Villager10":[2,6,3,4],
    "Villager11":[3,7,3,5],
    "Villager12":[3,7,3,5],
    "Villager13":[2,6,3,4],
    "Villager14":[4,6,4,4],
    "Villager15":[2,5,3,3],
    "Villager16":[2,6,3,4],
    "Villager17":[2,6,3,4],
    "Villager18":[2,7,2,4],
    "Villager19":[2,6,3,4],
    "Villager20":[2,6,3,4],
    "Villager21":[2,5,3,3],
    "Villager22":[2,6,3,4],
    "Villager23":[3,7,3,5],
    "Villager24":[3,7,3,5],
    "Villager25":[2,6,3,4],
    "Villager26":[4,6,4,4],
    "Villager27":[2,5,3,3],
    "Villager28":[2,6,3,4],
    "Villager29":[2,6,3,4],
    "Villager30":[2,7,2,4],
    "Villager31":[2,6,3,4],
    "Villager32":[2,6,3,4],
    "Villager33":[2,5,3,3],
    "Villager34":[2,6,3,4],
    "Villager35":[3,7,3,5],
    "Villager36":[3,7,3,5],
    "Villager37":[2,6,3,4],
    "Villager38":[4,6,4,4],
    "Villager39":[2,5,3,3],
    "Villager40":[2,6,3,4],
    "Villager41":[2,6,3,4],
    "Villager42":[2,7,2,4],
    "Villager43":[2,6,3,4],
    "Villager44":[2,6,3,4],
    "Villager45":[2,5,3,3],
    "Villager46":[2,6,3,4],
    "Villager47":[3,7,3,5],
    "Villager48":[3,7,3,5],
    "Villager49":[2,6,3,4],
    "Villager50":[4,6,4,4],
    "Villager51":[2,5,3,3],
    "Villager52":[2,6,3,4],
    "Villager53":[2,6,3,4],
    "Villager54":[2,7,2,4],
    "Villager55":[2,6,3,4],
    "Villager56":[2,6,3,4],
    "Villager57":[2,5,3,3],
    "Villager58":[2,6,3,4],
    "Villager59":[3,7,3,5],
    "Villager60":[3,7,3,5],

}

paletteSwaps = [
    ["Soldier1","Soldier2","Soldier3","Soldier4","Soldier5","Soldier6","Soldier7"],
#    ["Villager1","Villager13","Villager25","Villager37","Villager49"],
    ["Villager2","Villager14","Villager26","Villager38","Villager50"],
    ["Villager3","Villager15","Villager27","Villager39","Villager51"],
    ["Villager3","Villager15","Villager27","Villager39","Villager51"],
    ["Villager4","Villager16","Villager28","Villager40","Villager52"],
    ["Villager5","Villager17","Villager29","Villager41","Villager53"],
    ["Villager6","Villager18","Villager30","Villager42","Villager54"],
    ["Villager7","Villager19","Villager31","Villager43","Villager55"],
    ["Villager8","Villager20","Villager32","Villager44","Villager56"],
    ["Villager9","Villager21","Villager33","Villager45","Villager57"],
    ["Villager10","Villager22","Villager34","Villager46","Villager58"],
    ["Villager11","Villager23","Villager35","Villager47","Villager59"],
    ["Villager12","Villager24","Villager36","Villager48","Villager60"],


    ["Legance","Morgan"],
    ["Orlo","Martel","Windham"],
    ["Wagner","Nord"],
    ["Peres","Oates"],
    ["Scott","Rose","Maggie"],
    ["Henning","Randy"],
    ["Monke","SacaeGaidenBosses"],
    ["Raith","Tick"]

]

noMinis =[
    "Anna",
    "Armory",
    "Vendor",
    "Arena",
    "SecretShop"
    "BanditKid",
    "HectorBlood",
    "Mordred",
    "GenericPegasusKnight",
    "Priest",
    "SacaeanVillager",
    "Soldier1",
    "Soldier2",
    "Soldier3",
    "Soldier4",
    "Soldier5",
    "Soldier6",
    "Soldier7",
    "Mary",
    "Mieu",
    "Villager1",
    "Villager2",
    "Villager3",
    "Villager4",
    "Villager5",
    "Villager6",
    "Villager7",
    "Villager8",
    "Villager9",
    "Villager10",
    "Villager11",
    "Villager12",
    "Villager13",
    "Villager14",
    "Villager15",
    "Villager16",
    "Villager17",
    "Villager18",
    "Villager19",
    "Villager20",
    "Villager21",
    "Villager22",
    "Villager23",
    "Villager24",
    "Villager25",
    "Villager26",
    "Villager27",
    "Villager28",
    "Villager29",
    "Villager30",
    "Villager31",
    "Villager32",
    "Villager33",
    "Villager34",
    "Villager35",
    "Villager36",
    "Villager37",
    "Villager38",
    "Villager39",
    "Villager40",
    "Villager41",
    "Villager42",
    "Villager43",
    "Villager44",
    "Villager45",
    "Villager46",
    "Villager47",
    "Villager48",
    "Villager49",
    "Villager50",
    "Villager51",
    "Villager52",
    "Villager53",
    "Villager54",
    "Villager55",
    "Villager56",
    "Villager57",
    "Villager58",
    "Villager59",
    "Villager60",
]

output = []

names = list(mugsData.keys())
i = 1
for name in names:
    a,b,c,d = mugsData[name]
    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)
    output.append("#define "+name+"Mug "+Funny(i)+"\n")

    isSwap = False
    for swap in paletteSwaps:
        if name in swap:
            isSwap = True
            if name == swap[0]:
                if name not in noMinis:
                    templateString = [
                        #"ALIGN 4\n",
                        (name+"MugData:\n"),
                        ("#incbin \"Dmp/"+name+"_mug.dmp\"\n"),
                        (name+"MugFramesData:\n"),
                        ("#incbin \"Dmp/"+name+"_frames.dmp\"\n"),
                        (name+"MugPaletteData:\n"),
                        ("#incbin \"Dmp/"+name+"_palette.dmp\"\n"),
                        (name+"MugMiniData:\n"),
                        ("#incbin \"Dmp/"+name+"_minimug.dmp\"\n"),
                        ("setMugEntryManual("+name+"Mug, "+name+"MugData, "+name+"MugMiniData, "+name+"MugPaletteData, "+name+"MugFramesData, "+a+","+b+","+c+","+d+")\n")
                    ]
                else:
                    templateString = [
                        #"ALIGN 4\n",
                        (name+"MugData:\n"),
                        ("#incbin \"Dmp/"+name+"_mug.dmp\"\n"),
                        (name+"MugFramesData:\n"),
                        ("#incbin \"Dmp/"+name+"_frames.dmp\"\n"),
                        (name+"MugPaletteData:\n"),
                        ("#incbin \"Dmp/"+name+"_palette.dmp\"\n"),
                        ("setMugEntryManual("+name+"Mug, "+name+"MugData, 0x0, "+name+"MugPaletteData, "+name+"MugFramesData, "+a+","+b+","+c+","+d+")\n")
                    ]
            else:
                ogName = swap[0]
                a,b,c,d = mugsData[ogName]
                a = str(a)
                b = str(b)
                c = str(c)
                d = str(d)
                if name not in noMinis:
                    templateString = [
                        #"ALIGN 4\n",
                        (name+"MugPaletteData:\n"),
                        ("#incbin \"Dmp/"+name+"_palette.dmp\"\n"),
                        ("setMugEntryManual("+name+"Mug, "+ogName+"MugData, "+ogName+"MugMiniData, "+name+"MugPaletteData, "+ogName+"MugFramesData, "+a+","+b+","+c+","+d+")\n")
                    ]
                else:
                    templateString = [
                        #"ALIGN 4\n",
                        (name+"MugPaletteData:\n"),
                        ("#incbin \"Dmp/"+name+"_palette.dmp\"\n"),
                        ("setMugEntryManual("+name+"Mug, "+ogName+"MugData, 0x0, "+name+"MugPaletteData, "+ogName+"MugFramesData, "+a+","+b+","+c+","+d+")\n")
                    ]
            break

    if not isSwap:
        if name not in noMinis:
            templateString = [
                #"ALIGN 4\n",
                (name+"MugData:\n"),
                ("#incbin \"Dmp/"+name+"_mug.dmp\"\n"),
                (name+"MugFramesData:\n"),
                ("#incbin \"Dmp/"+name+"_frames.dmp\"\n"),
                (name+"MugPaletteData:\n"),
                ("#incbin \"Dmp/"+name+"_palette.dmp\"\n"),
                (name+"MugMiniData:\n"),
                ("#incbin \"Dmp/"+name+"_minimug.dmp\"\n"),
                ("setMugEntryManual("+name+"Mug, "+name+"MugData, "+name+"MugMiniData, "+name+"MugPaletteData, "+name+"MugFramesData, "+a+","+b+","+c+","+d+")\n")
            ]
        else:
            templateString = [
                #"ALIGN 4\n",
                (name+"MugData:\n"),
                ("#incbin \"Dmp/"+name+"_mug.dmp\"\n"),
                (name+"MugFramesData:\n"),
                ("#incbin \"Dmp/"+name+"_frames.dmp\"\n"),
                (name+"MugPaletteData:\n"),
                ("#incbin \"Dmp/"+name+"_palette.dmp\"\n"),
                ("setMugEntryManual("+name+"Mug, "+name+"MugData, 0x0, "+name+"MugPaletteData, "+name+"MugFramesData, "+a+","+b+","+c+","+d+")\n")
            ]
    for line in templateString:
        output.append(line)
    output.append("\n")
    i += 1
    
with open("GeneratedMugInstaller.event", "w") as writeMugInstaller:
    writeMugInstaller.writelines(output)


# ShowMugs
output = []

i = 1
for name in names:
    output.append("[Load"+name+"] = [LoadPortrait]["+Funny(i)+"][0x1]\n")
    i += 1

with open("ShowMugsAddToTextParseDefs.event", "w") as write:
    write.writelines(output)

# Cards

names = ["Mercenary",
         "Hero",
         "Myrmidon",
         "Swordmaster",
         "Fighter",
         "Warrior",
         "Brigand",
         "Pirate",
         "Berserker",
         "Soldier",
         "Knight",
         "General",
         "Archer",
         "Sniper",
         "Thief",
         "Rogue",
         #"Assassin",
         "Cavalier",
         "Paladin",
         "GreatKnight",
         "Nomad",
         "NomadTrooper",
         "MonkCleric",
         "Bishop",
         "Troubadour",
         "Valkyrie",
         "Mage",
         "Sage",
         "MageKnight",
         "Shaman",
         "Druid",
         "PegasusKnight",
         "Falcoknight",
         "WyvernRider",
         "WyvernLord",
         "WyvernKnight",
         "FireManakete"
]

output = []
for name in names:
    output.append("#define "+name+"ClassCard"+" "+Funny(i)+"\n")
    output.append("setCardEntry("+name+"ClassCard, "+name+"CardData, "+name+"CardPalette)\n")
    output.append("\n")
    i += 1
    
with open("GeneratedCardInstaller.event", "w") as writeCardInstaller:
    writeCardInstaller.writelines(output)