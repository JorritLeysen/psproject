from riotwatcher import LolWatcher, TftWatcher
import json

# global variables
api_key = 'RGAPI-97b4a4b4-30c5-432c-b989-9b656fd518d4'
leagueWatcher = LolWatcher(api_key)
tftWatcher = TftWatcher(api_key)
my_region = 'euw1'

# input
# declaration
all_matches = {}

# enter account name
name = input("Enter your TFT summoner name (type 'done' if you've entered everything): ")

# let user choose account
while name != "done":

    acc = leagueWatcher.summoner.by_name(my_region, name)
    print(acc)

    tft_stats = tftWatcher.league.by_summoner(my_region, acc['id'])
    print(tft_stats)

    # enter amount of matches
    amount = input("Enter the amount of matches: ")
    tft_matches = tftWatcher.match.by_puuid("EUROPE", acc['puuid'], amount)

    # add info of matches to dictionary
    for matchID in tft_matches:
        match = tftWatcher.match.by_id("EUROPE", matchID)
        info = match['info']
        all_matches[matchID] = info

    name = input("Enter your TFT summoner name (type 'done' if you've entered everything): ")

# output
# create json object from dictionary
json = json.dumps(all_matches)

# open file for writing, "w"
f = open("matches.json", "w")

# write json object to file
f.write(json)

# close file
f.close()
