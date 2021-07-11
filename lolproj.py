import requests

from riotwatcher import LolWatcher, ApiError
import pandas as pd
import matplotlib.pyplot as plt
import random
from PIL import Image
import requests
from io import BytesIO
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import re





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

def testquote():
    randchampname = random.choice(list(lore_dict.keys()))
    print(quote_dict[randchampname][random.choice(range(0,len(quote_dict[randchampname])))])
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
quote_dict={}
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

ssl._create_default_https_context = ssl._create_unverified_context
for key in static_champ_list['data']:
    addtourl=key
    if addtourl=='AurelionSol':
        addtourl='Aurelion_Sol'
    elif addtourl=='Chogath':
        addtourl='Cho%27Gath'
    elif addtourl=='DrMundo':
        addtourl='Dr._Mundo'
    elif addtourl=='JarvanIV':
        addtourl='Jarvan_IV'
    elif addtourl=='Kaisa':
        addtourl='Kai%27Sa'
    elif addtourl=='Khazix':
        addtourl='Kha%27Zix'
    elif addtourl=='KogMaw':
        addtourl='Kog%27Maw'
    elif addtourl=='Leblanc':
        addtourl='LeBlanc'
    elif addtourl=='LeeSin':
        addtourl='Lee_Sin'
    elif addtourl=='MissFortune':
        addtourl='Miss_Fortune'
    elif addtourl=='MasterYi':
        addtourl='Master_Yi'
    elif addtourl=='MonkeyKing':
        addtourl='Wukong'
    elif addtourl=='Velkoz':
        addtourl='Vel%27Koz'
    elif addtourl=='RekSai':
        addtourl='Rek%27Sai'
    elif addtourl=='TahmKench':
        addtourl='Tahm_Kench'
    elif addtourl=='TwistedFate':
        addtourl='Twisted_Fate'
    elif addtourl=='XinZhao':
        addtourl='Xin_Zhao'
    url = "https://leagueoflegends.fandom.com/wiki/"+addtourl+"/LoL/Audio"

    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    pattern = '["][a-zA-Z. ]*["]'
    m = re.findall(pattern, text)
    quote_dict[key] = m

#print(quote_dict)





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
    testquote()
    keep_running = input("Another? (y/n): ")
    if keep_running =='n':
        break
'''
todo:
fix kogmaw vs kog'maw
fix nunu vs nunu and willlump
fix mundo vs drmundo
fix master yi vs masteryi vs yi
fix tahmkench vs tahm kench
fix xinzhao vs xin zhao
kha'zix vs khazix
morgana and kayle splash show both champs
nonvoicelines occasionally enclosed in parentheses- e.g "draven laughs"
'''
