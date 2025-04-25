import requests

print("Enter username of player (blank for all stats):") # WALK% SORTED IS STILL BROKEN
user = input()
print("Enter '0' for stars-off data; '1' for stars-on")
stars = int(input())
print("Sort by Walks or Walk Rate? 0/1 ")
sort = int(input())

url = "https://projectrio-api-1.api.projectrio.app/stats/?&exclude_fielding=1&exclude_pitching=1&exculde_misc=1"

if stars == 0:
    url += "&tag=netplaysuperstars21"
elif stars == 1:
    url += "&tag=StarsOnSeason6"

all_response = requests.get(url).json()
all_char_response = requests.get(url + "&by_char=1").json()

if user != "":
    url += "&username=" + user

response = requests.get(url).json()

# print(response)

stats = response["Stats"]["Batting"]
o_bb = stats["summary_walks_bb"] + stats["summary_walks_hbp"]
o_pa = stats["summary_at_bats"] + o_bb + stats["summary_sac_flys"]
o_bb_pa = o_pa / o_bb
print("User:", user)
print("BBs / AB/BB")
print("OVERALL (" + str(o_pa) + " PA): " + str(o_bb) + " BBs / " + "{:.2f}".format(o_bb_pa) + " AB/BB")
url += "&by_char=1"

response = requests.get(url).json()
sorted_char_list = []
keys = dict(response["Stats"])
for key in keys:
    sum_at_bats = response["Stats"][key]["Batting"]["summary_at_bats"]
    sum_walks = response["Stats"][key]["Batting"]["summary_walks_bb"] + response["Stats"][key]["Batting"]["summary_walks_hbp"]
    sum_sacfly = response["Stats"][key]["Batting"]["summary_sac_flys"]

    try:
        ((sum_at_bats + sum_walks + sum_sacfly) / sum_walks)
    except KeyError:
        del response["Stats"][key]
    except ZeroDivisionError:
        del response["Stats"][key]

if sort == 1: #walk rate sort
    try:
        sorted_char_list = sorted(response["Stats"].keys(), key=lambda x: ((response["Stats"][x]["Batting"]["summary_walks_hbp"] + response["Stats"][x]["Batting"]["summary_walks_bb"]) / (response["Stats"][x]["Batting"]["summary_walks_hbp"] + response["Stats"][x]["Batting"]["summary_sac_flys"] + response["Stats"][x]["Batting"]["summary_at_bats"] + response["Stats"][x]["Batting"]["summary_walks_bb"])), reverse=True)
    except KeyError:
        print("Sort Error :(")
        sorted_char_list = response["Stats"].keys()
else: #walk number sort
    try:
        sorted_char_list = sorted(response["Stats"].keys(), key=lambda x: (response["Stats"][x]["Batting"]["summary_walks_hbp"] + response["Stats"][x]["Batting"]["summary_walks_bb"]), reverse=True)
    except KeyError:
        print("Sort Error :(")
        sorted_char_list = response["Stats"].keys()

# print(response)
for char in sorted_char_list:
    char_stats = response["Stats"][char]["Batting"]
    pa = char_stats["summary_at_bats"] + char_stats["summary_walks_bb"] + char_stats["summary_walks_hbp"] + stats["summary_sac_flys"]
    bb = char_stats["summary_walks_hbp"] + char_stats["summary_walks_bb"]
    bbp = round(bb / pa, 3) * 100

    if user == "":
        if pa > 100:
            print(char + " (" + str(pa) + " PA): " + str(bb) + " / " + "{:.1f}".format(bbp) + "%")
    else:
        print(char + " (" + str(pa) + " PA): " + str(bb) + " / " + "{:.1f}".format(bbp) + "%")
