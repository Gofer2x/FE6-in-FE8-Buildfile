An attempt at an (FEBuilder-friendly) recreation of FE6 in FE8's engine.

Requires "FE8_clean.gba" (sha1: c25b145e37456171ada4b0d440bf88a19f4d509f) and "FE6.gba" (either original or translated will work) in the root directory.

Requires Python 3 and a copy of FEBuilder in Tools/FEBuilderGBA.

To build, run "_MAKE HACK_full.cmd", which will build "myHack.gba". Afterwards run "_FullSoundInsertion.bat" to build "myHackWithSound.gba" (using FEBuilder's Sound Import function), which will be the proper finished ROM. It will take a few minutes though.

For information about how to insert new data, various helper scripts used etc. please read [GUIDE.md](GUIDE.md).

Based on [EasyBuildFile](https://github.com/MysticOCE/EasyBuildfile) by MysticOCE.
