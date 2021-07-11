import requests

from riotwatcher import LolWatcher, ApiError
import pandas as pd
import matplotlib.pyplot as plt
import random
from PIL import Image
import requests
from io import BytesIO

def showimage(champname):
    url = image_dict[champname]
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()


def testimage():
    randchampname = random.choice(list(lore_dict.keys()))
    showimage(randchampname)

    answer = input("guess the champ:")
    if answer.lower() == randchampname.lower():
        print('correct')
    else:
        print('incorrect. answer is ', randchampname)


def testability():
    randchampname = random.choice(list(lore_dict.keys()))
    print(ability_dict[randchampname][random.choice([0, 1, 2, 3])])
    answer = input("guess the champ:")
    if answer.lower() == randchampname.lower():
        print('correct')
    else:
        print('incorrect. answer is ', randchampname)

def testlore():
    randchampname = random.choice(list(lore_dict.keys()))
    print(lore_dict[randchampname])
    answer = input("guess the champ:")
    if answer.lower() == randchampname.lower():
        print('correct')
    else:
        print('incorrect. answer is ', randchampname)

lol_watcher = LolWatcher('RGAPI-6046f816-35c0-4de2-a7f0-c463dc877804')
my_region = 'na1'
me = lol_watcher.summoner.by_name(my_region, 'XxQuakerOatsxX')

my_matches = lol_watcher.match.matchlist_by_account(my_region, me['accountId'])

# fetch last match detail
# check league's latest version
latest = lol_watcher.data_dragon.versions_for_region(my_region)['n']['champion']
# Lets get some champions static information
static_champ_list = lol_watcher.data_dragon.champions(latest, True, 'en_US')
static_item_list = lol_watcher.data_dragon.items(latest)

#print(static_champ_list)

# build champid : champname map
champ_dict = {}
lore_dict = {}
ability_dict = {}
image_dict={}
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_dict[int(row['key'])] = row['id']
#print(champ_dict)
#build champname : chamdescription map

for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    lore_dict[key] = row['lore'].replace(key,'???')

#build champname:[Qname,Wname,Ename,Rname] map
for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    ability_list = [row['spells'][0]['name'],row['spells'][1]['name'],row['spells'][2]['name'],row['spells'][3]['name']]
    ability_dict[key] = ability_list

for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    image_dict[key] = 'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'+key+'_0.jpg'







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
    testability()
    testlore()
    testimage()
    keep_running = input("Another? (y/n): ")
    if keep_running =='n':
        break
'''
todo:
fix kogmaw vs kog'maw
fix nunu vs nunu and willlump
fix mundo vs drmundo
fix master yi vs masteryi vs yi
'''
