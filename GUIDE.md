modifiable supports

config.event in root (doesn't have an affect yet)


Somethign about table readers

Something about mugs and

GRAPHICS:
    To insert new Mugs/Portraits, go into Graphics/Mugs.
	Drop your mug's png file (Have it named like "Character.png") into the "Png" folder, and run "_BatchPortraitFormatter.cmd". 
	Afterwards, open "MasterMugInstallerGenerator.py" in a text editor. This is where you'll set up how your mug should be installed.
	Add your mug's name to the mugsData dict, but only put it after the "SecretShop" entry. Otherwise it will mess up vendor menus.
	The template is:
	    "Name": [mouthX,mouthY,eyeX,eyeY]
	If your mug doesn't have a mini version, also add it to the "noMinis" list. Order doesn't matter there.
	If it's a palette swap, add it to the "paletteSwaps" dict. How it works is described there.
	When done, run "Master Mug Installer Generator.py". Press enter when it finishes. It will have generated all the relevant data imports, definitions, and also put the various LoadMugs into ParseDefinitions in the main Text folder.
