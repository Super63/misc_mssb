import json
import os
import requests


player = str(input("Enter player name (Leave blank for all): "))
empty = 1
base_url = "https://projectrio-api-1.api.projectrio.app/stats/?exclude_batting=1&exclude_fielding=1&exclude_pitching=1"
url = "https://projectrio-api-1.api.projectrio.app/stats/?exclude_batting=1&exclude_fielding=1&exclude_pitching=1&by_char=1"
tag = "&tag=mbachampionsleague2024"
# tags - netplaysuperstars16 npss17 npss18 slice2024superstarsoff
# 16 bracket only &start_time=1707274800
# 17 bracket only &start_time=1713309948
# npss16 no walrus i think https://projectrio-api-1.api.projectrio.app/stats/?exclude_batting=1&exclude_fielding=1&exclude_pitching=1&start_time=1707242962&exclude_username=Walrus
# npss18 is VERY incomplete data (55/80)
# top20 = ["seth", "remkey", "super63", "faceman", "mori", "hellzhero", "samn", "cezarito", "bignick", "balambtransfer", "pokebunny", "toastyy", "bennyokay", "legendarybolt", "dyla81", "clutch1908", "mattgree", "flatbread", "amongusblaster", "melthrax"]

if player != "":
    base_url += "&username=" + player
    url += "&username=" + player
else:
    empty = 2
url += tag

response = requests.get(url).json()
stats = response["Stats"]
# print(stats)
sorted_char_list = sorted(response["Stats"].keys(), key=lambda x: response["Stats"][x]["Misc"]["game_appearances"], reverse=True)
pick_rate_list = []

for char in sorted_char_list:
    char_stats = response["Stats"][char]["Misc"]
    away_wins = char_stats["away_wins"]
    away_losses = char_stats["away_loses"]
    home_wins = char_stats["home_wins"]
    home_losses = char_stats["home_loses"]
    game_appearances = char_stats["game_appearances"]

    # Totals
    total_wins = away_wins + home_wins
    total_losses = away_losses + home_losses
    total = total_wins + total_losses

    # Calculations
    try: win_percentage = round((total_wins / total) * 100, 2)
    except ZeroDivisionError:
        win_percentage = 0



    # Store Stats
    pick_rate_list.append([char, total_wins, total, win_percentage])

# this is gross
toadcount = 0
shyguycount = 0
koopacount = 0
paracount = 0
magcount = 0
bonescount = 0
nokicount = 0
piantacount = 0
brocount = 0
toadlist = ["", 0, 0, 0]
shyguylist = ["", 0, 0, 0]
koopalist = ["", 0, 0, 0]
paralist = ["", 0, 0, 0]
maglist = ["", 0, 0, 0]
boneslist = ["", 0, 0, 0]
nokilist = ["", 0, 0, 0]
piantalist = ["", 0, 0, 0]
brolist = ["", 0, 0, 0]

total_games = 0
total_wins = 0
for item in pick_rate_list:
    if item[0].find("(") != -1:
        if item[0].find("Toad(") != -1:
            toadcount += 1
            toadlist[0] = "Toad(All)"
            toadlist[1] += item[1]
            toadlist[2] += item[2]
            toadlist[3] = round((toadlist[1] / toadlist[2]) * 100, 2)
        if item[0].find("Shy Guy") != -1:
            shyguycount += 1
            shyguylist[0] = "Shy Guy(All)"
            shyguylist[1] += item[1]
            shyguylist[2] += item[2]
            shyguylist[3] = round((shyguylist[1] / shyguylist[2]) * 100, 2)
        if item[0].find("Koopa") != -1:
            koopacount += 1
            koopalist[0] = "Koopa(All)"
            koopalist[1] += item[1]
            koopalist[2] += item[2]
            koopalist[3] = round((koopalist[1] / koopalist[2]) * 100, 2)
        if item[0].find("Paratroopa") != -1:
            paracount += 1
            paralist[0] = "Paratroopa(All)"
            paralist[1] += item[1]
            paralist[2] += item[2]
            paralist[3] = round((paralist[1] / paralist[2]) * 100, 2)
        if item[0].find("Magikoopa") != -1:
            magcount += 1
            maglist[0] = "Magikoopa(All)"
            maglist[1] += item[1]
            maglist[2] += item[2]
            maglist[3] = round((maglist[1] / maglist[2]) * 100, 2)
        if item[0].find("Dry Bones") != -1:
            bonescount += 1
            boneslist[0] = "Dry Bones(All)"
            boneslist[1] += item[1]
            boneslist[2] += item[2]
            boneslist[3] = round((boneslist[1] / boneslist[2]) * 100, 2)
        if item[0].find("Noki") != -1:
            nokicount += 1
            nokilist[0] = "Noki(All)"
            nokilist[1] += item[1]
            nokilist[2] += item[2]
            nokilist[3] = round((nokilist[1] / nokilist[2]) * 100, 2)
        if item[0].find("Pianta") != -1:
            piantacount += 1
            piantalist[0] = "Pianta(All)"
            piantalist[1] += item[1]
            piantalist[2] += item[2]
            piantalist[3] = round((piantalist[1] / piantalist[2]) * 100, 2)
        if item[0].find("Bro") != -1:
            brocount += 1
            brolist[0] = "Bro(All)"
            brolist[1] += item[1]
            brolist[2] += item[2]
            brolist[3] = round((brolist[1] / brolist[2]) * 100, 2)

for item in pick_rate_list:
    total_games += item[2] / 9
    total_wins += item[1] / 9

total_wins = round(total_wins, 0)
total_games = round(total_games, 0) / empty

if toadcount > 1:
    pick_rate_list.append(toadlist)
if shyguycount > 1:
    pick_rate_list.append(shyguylist)
if koopacount > 1:
    pick_rate_list.append(koopalist)
if paracount > 1:
    pick_rate_list.append(paralist)
if magcount > 1:
    pick_rate_list.append(maglist)
if bonescount > 1:
    pick_rate_list.append(boneslist)
if nokicount > 1:
    pick_rate_list.append(nokilist)
if piantacount > 1:
    pick_rate_list.append(piantalist)
if brocount > 1:
    pick_rate_list.append(brolist)


if player == "":
    total_wr = "N/A"
    used_wr = 50
else:
    total_wr = round((total_wins/total_games)*100,2)
    used_wr = total_wr

for item in pick_rate_list:
    item.append(round((item[2] / total_games) * 100, 2))

for item in pick_rate_list:
    try: item.insert(4, round(item[3] - used_wr, 2))
    except TypeError:
        pass

sorted_main_list = sorted(pick_rate_list, key=lambda x: x[5], reverse=True)

print('User:', player)
sorted_main_list.insert(0,["Character", "Wins", "Games", "Win%", "W%+-", "Pick "],)
sorted_main_list.insert(1,["Total", int(total_wins), int(total_games), total_wr, "N/A", "N/A"],)

one = True
two = True

for character in sorted_main_list:
    spaces0 = 1
    spaces1 = 1
    spaces2 = 1
    spaces3 = 3
    spaces4 = 1
    spaces0r = ""
    spaces1r = ""
    spaces2r = ""
    spaces3r = ""
    spaces4r = ""
    trail = "%"
    sign3 = ""
    if len(character[0]) < 17:
        spaces0 += (17 - len(character[0]))
    if len(str(character[1])) < 7:
        spaces1 += (7 - len(str(character[1])))
    if len(str(character[2])) < 7:
        spaces2 += (7 - len(str(character[2])))
    if len(str(character[3])) < 8:
        spaces3 += (8 - len(str(character[3])))
    if len(str(character[4])) < 8:
        spaces4 += (8 - len(str(character[4])))
    for x in range(0, spaces0):
        spaces0r += " "
    for x in range(0, spaces1):
        spaces1r += " "
    for x in range(0, spaces2):
        spaces2r += " "
    for x in range(0, spaces3):
        spaces3r += " "
    for x in range(0, spaces4):
        spaces4r += " "
    try:
        if character[4] < 0:
            spaces3r = spaces3r[:-1]
        else:
            spaces4r = spaces4r[:-1]
    except TypeError:
        pass

    if one:
        trail = ""
        one = False
    else:
        if two:
            trail = ""
            two = False
            if player != "":
                sign3 = "%"
                spaces3r = spaces3r[:-1]
        else:
            sign3 = "%"
            spaces3r = spaces3r[:-1]

    print(str(character[0]) + spaces0r + str(character[1])+ spaces1r + str(character[2])+ spaces2r + str(character[3]) + sign3 + spaces3r + str(character[4]) + trail + spaces4r + str(character[5]) + trail)
stadium_names = ["Mario Stadium:", "Bowser Castle:", "Wario Palace:", "Yoshi Park:", "Peach Garden:", "DK Jungle:"]
stadium_list = []
win = []
loss = []
home_wr = []
home_record = []
#by stadium
for num in range(0,6):
    turl = base_url + tag + "&stadium=" + str(num)
    try:
        res = requests.get(turl).json()
        if player == "":
            stadium_list.append(res["Stats"]["Misc"]["away_loses"] + res["Stats"]["Misc"]["away_wins"])
        else:
            stadium_list.append(res["Stats"]["Misc"]["game_appearances"])
            if res["Stats"]["Misc"]["game_appearances"] / 2 > total_games:
                win.append(0)
                loss.append(0)
                stadium_list[num] = 0
            else:
                win.append(res["Stats"]["Misc"]["home_wins"] + res["Stats"]["Misc"]["away_wins"])
                loss.append(res["Stats"]["Misc"]["home_loses"] + res["Stats"]["Misc"]["away_loses"])
    except requests.exceptions.JSONDecodeError:
        stadium_list.append(0)
        win.append(0)
        loss.append(0)
    try: home_wr.append(round((res["Stats"]["Misc"]["home_wins"] / (res["Stats"]["Misc"]["home_wins"] + res["Stats"]["Misc"]["home_loses"])) * 100, 2))
    except ZeroDivisionError:
        home_wr.append("-")
    home_record.append(str(res["Stats"]["Misc"]["home_wins"]) + "-" + str(res["Stats"]["Misc"]["home_loses"]))
print("---")
for number in range(0, 6):
    if player != "":
        try: stadium_winrate = " " + str(round(win[number] / (win[number] + loss[number]) * 100, 2)) + "%"
        except ZeroDivisionError:
            stadium_winrate = " N/A"
    else:
        stadium_winrate = ""
    if stadium_list[number] == 0:
        printed_home_winrate = ""
    else:
        printed_home_winrate = "- Home WR: " + str(home_wr[number]) + "% " + "(" + home_record[number] + ")"

    print(stadium_names[number], str(stadium_list[number]) + " -" + stadium_winrate, printed_home_winrate)
