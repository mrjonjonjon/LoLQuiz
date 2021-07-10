import requests

from riotwatcher import LolWatcher, ApiError
import pandas as pd
import matplotlib.pyplot as plt
import random






lol_watcher = LolWatcher('RGAPI-6046f816-35c0-4de2-a7f0-c463dc877804')
my_region = 'na1'
me = lol_watcher.summoner.by_name(my_region, 'XxQuakerOatsxX')

my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])

# fetch last match detail
# check league's latest version
latest = lol_watcher.data_dragon.versions_for_region(my_region)['n']['champion']
# Lets get some champions static information
static_champ_list = lol_watcher.data_dragon.champions(latest, False, 'en_US')

# build champid : champname map
champ_dict = {}
blurb_dict={}
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_dict[int(row['key'])] = row['id']
#print(champ_dict)
#build champname : chamdescription map

for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    blurb_dict[key] = row['blurb'].replace(key,'???')

#print(blurb_dict)
my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])

'''
for matchnum in range(10,12):
    match = my_matches['matches'][matchnum]
    match_detail = lol_watcher.match.by_id(my_region, match['gameId'])

    for pid in match_detail['participantIdentities']:
        if pid['player']['summonerName'] == 'XxQuakerOatsxX':
            mypid = pid['participantId']
            break

    for part in match_detail['participants']:
             if part['participantId']==mypid:
                mystats=part['stats']
                #print("you played",champ_dict[part['championId']],matchnum,"game(s) ago")
                #print("your cs/min was",round((mystats['totalMinionsKilled']+mystats['neutralMinionsKilled'])/(match_detail['gameDuration']/60),1))
                break
'''
while True:
    randchampname=random.choice(list(blurb_dict.keys()))
    print(blurb_dict[randchampname])
    answer=input("guess the champ:")
    if answer.lower()==randchampname.lower():
        print('correct')
    else:
        print('incorrect. answer is ',randchampname)

    keep_running = input("Another? (y/n): ")
    if keep_running=='n':
        break
'''
todo:
fix kogmaw vs kog'maw
fix nunu vs nunuand willlump
fix mundo vs drmundo
'''