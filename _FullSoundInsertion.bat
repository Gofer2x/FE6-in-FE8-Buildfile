set genSoundScriptPath=Tools\SoundScripts\GenerateSoundBat.py
set generatedBatPath=_GeneratedSoundInsertionAndFix.bat
set csvPath=Tools\SoundScripts\FE6toFE8Sounds.csv
set febPath=Tools\FEBuilderGBA\FEBuilderGBA.exe
set fe6Path=FE6.gba
set myHackWMusicPath=myHackWithMusic.gba
set prioFixEAPath=Tools\SoundScripts\SoundPriorityFixEA.event




cd %~dp0

copy %~dp0myHack.gba %myHackWMusicPath%

echo Generating sound insertion .bat.

call %genSoundScriptPath% %generatedBatPath% %csvPath% %febPath% %fe6Path% %myHackWMusicPath% %prioFixEAPath%

echo Running sound insertion .bat.

call %~dp0%generatedBatPath%

pause