import requests
def ba_obp_comp(user):
    url = "https://api.projectrio.app/stats/?exclude_pitching=1&exclude_fielding=1&exclude_misc=1&by_char=1&tag=starsoffseason6&tag=starsoffseason5"

    if user != "":
        url += "&username=" + user

    response = requests.get(url).json()

    stat_dump = response["Stats"]
    # print(stat_dump)

    char_list = []
    ba_list = []
    obp_list = []

    for character in stat_dump:
        char_list.append(character)
        stats = stat_dump[character]["Batting"]
        pa = stats["summary_at_bats"] + stats["summary_walks_hbp"] + stats["summary_walks_bb"] + stats["summary_sac_flys"]
        avg = round(stats["summary_hits"] / stats["summary_at_bats"], 3)
        obp = round((stats["summary_hits"] + stats["summary_walks_hbp"] + stats["summary_walks_bb"]) / pa, 3)

        avg = str(avg) + ("0" * (5 - len(str(avg))))
        obp = str(obp) + ("0" * (5 - len(str(obp))))
        ba_list.append(avg)
        obp_list.append(obp)

    max_len = 0
    for num in range(0, len(char_list)):
        if int(len(char_list[num])) > max_len:
            max_len = len(char_list[num])
            
    for num in range(0, len(char_list)):
        # want 13 characters to be taken up (name + one extra space)
        offset = " " * abs((int(len(char_list[num])) - max_len))
        difference = round(float(obp_list[num]) - float(ba_list[num]), 3)

        sign = ""
        if difference > 0:
            sign = "+"
        if difference == 0:
            sign = "=" 

        difference = sign + str(difference) + ("0" * (5 - len(str(difference))))
        print(f"{char_list[num]}{offset}| BA: {ba_list[num]}, OBP: {obp_list[num]}, Difference: {difference}")

def strikeout_rate(user):
    url = "https://api.projectrio.app/stats/?exclude_pitching=1&exclude_fielding=1&exclude_misc=1&by_char=1&tag=starsoffseason6&tag=starsoffseason5"

    full_response = requests.get(url).json()

    if user != "":
        url += "&username=" + user
        response = requests.get(url).json()
        compare = True
    else:
        response = full_response
        compare = False
    

    stat_dump = response["Stats"]
    # print(stat_dump)

    char_list = []
    k_list = []
    full_k_list = []

    for character in stat_dump:
        char_list.append(character)
        stats = stat_dump[character]["Batting"]
        pa = stats["summary_at_bats"] + stats["summary_walks_hbp"] + stats["summary_walks_bb"] + stats["summary_sac_flys"]
        k = stats["summary_strikeouts"]
        k_rate = k / pa
        k_list.append(k_rate)
    if compare:
        full_stat_dump = full_response["Stats"]
        for character in full_stat_dump:
            stats = full_stat_dump[character]["Batting"]
            pa = stats["summary_at_bats"] + stats["summary_walks_hbp"] + stats["summary_walks_bb"] + stats["summary_sac_flys"]
            k = stats["summary_strikeouts"]
            k_rate = k / pa
            full_k_list.append(k_rate)

    max_len = 0
    for num in range(0, len(char_list)):
        if int(len(char_list[num])) > max_len:
            max_len = len(char_list[num])

    total = sum(k_list) / len(k_list)
    print(f"Total: {total:.1%}") 
    if compare:
        real_total = total - (sum(full_k_list) / len(full_k_list))
        sign = ""
        if real_total > 0:
            sign = "+"
        if real_total == 0:
            sign = "=" 

        print(f"({sign}{real_total:.1%})")
        print("",end="")
          
    for num in range(0, len(char_list)):
        # want 13 characters to be taken up (name + one extra space)
        offset = " " * abs((int(len(char_list[num])) - max_len))
        space = ""
        if k_list[num] < .1:
            space = " "
            
        print(f"{char_list[num]}{offset}| {k_list[num]:.1%}{space}", end=" ")
        if compare:
            diff = k_list[num] - full_k_list[num]

            sign = ""
            if diff > 0:
                sign = "+"
            if diff == 0:
                sign = "=" 

            print(f"({sign}{diff:.1%})")
        else:
            print()
        print("",end="")       

# maybe add league wide compare to xbh_rate
def xbh_rate(user):
    url = "https://api.projectrio.app/stats/?exclude_pitching=1&exclude_fielding=1&exclude_misc=1&by_char=1&tag=starsoffseason6&tag=starsoffseason5"

    if user != "":
        url += "&username=" + user

    response = requests.get(url).json()

    stat_dump = response["Stats"]
    # print(stat_dump)

    char_list = []
    xbh_list = []

    for character in stat_dump:
        char_list.append(character)
        stats = stat_dump[character]["Batting"]
        try: xbh = round(((stats["summary_doubles"] + stats["summary_triples"] + stats["summary_homeruns"]) / stats["summary_hits"] * 100), 1)
        except ZeroDivisionError:
            xbh = 0.0
        xbh = str(xbh) + ("0" * (4 - len(str(xbh))))

        xbh_list.append(xbh)

    max_len = 0
    for num in range(0, len(char_list)):
        if int(len(char_list[num])) > max_len:
            max_len = len(char_list[num])
            
    for num in range(0, len(char_list)):
        # want 13 characters to be taken up (name + one extra space)
        offset = " " * abs((int(len(char_list[num])) - max_len))
        '''difference = round(float(obp_list[num]) - float(xbh_list[num]), 3)

        sign = ""
        if difference > 0:
            sign = "+"
        if difference == 0:
            sign = "=" 

        difference = sign + str(difference) + ("0" * (5 - len(str(difference))))'''
        print(f"{char_list[num]}{offset}| XBH%: {xbh_list[num]}%")

def babip(user):
    url = "https://api.projectrio.app/stats/?exclude_pitching=1&exclude_fielding=1&exclude_misc=1&by_char=1&tag=starsoffseason6&tag=starsoffseason5"

    if user != "":
        url += "&username=" + user

    response = requests.get(url).json()

    stat_dump = response["Stats"]
    # print(stat_dump)

    char_list = []
    babip_list = []

    for character in stat_dump:
        char_list.append(character)
        stats = stat_dump[character]["Batting"]
        babip = round( (stats["summary_hits"] - stats["summary_homeruns"]) / ( stats["summary_at_bats"] - stats["summary_strikeouts"] - stats["summary_homeruns"] + stats["summary_sac_flys"] ), 3)

        babip = str(babip) + ("0" * (5 - len(str(babip))))
        babip_list.append(babip)

    max_len = 0
    for num in range(0, len(char_list)):
        if int(len(char_list[num])) > max_len:
            max_len = len(char_list[num])
            
    for num in range(0, len(char_list)):
        # want 13 characters to be taken up (name + one extra space)
        offset = " " * abs((int(len(char_list[num])) - max_len))
        '''difference = round(float(obp_list[num]) - float(ba_list[num]), 3)

        sign = ""
        if difference > 0:
            sign = "+"
        if difference == 0:
            sign = "=" 

        difference = sign + str(difference) + ("0" * (5 - len(str(difference))))'''
        print(f"{char_list[num]}{offset}| BABIP: {babip_list[num]}")

def main():
    print("Enter username")
    username = input()

    print("Want to do BA:OBP Comp?")
    yn = input()
    if yn == "1":
        ba_obp_comp(username)

    print("Want to do Strikeout Rate?")
    yn = input()
    if yn == "1":
        strikeout_rate(username)

    print("Want to do XBH%?")
    yn = input()
    if yn == "1":
        xbh_rate(username)

    print("Want to do BABIP?")
    yn = input()
    if yn == "1":
        babip(username)
    return

main()

