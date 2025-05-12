set idsFromtables=Tools\IDsFromTables.py
set enumerate=Tools\Enumerate\Enumerate.py
%idsFromtables% Tables\NightmareModules\CharacterAndClass\CharacterTable.csv Definitions\Generated\CharacterIDs.event %enumerate% Character --oneIndexed
%idsFromtables% Tables\NightmareModules\CharacterAndClass\ClassTable.csv Definitions\Generated\ClassIDs.event Class %enumerate% --oneIndexed --ignoreFirstItem
%idsFromtables% Tables\NightmareModules\Item\ItemTable.csv Definitions\Generated\ItemIDs.event Item %enumerate% --oneIndexed --ignoreFirstItem
%idsFromtables% Tables\NightmareModules\ChapterData\ChapterData.csv Definitions\Generated\ChapterIDs.event Chapter %enumerate%
%idsFromtables% Tables\NightmareModules\WorldMap\Nodes.csv Definitions\Generated\WMNodeIDs.event Node %enumerate%
%idsFromtables% Tables\NightmareModules\WorldMap\Roads.csv Definitions\Generated\WMRoadIDs.event Road %enumerate%