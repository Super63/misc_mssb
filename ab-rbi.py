import requests

print("Enter username of player (blank for all stats):")
user = input()
print("Enter '0' for stars-off data; '1' for stars-on")
stars = int(input())

url = "https://projectrio-api-1.api.projectrio.app/stats/?exclude_pitching=1&exclude_fielding=1&exclude_misc=1"
if stars == 0:
    url += "&tag=StarsOffSeason6"
elif stars == 1:
    url += "&tag=StarsOnSeason6"

all_response = requests.get(url).json()
all_char_response = requests.get(url + "&by_char=1").json()

if user != "":
    url += "&username=" + user

response = requests.get(url).json()

# print(response)

stats = response["Stats"]["Batting"]
o_pa = stats["summary_at_bats"]
o_rbi = stats["summary_rbi"]
o_rbi_pa = o_pa / o_rbi
print("RBIs / AB/RBI")
print("OVERALL (" + str(o_pa) + " PA): " + str(o_rbi) + " RBIs / " + "{:.2f}".format(o_rbi_pa) + " AB/RBI")
url += "&by_char=1"

response = requests.get(url).json()
sorted_char_list = []
keys = dict(response["Stats"])
for key in keys:
    try:
        (response["Stats"][key]["Batting"]["summary_at_bats"] / response["Stats"][key]["Batting"]["summary_rbi"])
    except KeyError:
        del response["Stats"][key]
    except ZeroDivisionError:
        del response["Stats"][key]
try:
    sorted_char_list = sorted(response["Stats"].keys(), key=lambda x: (response["Stats"][x]["Batting"]["summary_rbi"] / response["Stats"][x]["Batting"]["summary_at_bats"]), reverse=True)
except KeyError:
    print("Sort Error :(")
    sorted_char_list = response["Stats"].keys()

# print(response)
for char in sorted_char_list:
    char_stats = response["Stats"][char]["Batting"]
    pa = char_stats["summary_at_bats"]
    rbi = char_stats["summary_rbi"]
    if user == "":
        if pa > 100:
            print(char + " (" + str(pa) + " PA): " + str(rbi) + " / " + "{:.2f}".format(pa / rbi) + " AB/RBI ")# / " + "{:.0f}".format(abrbi) + " AB/RBI+")
    else:
        print(char + " (" + str(pa) + " PA): " + str(rbi) + " / " + "{:.2f}".format(pa / rbi) + " AB/RBI ") # / " + "{:.0f}".format(abrbi) + " AB/RBI+")
