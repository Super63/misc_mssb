import requests

print("Enter username of player (blank for all stats):")
user = input()
print("Enter '0' for stars-off data; '1' for stars-on")
stars = int(input())

url = "https://api.projectrio.app/stats/?exclude_pitching=1&exclude_fielding=1&exclude_misc=1"
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
o_pa = stats["plate_appearances"]
o_hr = stats["homeruns"]
o_hr_pa = o_pa / o_hr
print("HRs / AB/HR")
print("OVERALL (" + str(o_pa) + " PA): " + str(o_hr) + " HR / " + "{:.2f}".format(o_hr_pa) + " AB/HR")
# print()
url += "&by_char=1"

response = requests.get(url).json()
sorted_char_list = []
keys = dict(response["Stats"])
for key in keys:
    try:
        (response["Stats"][key]["Batting"]["plate_appearances"] / response["Stats"][key]["Batting"]["homeruns"])
    except KeyError:
        del response["Stats"][key]
    except ZeroDivisionError:
        del response["Stats"][key]
try:
    sorted_char_list = sorted(response["Stats"].keys(), key=lambda x: (response["Stats"][x]["Batting"]["homeruns"] / response["Stats"][x]["Batting"]["plate_appearances"]), reverse=True)
except KeyError:
    print("Sort Error :(")
    sorted_char_list = response["Stats"].keys()

# print(response)
for char in sorted_char_list:
    char_stats = response["Stats"][char]["Batting"]
    #print(char_stats)
    pa = char_stats["plate_appearances"]
    hr = char_stats["homeruns"]
    abhr = round(o_hr_pa / (pa / hr), 2) * 100
    if user == "":
        if pa > 100:
            print(char + " (" + str(pa) + " PA): " + str(hr) + " HR / " + "{:.2f}".format(pa / hr) + " AB/HR ")#/ " + "{:.0f}".format(abhr) + " AB/HR+")
    else:
        print(char + " (" + str(pa) + " PA): " + str(hr) + " HR / " + "{:.2f}".format(pa / hr) + " AB/HR")# / " + "{:.0f}".format(abhr) + " AB/HR+")
