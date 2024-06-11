import requests, json, time, threading, os
import pyfiglet
from colorama import Fore, init

# warna
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
yellow = Fore.LIGHTYELLOW_EX
white = Fore.WHITE
bl = Fore.BLACK

record = [
    {'Key': {'sourceCity': 'MLG', 'destinationCity': 'SBY', 'routePassed': ['SBY', 'MLG'], 'activityRewards': None}, 'Value': 30 * 8.33},
    {'Key': {'sourceCity': 'SBY', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'SBY'], 'activityRewards': None}, 'Value': 60 * 8.33},
    {'Key': {'sourceCity': 'MLG', 'destinationCity': 'SMG', 'routePassed': ['SMG', 'MLG'], 'activityRewards': None}, 'Value': 12 * 8.33},
    {'Key': {'sourceCity': 'SMG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SMG'], 'activityRewards': None}, 'Value': 50 * 8.33},
    {'Key': {'sourceCity': 'SBY', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'SBY'], 'activityRewards': None}, 'Value': 10 * 8.33},
    {'Key': {'sourceCity': 'MLG', 'destinationCity': 'CBN', 'routePassed': ['CBN', 'MLG'], 'activityRewards': None}, 'Value': 5 * 8.33},
    {'Key': {'sourceCity': 'CBN', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'CBN'], 'activityRewards': None}, 'Value': 45 * 8.33},
    {'Key': {'sourceCity': 'SMG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SMG'], 'activityRewards': None}, 'Value': 9 * 8.33},
    {'Key': {'sourceCity': 'SBY', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'SBY'], 'activityRewards': None}, 'Value': 5 * 8.33},
    {'Key': {'sourceCity': 'MLG', 'destinationCity': 'JKT', 'routePassed': ['JKT', 'MLG'], 'activityRewards': None}, 'Value': 3 * 8.33},
    {'Key': {'sourceCity': 'JKT', 'destinationCity': 'P_Merak', 'routePassed': ['P_Merak', 'JKT'], 'activityRewards': None}, 'Value': 45 * 8.33}
]

print(f"{yellow}--------------------------------------------------------------------------------")
print(f"{red}██╗░██████╗██╗░░░██╗██████╗░██████╗░░█████╗░██████╗░████████╗░██████╗░██████╗")
print(f"{red}██║██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔════╝░")
print(f"{red}██║╚█████╗░██║░░░██║██████╔╝██████╔╝██║░░██║██████╔╝░░░██║░░░╚█████╗░██║░░██╗░")
print(f"{red}██║░╚═══██╗██║░░░██║██╔═══╝░██╔═══╝░██║░░██║██╔══██╗░░░██║░░░░╚═══██╗██║░░╚██╗")
print(f"{red}██║██████╔╝╚██████╔╝██║░░░░░██║░░░░░╚█████╔╝██║░░██║░░░██║░░░██████╔╝╚██████╔╝")
print(f"{red}╚═╝╚═════╝░░╚═════╝░╚═╝░░░░░╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░░╚═════╝░")
print(f"{yellow}--------------------------------------------------------------------------------")
print(f"{red}██████╗░██╗░░░██╗░██████╗░██████╗██╗██████╗░")
print(f"{red}██╔══██╗██║░░░██║██╔════╝██╔════╝██║██╔══██╗")
print(f"{red}██████╦╝██║░░░██║╚█████╗░╚█████╗░██║██║░░██║")
print(f"{red}██╔══██╗██║░░░██║░╚═══██╗░╚═══██╗██║██║░░██║")
print(f"{red}██████╦╝╚██████╔╝██████╔╝██████╔╝██║██████╔╝")
print(f"{red}╚═════╝░░╚═════╝░╚═════╝░╚═════╝░╚═╝╚═════╝░")
print(f"{green}Tools Created By : @iSupportSG")
print(f"{green}Credit : Thanks To All !")
print(f"{green}Community : @TeamiRaid")
print(f"{yellow}--------------------------------------------------------------------------------")
auth = input(f'{red}[{white}#{red}] {red}Enter X-Authorization : {white} ')

headers = {
    'User-Agent': 'UnityEngine-Unity; Version: 2018.4.26f1',
    'X-ReportErrorAsSuccess': 'true',
    'X-PlayFabSDK': 'UnitySDK-2.20.170411',
    'X-Authorization': '',
    'Content-Type': 'application/json',
    'Content-Length': '157',
    'Host': '4ae9.playfabapi.com'
}
headers['X-Authorization'] = auth
counter = 0

def create_mission():
    game_data = '{"FunctionName":"PlayCareer","FunctionParameter":{"cities":["MLG","SBY","SMG","CBN","JKT","P_Merak","P_Bakauheni","LPG","PLB","JMB","PBR"]},"RevisionSelection":"Live","SpecificRevision":null,"GeneratePlayStreamEvent":false}'
    response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=game_data).text
    if response != '':
        parser = json.loads(response)
        if parser['code'] == 401:
            return None
        elif parser['code'] == 200:
            data = parser['data']
            if "apiError" in str(data):
                return None
            else:
                carrer = data['FunctionResult']['careerSession']
                return carrer
    else:
        return None

def skip_mission(token):
    data = json.dumps({"FunctionName":"FarePayment","FunctionParameter":{"records":record,"bonus":True,"careerToken":token,"activityRewardToken":"{\"rewards\":[]}"},"RevisionSelection":"Live","SpecificRevision":None,"GeneratePlayStreamEvent":False})
    response = requests.post('https://4ae9.playfabapi.com/Client/ExecuteCloudScript', headers=headers, data=data).text
    if response != '':
        parser = json.loads(response)
        if parser['code'] == 401:
            pass
        elif parser['code'] == 200:
            backend_data = parser['data']
            if "apiError" in str(backend_data):
                pass
            else:
                logs = backend_data['Logs']
                msg = logs[len(logs)-1]['Message']
                print(f'[{token}] {msg}')
    
def pass_mission():
    carrer = create_mission()
    if carrer != None:    
        token = carrer['token']
        skip_mission(token)

while 1:
    pass_mission()
    if counter == 1:
        counter = 0
        time.sleep(1)
    else:
        counter += 1
