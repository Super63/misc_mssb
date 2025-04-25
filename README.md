# misc_MSSB
General MSSB Stat Parsers I've created (these are all generally older but I remember viewing code by Pokebunny for stuff on this)

Most code here runs using StarsOffSeason5/6 statistics, they also work with older seasons but are hard coded to use those since that was the current season at the time

All functions here take a Username input, which can be empty allowing all data to be used, otherwise it will only pull data from 'username'

# stats.py

ba_opb_comp: Compares the BA to the OPB of the character, and outputs the difference

strikeout_rate: Finds the strikeout% of each character, and outputs the total average, along with each characters strikeout%

xbh_rate: Finds the percent amount of hits by each character that are eXtra Base Hits (Doubles, Triples, Homeruns), and outputs the percentages

BABIP: Finds the Batting Average on Balls In Play for each character, and outputs the average

# ab-rbi

Inputs are Username (same as listed up top) and a selection of Stars Off or Stars On (different gamemode selection, code works the same either way)

Finds the rate of At Bats per each RBI the character gets, and outputs the average per character, sorted by lowest to highest rate

