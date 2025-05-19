EA Configs
===============
The file [Config.event](Config.event) contains a few definitions that you can uncomment/comment out to enable and disable various behaviors (not like most of them do anything at the moment though...).

Table Readers
===============
There is a Python script (TableUpdater.py in the Tools folder) that can take the names out of the leftmost column of a Nightmare table and using Enumerate (another script) autogenerate EA definitions. It's ran on various tables through _UpdateIDsFromTables.cmd in the root folder.

Supports
===============
Due to engine limitations, Roy and Lilina cannot have all of their supports (they have 11, FE8 engine has a limit of 7). There is a script to let you choose which of their supports are cut in [Tables/EA/Generated](Tables/EA/Generated).

It also supports adding new supports if you add them in the support data dict in the script itself. Just follow the naming convention of the already present vanilla supports' text data.

Mugs
===============

To insert new Mugs/Portraits, go into [Graphics/Mugs](Graphics/Mugs).

Drop your mug's png file (Have it named like "Character.png") into the "Png" folder, and run "_BatchPortraitFormatter.cmd". 
 
Afterwards, open "MasterMugInstallerGenerator.py" in a text editor. This is where you'll set up how your mug should be installed.
 
Add your mug's name to the mugsData dict, but only put it after the "SecretShop" entry. Otherwise it will mess up vendor menus.
 
The template is:
 
	"Name": [mouthX,mouthY,eyeX,eyeY]
     
If your mug doesn't have a mini version, also add it to the "noMinis" array. Order doesn't matter there.
 
If it's a palette swap, add it to the "paletteSwaps" dict. How it works is described there.
 
When done, run "MasterMugInstallerGenerator.py". Press enter when it finishes. It will have generated all the relevant data imports, definitions, and also put the various LoadMugs into ParseDefinitions in the main Text folder.
