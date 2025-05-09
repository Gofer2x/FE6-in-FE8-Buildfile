cd %~dp0

copy %~dp0myHack.gba myHackWithMusic.gba

echo Generating sound insertion .bat.

call Tools\SoundScripts\GenerateSoundBat.py _GeneratedSoundInsertionAndFix.bat Tools\SoundScripts\FE6toFE8Sounds.csv Tools\FEBuilderGBA\FEBuilderGBA.exe FE6.gba myHackWithMusic.gba Tools\SoundScripts\SoundPriorityFixEA.event

REM echo Running sound insertion .bat.

REM call %~dp0_GeneratedSoundInsertionAndFix.bat

pause