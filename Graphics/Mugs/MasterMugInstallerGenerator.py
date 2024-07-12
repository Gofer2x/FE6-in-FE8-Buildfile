def Funny(i):
    j = hex(i)
    j = j.upper()
    j = j.replace("X", "x")
    return str(j)

a = 0
b = 0
c = 0
d = 0

names = [
        ["Roy",2,6,3,4],
        ["Marcus",2,5,2,3],
        ["Alen",2,5,3,3],
        ["Lance",2,5,3,3],
        ["Wolt",2,6,3,4],
        ["Bors",2,4,3,2],
        ["Merlinus",2,5,2,3],
        ["Elen",2,6,3,4],
        ["Dieck",2,5,2,3],
        ["Ward",2,5,2,3],
        ["Lot",2,5,3,3],
        ["Shanna",2,6,3,4],
        ["Chad",2,6,3,4],
        ["Lugh",2,6,3,4],
        ["Clarine",2,6,3,4],
        ["Rutger",2,5,2,3],
        ["Saul",2,5,3,3],
        ["Dorothy",2,5,3,3],
        ["Sue",2,5,3,3],
        ["Zelot",2,5,3,3],
        ["Trec",2,5,3,3],
        ["Noah",2,5,3,3],
        ["Astolfo",2,5,2,3],
        ["Lilina",2,6,3,4],
        ["Barthe",2,4,2,2],
        ["Ogier",2,6,3,4],
        ["Gwendolyn",2,6,3,4],
        ["Fir",2,6,3,4],
        ["Sin",2,5,3,3],
        ["Geese",2,5,3,3],
        ["Gonzalez",2,5,2,3],
        ["Klein",2,5,3,3],
        ["Thea",2,5,3,4],
        ["Larum",2,6,3,4],
        ["Elffin",2,5,2,3],
        ["Echidna",2,5,3,3],
        ["Bartre",2,5,2,2],
        ["Raigh",2,6,3,4],
        ["Cath",2,6,3,4],
        ["Melady",2,5,4,3],
        ["Perceval",2,5,2,3],
        ["Cecilia",2,5,3,3],
        ["Sophia",2,6,3,4],
        ["Igrene",2,5,3,3],
        ["Garret",2,4,3,2],
        ["Fae",3,7,3,5],
        ["Hugh",2,5,3,3],
        ["Zeiss",2,5,2,3],
        ["Douglas",2,5,3,3],
        ["Niime",2,6,2,4],
        ["Juno",2,5,3,3],
        ["Dayan",2,5,3,3],
        ["Yoder",2,5,3,3],
        ["Karel",2,5,3,3],
        ["Hector",2,5,3,2],
        ["Eliwood",2,5,3,3],
        ["Guinivere",3,6,3,4],
        ["Damas",2,5,2,3],
        ["Ruud",3,5,4,3],
        ["Slater",3,5,3,3],
        ["Erik",2,5,3,3],
        ["Dory",2,5,3,3],
        ["Wagner",2,6,3,4],
        ["Debias",2,5,2,3],
        ["Legance",2,5,2,3],
        ["Henning",2,5,3,3],
        ["Scott",2,5,3,3],
        ["Nord",2,6,3,4],
        ["Orlo",3,5,3,3],
        ["Roberts",2,5,3,3],
        ["Zinque",2,5,3,3],
        ["Scollan",2,5,2,3],
        ["Morgan",2,5,2,3],
        ["Ein",2,5,3,3],
        ["Guerrero",2,5,3,3],
        ["Flaer",2,5,3,3],
        ["Randy",2,5,3,3],
        ["Maggie",2,5,3,3],
        ["Rose",2,5,3,3],
        ["Oates",2,6,2,3],
        ["Raith",2,5,3,3],
        ["Narcian",2,5,3,3],
        ["Windham",3,5,3,3],
        ["Arcardo",2,5,3,3],
        ["Martel",3,5,3,3],
        ["Sigune",2,5,3,3],
        ["Roartz",2,5,2,3],
        ["Tick",2,5,3,3],
        ["Monke",2,5,3,3],
        ["Kel",2,5,3,3],
        ["SacaeGaidenBosses",2,5,3,3],
        ["Galle",2,5,3,3],
        ["Murdock",2,4,3,2],
        ["Peres",2,6,2,4],
        ["Zephiel",4,4,4,2],
        ["Brunnya",2,5,3,3],
        ["Jahn",3,5,3,3],
        ["IdunnHuman",2,6,3,4],
        ["IdunnDragon",2,10,3,4],
        ["BanditKid",2,6,2,4],
        ["IdunnHood",2,6,3,4],
        ["HectorBlood",2,5,3,2],
        ["Mordred",3,6,4,4],
        ["PegasusMessanger",2,6,3,4],
        ["Priest",2,5,2,3],
        ["SacaeanVillager",2,6,3,4],
        ["Soldier1",4,6,4,4],
        ["Soldier2",4,6,4,4],
        ["Soldier3",4,6,4,4],
        ["Soldier4",4,6,4,4],
        ["Soldier5",4,6,4,4],
        ["Soldier6",4,6,4,4],
        ["Soldier7",4,6,4,4],
        ["Villager1",2,5,3,3],
        ["Villager2",2,7,3,5],
        ["Villager3",2,6,3,4],
        ["Villager4",4,6,4,4],
        ["Villager5",2,5,3,3],
        ["Villager6",2,6,3,4],
        ["Villager7",2,6,3,4],
        ["Villager8",2,7,2,4],
        ["Villager9",2,6,3,4],
        ["Villager10",2,6,3,4],
        ["Villager11",2,5,3,3],
        ["Villager12",2,6,3,4],
        ["Villager13",3,7,3,5],
        ["Villager14",3,7,3,5],
        ["Villager15",4,6,4,4],
        ["Villager16",2,5,3,3],
        ["Villager17",2,6,3,4],
        ["Villager18",2,6,3,4],
        ["Villager19",2,7,2,4],
        ["Villager20",2,6,3,4],
        ["Villager21",2,6,3,4],
        ["Villager22",2,5,3,3],
        ["Villager23",2,6,3,4],
        ["Villager24",3,7,3,5],
        ["Villager25",3,7,3,5],
        ["Villager26",2,6,3,4],
        ["Villager27",4,6,4,4],
        ["Villager28",2,5,3,3],
        ["Villager29",2,6,3,4],
        ["Villager30",2,6,3,4],
        ["Villager31",2,7,2,4],
        ["Villager32",2,6,3,4],
        ["Villager33",2,6,3,4],
        ["Villager34",2,5,3,3],
        ["Villager35",2,6,3,4],
        ["Villager36",3,7,3,5],
        ["Villager37",3,7,3,5],
        ["Villager38",2,6,3,4],
        ["Villager39",4,6,4,4],
        ["Villager40",2,5,3,3],
        ["Villager41",2,6,3,4],
        ["Villager42",2,6,3,4],
        ["Villager43",2,7,2,4],
        ["Villager44",2,6,3,4],
        ["Villager45",2,6,3,4],
        ["Villager46",2,5,3,3],
        ["Villager47",2,6,3,4],
        ["Villager48",3,7,3,5],
        ["Villager49",3,7,3,5],
        ["Villager50",2,6,3,4],
        ["Villager51",4,6,4,4],
        ["Villager52",2,5,3,3],
        ["Villager53",2,6,3,4],
        ["Villager54",2,6,3,4],
        ["Villager55",2,7,2,4],
        ["Villager56",2,6,3,4],
        ["Villager57",2,6,3,4],
        ["Villager58",2,5,3,3],
        ["Villager59",2,6,3,4],
        ["Villager60",3,7,3,5],
        ["Villager61",3,7,3,5]
]


output = []


i = 1
for namepackage in names:
    name = namepackage[0]
    a = str(namepackage[1])
    b = str(namepackage[2])
    c = str(namepackage[3])
    d = str(namepackage[4])
    output.append("#define "+name+"Mug "+Funny(i)+"\n")
    templateString = [
        "ALIGN 4\n",
        (name+"MugData:\n"),
        ("#incbin \"Dmp/"+name+"_mug.dmp\"\n"),
        ("#incbin \"Dmp/"+name+"_frames.dmp\"\n"),
        ("#incbin \"Dmp/"+name+"_palette.dmp\"\n"),
        ("#incbin \"Dmp/"+name+"_minimug.dmp\"\n"),
        ("setMugEntry("+name+"Mug, "+name+"MugData," +a+","+b+","+c+","+d+")\n")
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
for namepackage in names:
    name = namepackage[0]
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