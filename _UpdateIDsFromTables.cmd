set idsFromTables=Tools\IDsFromTables.py
set enumerate=Tools\Enumerate\Enumerate.py
%idsFromTables% Tables\NightmareModules\CharacterAndClass\CharacterTable.csv Definitions\Generated\CharacterIDs.event %enumerate% Character --oneIndexed
%idsFromTables% Tables\NightmareModules\CharacterAndClass\ClassTable.csv Definitions\Generated\ClassIDs.event Class %enumerate% --oneIndexed --ignoreFirstItem
%idsFromTables% Tables\NightmareModules\Item\ItemTable.csv Definitions\Generated\ItemIDs.event Item %enumerate% --oneIndexed --ignoreFirstItem
%idsFromTables% Tables\NightmareModules\ChapterData\ChapterData.csv Definitions\Generated\ChapterIDs.event Chapter %enumerate%
%idsFromTables% Tables\NightmareModules\WorldMap\Nodes.csv Definitions\Generated\WMNodeIDs.event Node %enumerate%
%idsFromTables% Tables\NightmareModules\WorldMap\Roads.csv Definitions\Generated\WMRoadIDs.event Road %enumerate%