# misc_MSSB
General MSSB Stat Parsers I've created (these are all generally older but I remember viewing code by Pokebunny for stuff on this)

Most code here runs using StarsOffSeason5/6 statistics, they also work with older seasons but are hard coded to use those since that was the current season at the time - its also beneficial to use older seasons as they have less statisitcs overall, and can be ran faster

All functions here take a Username input, which can be empty allowing all data to be used, otherwise it will only pull data from 'username'

# stats.py

ba_opb_comp: Compares the BA to the OPB of the character, and outputs the difference

strikeout_rate: Finds the strikeout% of each character, and outputs the total average, along with each characters strikeout%

xbh_rate: Finds the percent amount of hits by each character that are eXtra Base Hits (Doubles, Triples, Homeruns), and outputs the percentages

BABIP: Finds the Batting Average on Balls In Play for each character, and outputs the average

# ab-rbi

Inputs are Username (same as listed up top) and a selection of Stars Off or Stars On (different gamemode selection, code works the same either way)

Finds the rate of At Bats per each RBI the character gets, and outputs the total rate for all characters, and outputs the average per character, sorted by lowest to highest rate

# walk-rate

Inputs are Username (same as listed up top) and a selection of Stars Off or Stars On (different gamemode selection, code works the same either way)

Finds the rate of at bats per each characters walk (4 Balls or Hit By Pitch) and outputs the total rate for all characters together, and outputs each character's numerical walks and walk percent. Can be sorted by highest walk rate, but sorting gets less accurate the further down the list.

# ab-hr

Inputs are Username (same as listed up top) and a selection of Stars Off or Stars On (different gamemode selection, code works the same either way)

Finds the rate of At Bats per each Homerun the character gets, and outputs the total rate for all characters, and average per character, sorted by lowest to highest rate
