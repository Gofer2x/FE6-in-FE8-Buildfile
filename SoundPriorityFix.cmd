copy myHackWithMusicBroken.gba myHackWithMusic.gba
cd "%~dp0EventAssembler"
ColorzCore A FE8 "-output:%~dp0myHackWithMusic.gba" "-input:%~dp0SoundPriorityFixEA.event" "--build-times"
