from csv import DictReader
import sys
import os
#don't forget to change the X and Y into X1, Y1, X2, Y2 after exporting the csv!

def AI3Divide(input):
    properhex = int(input, 16)
    binary = format(properhex,'08b')
    rai = binary[5:8]
    tai = binary[0:5]
    return([rai, tai])
    #return([recoveryAIsList[str(rai)],targetAIsList[str(tai)]])

def UnitStateDivide(input):
    properhex = int(input, 16)
    binary = format(properhex,'08b')
    level = binary[0:5]
    army = binary[5:7]
    autolevel = binary[7]
    #level = int(level, 2)
    #army = affiliations[str(army)]
    #autolevel = autolevels[str(autolevel)]
    return([level, army, autolevel])


def CsvUnitToText(input):
    unit = unitsList[input['Unit Number']]
    classs = classesList[input['Class']]
    commander = unitsList[input['Commander']]

    level, army, autolevel = UnitStateDivide(input['Unit State'])
    level = str(int(level, 2))
    army = affiliations[army]
    autolevel = autolevels[autolevel]

    x = str(int(input['X1'],16))
    y = str(int(input['Y1'],16))
    xREDA = str(int(input['X2'],16))
    yREDA = str(int(input['Y2'],16))
    if (x != xREDA) or (y != yREDA):
        REDA = "0x1 REDA_"+xREDA+"_"+yREDA+""
    else:
        REDA = "0x0 0x0"

    item1 = itemsList[input['Item 1']]
    item2 = itemsList[input['Item 2']]
    item3 = itemsList[input['Item 3']]
    item4 = itemsList[input['Item 4']]

    ai1 = primaryAIsList[input['Primary AI']]
    ai2 = secondaryAIsList[input['Secondary AI']]

    rai, tai = AI3Divide(input['Target AI'])
    rai = recoveryAIsList[rai]
    tai = targetAIsList[tai]

    ai4 = retreatAIsList[input['Retreat AI']]

    unititems = [] 
    for i in [item1, item2, item3, item4]:
        if i:
            unititems.append(i)
    unititems = str(unititems)
    unititems = unititems.replace('\'','')

    return "UNIT"+" "+unit+" "+classs+" "+commander+" Level("+level+","+army+","+autolevel+") ["+x+","+y+"] 0x0 0x0 "+REDA+" "+unititems+" ["+ai1+", "+ai2+", "+rai+"|"+tai+", "+ai4+"]\n"

autolevels = {
    '0': "0",
    '1': "1"
}

affiliations = {
    '00': "Ally",
    '01': "NPC",
    '10': "Enemy",
    '11': "Defeated"
}

unitsList = {
"0x00" : "0x0",
"0x01" : "Roy",
"0x02" : "Clarine",
"0x03" : "Fae",
"0x04" : "Sin",
"0x05" : "Sue",
"0x06" : "Dayan",
"0x07" : "Dayan",
"0x08" : "Barthe",
"0x09" : "Bors",
"0x0A" : "Gwendolyn",
"0x0B" : "Douglas",
"0x0C" : "Douglas",
"0x0D" : "Wolt",
"0x0E" : "Dorothy",
"0x0F" : "Klein",
"0x10" : "Saul",
"0x11" : "Elen",
"0x12" : "Yoder",
"0x13" : "Yoder",
"0x14" : "Chad",
"0x15" : "Karel",
"0x16" : "Fir",
"0x17" : "Rutger",
"0x18" : "Dieck",
"0x19" : "Ogier",
"0x1A" : "Garrett",
"0x1B" : "Alen",
"0x1C" : "Lance",
"0x1D" : "Perceval",
"0x1E" : "Igrene",
"0x1F" : "Marcus",
"0x20" : "Astolfo",
"0x21" : "Ward",
"0x22" : "Lot",
"0x23" : "Bartre",
"0x24" : "Bartre",
"0x25" : "Lugh",
"0x26" : "Lilina",
"0x27" : "Hugh",
"0x28" : "Niime",
"0x29" : "Niime",
"0x2A" : "Raigh",
"0x2B" : "Larum",
"0x2C" : "Juno",
"0x2D" : "Juno",
"0x2E" : "Thea",
"0x2F" : "Thea",
"0x30" : "Thea",
"0x31" : "Shanna",
"0x32" : "Zeiss",
"0x33" : "Galle",
"0x34" : "Elffin",
"0x35" : "Cath",
"0x36" : "Sophia",
"0x37" : "Melady",
"0x38" : "Gonzalez",
"0x39" : "Gonzalez",
"0x3A" : "Noah",
"0x3B" : "Trec",
"0x3C" : "Zelot",
"0x3D" : "Echidna",
"0x3E" : "Echidna",
"0x3F" : "Cecilia",
"0x40" : "Geese",
"0x41" : "Geese",
"0x42" : "Merlinus",
"0x43" : "EliwoodTrial",
"0x44" : "GuinivereTrial",
"0x45" : "GenericBandit",
"0x46" : "GenericBandit",
"0x47" : "GenericBandit",
"0x48" : "GenericBandit",
"0x49" : "GenericBandit",
"0x4A" : "Damas",
"0x4B" : "Ruud",
"0x4C" : "Slater",
"0x4D" : "Erik",
"0x4E" : "Dory",
"0x4F" : "Wagner",
"0x50" : "Debias",
"0x51" : "Legance",
"0x52" : "Scott",
"0x53" : "Nord",
"0x54" : "William",
"0x55" : "Flaer",
"0x56" : "Orlo",
"0x57" : "Roberts",
"0x58" : "Ein",
"0x59" : "Narcian",
"0x5A" : "Randy",
"0x5B" : "Rose",
"0x5C" : "Maggie",
"0x5D" : "Raith",
"0x5E" : "Arcardo",
"0x5F" : "Martel",
"0x60" : "Sigune",
"0x61" : "Roartz",
"0x62" : "Murdock",
"0x63" : "Brunnya",
"0x64" : "Zephiel",
"0x65" : "IdunnHuman",
"0x66" : "IdunnDragon",
"0x67" : "Jahn",
"0x68" : "Zinque",
"0x69" : "Monke",
"0x6A" : "Kel",
"0x6B" : "0x6B",
"0x6C" : "GenericBern",
"0x6D" : "GenericBern",
"0x6E" : "GenericBern",
"0x6F" : "GenericBern",
"0x70" : "GenericBern",
"0x71" : "GenericLaus",
"0x72" : "GenericPirate",
"0x73" : "GenericBandit",
"0x74" : "GenericThria",
"0x75" : "GenericRebel",
"0x76" : "GenericBernCh8",
"0x77" : "GenericRebel",
"0x78" : "0x78",
"0x79" : "GenericThief",
"0x7A" : "GenericBanditWestIsles",
"0x7B" : "GenericWestIslesPirate",
"0x7C" : "GenericArmagh",
"0x7D" : "GenericRobber",
"0x7E" : "GenericResistance",
"0x7F" : "GenericEburacum",
"0x80" : "GenericBanditWestIsles",
"0x81" : "GenericSoldierWestIslesLords",
"0x82" : "GenericBanditWestIsles",
"0x83" : "GenericBern",
"0x84" : "GenericJuteaux",
"0x85" : "GenericSoldierWestIslesCapital",
"0x86" : "GenericBern",
"0x87" : "GenericEtruria",
"0x88" : "GenericBern",
"0x89" : "GenericBanditDesert",
"0x8A" : "GenericEtruria",
"0x8B" : "GenericBern",
"0x8C" : "GenericIllia",
"0x8D" : "GenericBandit",
"0x8E" : "GenericBern",
"0x8F" : "GenericEtruria",
"0x90" : "GenericThief",
"0x91" : "GenericEtruria",
"0x92" : "GenericBern",
"0x93" : "GenericPirate",
"0x94" : "GenericPirate",
"0x95" : "GenericIllia",
"0x96" : "GenericBern",
"0x97" : "GenericIllia",
"0x98" : "GenericBandit",
"0x99" : "GenericIlliaMercenary",
"0x9A" : "GenericIllia",
"0x9B" : "0x9B",
"0x9C" : "GenericIllia",
"0x9D" : "GenericCitizenIllia",
"0x9E" : "GenericThief",
"0x9F" : "GenericBern",
"0xA0" : "GenericBern",
"0xA1" : "GenericBern",
"0xA2" : "GenericThief",
"0xA3" : "GenericEidyna",
"0xA4" : "GenericCitizenEidyna",
"0xA5" : "GenericBanditWestIsles",
"0xA6" : "GenericEtruria",
"0xA7" : "GenericSacae",
"0xA8" : "GenericBern",
"0xA9" : "GenericDjute",
"0xAA" : "GenericBern",
"0xAB" : "GenericSacae",
"0xAC" : "GenericBern",
"0xAD" : "GenericEtruria",
"0xAE" : "GenericSacae",
"0xAF" : "GenericBern",
"0xB0" : "GenericManakete",
"0xB1" : "GenericBern",
"0xB2" : "GenericDragon",
"0xB3" : "0xB3",
"0xB4" : "0xB4",
"0xB5" : "Henning",
"0xB6" : "Scollan",
"0xB7" : "GenericBandit",
"0xB8" : "Guerrero",
"0xB9" : "Oates",
"0xBA" : "Tick",
"0xBB" : "GenericBern",
"0xBC" : "GenericSacae",
"0xBD" : "GenericBern",
"0xBE" : "Thoril",
"0xBF" : "Brakul",
"0xC0" : "Kudoka",
"0xC1" : "Marral",
"0xC2" : "Kabul",
"0xC3" : "Chan",
"0xC4" : "Peres",
"0xC5" : "GenericBern",
"0xC6" : "Windham",
"0xC7" : "GenericEtruria",
"0xC8" : "Morgan",
"0xC9" : "GenericRebel",
"0xCA" : "GenericBern",
"0xCB" : "GenericBern",
"0xCC" : "GenericBern",
"0xCD" : "0xCD",
"0xCE" : "0xCE",
"0xCF" : "0xCF",
"0xD0" : "0xD0",
"0xD1" : "0xD1",
"0xD2" : "0xD2",
"0xD3" : "0xD3",
"0xD4" : "0xD4",
"0xD5" : "0xD5",
"0xD6" : "0xD6",
"0xD7" : "0xD7",
"0xD8" : "0xD8",
"0xD9" : "0xD9",
"0xDA" : "0xDA",
"0xDB" : "0xDB",
"0xDC" : "0xDC",
"0xDD" : "0xDD",
"0xDE" : "0xDE",
"0xDF" : "0xDF",
"0xE0" : "GenericBandit",
"0xE1" : "0xE1",
"0xE2" : "0xE2",
"0xE3" : "0xE3",
"0xE4" : "0xE4",
"0xE5" : "0xE5",
"0xE6" : "0xE6",
"0xE7" : "0xE7",
"0xE8" : "0xE8",
"0xE9" : "0xE9",
"0xEA" : "0xEA",
"0xEB" : "0xEB",
"0xEC" : "0xEC",
"0xED" : "0xED",
"0xEE" : "0xEE",
"0xEF" : "0xEF",
"0xF0" : "0xF0",
"0xF1" : "0xF1",
"0xF2" : "0xF2",
"0xF3" : "0xF3",
"0xF4" : "0xF4",
"0xF5" : "0xF5",
"0xF6" : "0xF6",
"0xF7" : "0xF7",
"0xF8" : "0xF8",
"0xF9" : "0xF9",
"0xFA" : "0xFA",
"0xFB" : "0xFB",
"0xFC" : "0xFC",
"0xFD" : "0xFD",
"0xFE" : "0xFE"
}

classesList = {
    "0x00" : "Invalid",
    "0x01" : "RoyLord",
    "0x02" : "Mercenary",
    "0x03" : "MercenaryF",
    "0x04" : "Hero",
    "0x05" : "HeroF",
    "0x06" : "Myrmidon",
    "0x07" : "MyrmidonF",
    "0x08" : "Swordmaster",
    "0x09" : "SwordmasterF",
    "0x0A" : "Fighter",
    "0x0B" : "Warrior",
    "0x0C" : "Knight",
    "0x0D" : "KnightF",
    "0x0E" : "General",
    "0x0F" : "GeneralF",
    "0x10" : "Archer",
    "0x11" : "ArcherF",
    "0x12" : "Sniper",
    "0x13" : "SniperF",
    "0x14" : "Priest",
    "0x15" : "Cleric",
    "0x16" : "Bishop",
    "0x17" : "BishopF",
    "0x18" : "Mage",
    "0x19" : "MageF",
    "0x1A" : "Sage",
    "0x1B" : "SageF",
    "0x1C" : "Shaman",
    "0x1D" : "ShamanF",
    "0x1E" : "Druid",
    "0x1F" : "DruidF",
    "0x20" : "Cavalier",
    "0x21" : "CavalierF",
    "0x22" : "Paladin",
    "0x23" : "PaladinF",
    "0x24" : "Troubadour",
    "0x25" : "Valkyrie",
    "0x26" : "Nomad",
    "0x27" : "NomadF",
    "0x28" : "NomadTrooper",
    "0x29" : "NomadTrooperF",
    "0x2A" : "PegasusKnight",
    "0x2B" : "Falcoknight",
    "0x2C" : "WyvernRider",
    "0x2D" : "WyvernRiderF",
    "0x2E" : "WyvernLord",
    "0x2F" : "WyvernLordF",
    "0x30" : "Soldier",
    "0x31" : "Brigand",
    "0x32" : "Pirate",
    "0x33" : "Berserker",
    "0x34" : "Thief",
    "0x35" : "ThiefF",
    "0x36" : "Bard",
    "0x37" : "Dancer",
    "0x38" : "FireManakete",
    "0x39" : "FaeManakete",
    "0x3A" : "FireDragon",
    "0x3B" : "DivineDragon",
    "0x3C" : "DemonDragon",
    "0x3D" : "King",
    "0x3E" : "Civilian",
    "0x3F" : "CivilianF",
    "0x40" : "Child",
    "0x41" : "ChildF",
    "0x42" : "Transporter",
    "0x43" : "RoyGreatLord",
    "0x44" : "",
    "0x45" : "",
    "0x46" : "",
    "0x47" : "",
    "0x48" : "",
    "0x49" : "",
    "0x4A" : "",
    "0x4B" : "",
    "0x4C" : "",
    "0x4D" : "",
    "0x4E" : "",
    "0x4F" : "",
    "0x50" : "",
    "0x51" : "",
    "0x52" : "",
    "0x53" : "",
    "0x54" : "",
    "0x55" : "",
    "0x56" : "",
    "0x57" : "",
    "0x58" : "",
    "0x59" : "",
    "0x5A" : "",
    "0x5B" : "",
    "0x5C" : "",
    "0x5D" : "",
    "0x5E" : "",
    "0x5F" : "",
    "0x60" : "",
    "0x61" : "",
    "0x62" : "",
    "0x63" : ""
}

itemsList = {
"0x00" : None,
"0x01" : "IronSword",
"0x02" : "IronBlade",
"0x03" : "SteelSword",
"0x04" : "SilverSword",
"0x05" : "SlimSword",
"0x06" : "PoisonSword",
"0x07" : "BraveSword",
"0x08" : "LightBrand",
"0x09" : "Durandal",
"0x0A" : "Armorslayer",
"0x0B" : "Rapier",
"0x0C" : "KillingEdge",
"0x0D" : "LanceReaver",
"0x0E" : "WoDao",
"0x0F" : "BindingBlade",
"0x10" : "IronLance",
"0x11" : "SteelLance",
"0x12" : "SilverLance",
"0x13" : "SlimLance",
"0x14" : "PoisonLance",
"0x15" : "BraveLance",
"0x16" : "Javelin",
"0x17" : "Maltet",
"0x18" : "Horseslayer",
"0x19" : "KillerLance",
"0x1A" : "Axereaver",
"0x1B" : "IronAxe",
"0x1C" : "SteelAxe",
"0x1D" : "SilverAxe",
"0x1E" : "PoisonAxe",
"0x1F" : "BraveAxe",
"0x20" : "HandAxe",
"0x21" : "Armads",
"0x22" : "Hammer",
"0x23" : "KillerAxe",
"0x24" : "Swordreaver",
"0x25" : "DevilAxe",
"0x26" : "Halberd",
"0x27" : "IronBow",
"0x28" : "SteelBow",
"0x29" : "SilverBow",
"0x2A" : "PoisonBow",
"0x2B" : "KillerBow",
"0x2C" : "BraveBow",
"0x2D" : "ShortBow",
"0x2E" : "Longbow",
"0x2F" : "Mulagir",
"0x30" : "Ballista",
"0x31" : "IronBallista",
"0x32" : "KillerBallista",
"0x33" : "Fire",
"0x34" : "Thunder",
"0x35" : "Fimbulvetr",
"0x36" : "Elfire",
"0x37" : "Aircalibur",
"0x38" : "Fenrir",
"0x39" : "Bolting",
"0x3A" : "Forblaze",
"0x3B" : "Lightning",
"0x3C" : "Divine",
"0x3D" : "Purge",
"0x3E" : "Aureola",
"0x3F" : "Flux",
"0x40" : "Nosferatu",
"0x41" : "Eclipse",
"0x42" : "Apocalypse",
"0x43" : "Heal",
"0x44" : "Mend",
"0x45" : "Recover",
"0x46" : "Physic",
"0x47" : "Fortify",
"0x48" : "Warp",
"0x49" : "Rescue",
"0x4A" : "Restore",
"0x4B" : "Silence",
"0x4C" : "Sleep",
"0x4D" : "TorchStaff",
"0x4E" : "Hammerne",
"0x4F" : "",
"0x50" : "Berserk",
"0x51" : "Unlock",
"0x52" : "Barrier",
"0x53" : "Firestone",
"0x54" : "Divinestone",
"0x55" : "",
"0x56" : "SecretBook",
"0x57" : "GoddessIcon",
"0x58" : "AngelicRobe",
"0x59" : "Dragonshield",
"0x5A" : "EnergyRing",
"0x5B" : "Speedwings",
"0x5C" : "Talisman",
"0x5D" : "Boots",
"0x5E" : "BodyRing",
"0x5F" : "HeroCrest",
"0x60" : "KnightCrest",
"0x61" : "OrionsBolt",
"0x62" : "ElysianWhip",
"0x63" : "GuidingRing",
"0x64" : "ChestKey5Uses",
"0x65" : "DoorKey",
"0x66" : "",
"0x67" : "Lockpick",
"0x68" : "Vulnerary",
"0x69" : "Elixir",
"0x6A" : "PureWater",
"0x6B" : "Torch",
"0x6C" : "Antitoxin",
"0x6D" : "MemberCard",
"0x6E" : "SilverCard",
"0x6F" : "GoldIconLol",
"0x70" : "DarkBreath",
"0x71" : "Eckesachs",
"0x72" : "SteelBlade",
"0x73" : "SilverBlade",
"0x74" : "AlsSword",
"0x75" : "GantsLance",
"0x76" : "TinasStaff",
"0x77" : "SaintsStaff",
"0x78" : "Wyrmslayer",
"0x79" : "WhiteGem",
"0x7A" : "BlueGem",
"0x7B" : "RedGem",
"0x7C" : "DelphiShield",
"0x7D" : "Runesword",
"0x7E" : "Spear",
"0x7F" : "Tomahawk"
}

primaryAIsList = {
"0x00" : "AI1_InRange",
"0x01" : "AI1_InRange80",
"0x02" : "AI1_InRange50",
"0x03" : "AI1_InPlace",
"0x04" : "AI1_InPlace80",
"0x05" : "AI1_InPlace50",
"0x06" : "AI1_None",
"0x07" : "AI1_InRangeLaus",
"0x08" : "AI1_Douglas",
"0x09" : "AI1_Ballista11B",
"0x0A" : "AI1_WeirdLilina",
"0x0B" : "AI1_Gale",
"0x0C" : "AI1_GhostOfBern",
"0x0D" : "AI1_GaleSquad",
"0x0E" : "AI1_HealAllies",
'0x78' : "AI1_None" #man wtf
}

secondaryAIsList = {
"0x00" : "AI2_Charge",
"0x01" : "AI2_ChargeLaus",
"0x02" : "AI2_Douglas",
"0x03" : "AI2_DontMove",
"0x04" : "AI2_PillageAttack",
"0x05" : "AI2_PillageEscape",
"0x06" : "AI2_TwoMoves",
"0x07" : "AI2_TwoMovesLaus",
"0x08" : "AI2_0x8",
"0x09" : "AI2_Random",
"0x0A" : "AI2_0xA",
"0x0B" : "AI2_ClarineTalkToRoy",
"0x0C" : "AI2_Escape",
"0x0D" : "AI2_0xD",
"0x0E" : "AI2_0xE",
"0x0F" : "AI2_0xF",
"0x10" : "AI2_0x10",
"0x11" : "AI2_0x11",
"0x12" : "AI2_0x12",
"0x13" : "AI2_0x13",
"0x14" : "AI2_0x14",
"0x15" : "AI2_0x15",
"0x16" : "AI2_0x16",
"0x17" : "AI2_0x17",
"0x18" : "AI2_0x18"
}

recoveryAIsList = {
"000" : "RAI_50_100", #0x00
"001" : "RAI_30_80", #0x01
"010" : "RAI_10_50", #0x02
"011" : "RAI_80_100", #0x03
"100" : "RAI_NoRecovery", #0x04
}

targetAIsList = {
"00000" : "TAI_Pos", #0x00
"00001" : "TAI_HP", #0x08
"00010" : "TAI_Reckless", #0x10
"00011" : "TAI_Def", #0x18
"00100" : "TAI_DmgAcc", #0x20
"00101" : "TAI_Arch", #0x28 
"00110" : "TAI_Weird1", #0x30
"00111" : "TAI_Weird2", #0x38
"01100" : "0x60", #0x60 somehow, found on mercs that start at the caslte in 11b
"01000" : "0x40", #0x40 somehow, found on fighters that come out on the castle in 11b
"01101" : "0x68", #0x68 somehow, found on thea and her squad 10b
"01010" : "0x50" #0x50 somehow, found on a soldier in upper left of ch3
}

retreatAIsList = {
"0x00" : "AI4_Retreat",
"0x20" : "AI4_DontRetreat",
}

#filename = sys.argv[1]

# open file in read mode
#with open(filename, 'r') as f:
#    dict_reader = DictReader(f)
#    fe6units = list(dict_reader)
#
#output = []
#for daunit in fe6units:
#    output.append(CsvUnitToText(daunit))

#cwd = os.getcwd()
#for folder in os.listdir(cwd+"/Unit CSVs/"):
#    files = os.listdir(cwd+"/Unit CSVs/"+folder)
#    output = []
#    for file in files:
#        with open(cwd+"/Unit CSVs/"+folder+"/"+file, 'r') as f:
#            dict_reader = DictReader(f)
#            fe6units = list(dict_reader)

cwd = os.getcwd()
for subdir, _, files in os.walk(cwd+"/Unit CSVs/"):
    output = []
    for filename in files:
        filepath = os.path.join(subdir, filename)
        if ".csv" in filename:
            with open(filepath, 'r', encoding='utf-8') as f:
                dict_reader = DictReader(f)
                fe6units = list(dict_reader)
            output.append((filename.replace(".csv",""))+":\n")
            for unit in fe6units:
                output.append(CsvUnitToText(unit))
            output.append("UNIT\n\n")
    if len(files) != 0:
        with open(subdir+"/Units.txt", "w") as f:
            f.writelines(output)
        


#with open(filename+'.txt', 'w') as f:
#    f.writelines(output)