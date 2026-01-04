# Welcome Enjoy 
#__________________________________________#
import os,sys,random,string,json,uuid,base64,requests,httpx,time,datetime,platform,subprocess,re,shutil
from time import sleep
import os
import uuid
import json
import requests
import platform
from random import choice as ch
from concurrent.futures import ThreadPoolExecutor
try:
	import mechanize
	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
except:
	os.system('pip install mechanize')
try:
	import requests
except:
	os.system('pip install requests')
try:
	from bs4 import BeautifulSoup as bs
except:
	os.system('pip install bs4')
try:
	open('/sdcard/....file.txt','w').write(' ')
except Exception as e:
	print(e)
	print('ALLOW TERMUX PERMISSIONS ! AND RUN AGAIN ')
	os.system('termux-setup-storage')
#__________________________________________#
owner = 'achraf'
tool = 'FILE KADIX'
version = '0.2'
bit = platform.architecture()[0]
#__________________________________________#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
#__________________________________________#
W = "\033[1;37m";G = "\033[38;5;46m";G1 = "\033[38;5;47m";G2 = "\033[38;5;48m";G3 = "\033[38;5;49m";G4 = "\033[38;5;50m";R = "\033[38;5;196m";R3 = "\033[38;5;1m";R1 = "\033[38;5;202m";R2 = "\033[38;5;203m";C = "\033[38;5;4m";K="\033[38;5;15m";A="\033[38;5;248m";LG="\033[38;5;195m";A1="\033[38;5;250m";A2="\033[38;5;251m";A3="\033[38;5;252m";A4="\033[38;5;253m";A5="\033[38;5;254m";B="\033[38;5;153m";rad="\033[1;31m"
logo = '\x1b[1;34m';logo1 = '\x1b[38;5;48m';logo2 = '\x1b[38;5;156m';logo3 = '\x1b[38;5;157m';logo4 = '\x1b[38;5;158m'
colors = ['\x1b[1;90m','\x1b[1;91m','\x1b[1;92m','\x1b[1;93m','\x1b[1;94m','\x1b[1;95m','\x1b[1;96m','\x1b[1;97m','\x1b[38;5;208m']

def color():
    random_color=ch(['\x1b[1;91m','\x1b[1;92m','\x1b[1;93m','\x1b[1;94m','\x1b[1;95m'])
    return random_color
#__________________________________________#
z = f'{W}[{G}✓{W}] '
age = f'{W}[{G}';pore = f'{W}] '
#__________________________________________#
sys.stdout.write('\x1b]2; FILE KADIX TOOL🤍\x07')
#__________________________________________#
line = f'{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
logo = f"""{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            {R}|{G}ERROR AGAIN BACK WITH NEW LOOK{R}|{G}
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 {logo}  .----------------.   .----------------. 
| .--------------. | | .--------------. |
| |  ________    | | | |   ________   | |
| | |_   ___ `.  | | | |  |  __   _|  | |
| |   | |   `. \ | | | |  |_/  / /    | |
| |   | |    | | | | | |     .'.' _   | |
| |  _| |___.' / | | | |   _/ /__/ |  | |
| | |________.'  | | | |  |________|  | |
| |              | | | |              | |
| '--------------' | | '--------------' |
 '----------------'   '----------------'  {W}┃ TOOL     {R}| {G}{tool}
 {logo}       {W}┃ OWNER    {R}| {G}{owner}
 {logo}    {W}┃ DATE     {R}| {G}{date}
 {logo}       {W}┃ DEVICE   {R}| {G}{bit}
 {logo}   {W}┃ VERSION  {R}| {G}{version}
{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"""
#__________________________________________#
xuid = str(uuid.uuid4())
#__________________________________________#
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    print(f'{age}1{pore}START TOKEN GETTER\n{age}2{pore}START UNLIMITED FILE MAKE WITH 1 ID\n{age}3{pore}REMOVE DUPLICATE\n{age}4{pore}REPORT BUG\n{age}5{pore}EXIT TERMINAL\n{line}')    
    ch = input(f'{z}CHOOSE : {G}')    
    if ch in ['1', 'a', 'A']:login()
    elif ch in ['2', 'b', 'B']:filee()
    elif ch in ['3', 'c', 'C']:remove_duplicates()
    elif ch in ['4', 'd', 'D']:os.system('xdg-open https://www.facebook.com/bryxxpogi');sleep(4);print(f'{z}{G}THANKS FOR YOUR FEEDBACK....!');sleep(2);print(f'{z}{G}RESTARTING THE TOOL.......!');sleep(0.5);main()
    elif ch in ['5', 'e', 'E']:exit(f'{line}\n{z}{G}THANKS FOR USING OUR TOOL.....!')
    else:print(f'{z}{R}SORRY, WRONG INPUT....!');sleep(3);print(f'{z}{G}RESTARTING THE TOOL.....!');sleep(2);main()
#__________________________________________#
def login():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(logo)
	print(f'{age}1{pore}GET TOKEN FROM UID & PASSWORD\n{line}')
	ch = input(f'{z}CHOOSE : {G}')
	if ch in ['1','a','A']:BRYX_KING()
	else:print(f'{z}{R}SORRY WRONG INPUT....!');sleep(3);print(f'{z}{G}RESTARTING THE TOOL.....!');sleep(2);login()
#__________________________________________#
def BRYX_KING():
	os.system('cls' if os.name == 'nt' else 'clear')
	print(logo)
	emails = input(f"USER ID/EMAIL : ")
	passwords = input(f"PASSWORD : ")
	print(f'{line}')
	cuser(emails,passwords)
#__________________________________________#
import requests
import uuid
import random

def cuser(emails,passwords):
    accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
    data = {
        'adid': f'{uuid.uuid4()}',
        'format': 'json',
        'device_id': f'{uuid.uuid4()}',
        'cpl': 'true',
        'family_device_id': f'{uuid.uuid4()}',
        'credentials_type': 'device_based_login_password',
        'error_detail_type': 'button_with_disabled',
        'source': 'device_based_login',
        'email': emails,
        'password': passwords,
        'access_token': accessToken,
        'generate_session_cookies': '1',
        'meta_inf_fbmeta': '',
        'advertiser_id': f'{uuid.uuid4()}',
        'currently_logged_in_userid': '0',
        'locale': 'en_US',
        'client_country_code': 'US',
        'method': 'auth.login',
        'fb_api_req_friendly_name': 'authenticate',
        'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
        'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    }
    headers = {
        'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'graph.facebook.com',
        'X-FB-Net-HNI': str(random.randint(10000, 99999)),
        'X-FB-SIM-HNI': str(random.randint(10000, 99999)),
        'X-FB-Connection-Type': 'MOBILE.LTE',
        'X-Tigon-Is-Retry': 'False',
        'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
        'x-fb-device-group': str(random.randint(1000, 9999)),
        'X-FB-Friendly-Name': 'ViewerReactionsMutation',
        'X-FB-Request-Analytics-Tags': 'graphservice',
        'X-FB-HTTP-Engine': 'Liger',
        'X-FB-Client-IP': 'True',
        'X-FB-Connection-Bandwidth': str(random.randint(20000000, 30000000)),
        'X-FB-Server-Cluster': 'True',
        'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
    }
    pos = requests.post("https://b-graph.facebook.com/auth/login", headers=headers, data=data, allow_redirects=False).json()
    if "session_key" in pos:
        cookies = ';'.join(i['name'] + '=' + i['value'] for i in pos['session_cookies'])
        c_user_value = [i['value'] for i in pos['session_cookies'] if i['name'] == 'c_user'][0]
        print(f'LOGIN SUCCESSFULLY!\n{line}\nUSER ID/EMAIL  : {emails}\n{line}\nPASSWORD  : {passwords}\n{line}\nTOKEN  : {pos["access_token"]}\n{line}')
        input(f"{z}{W}PRESS ENTER TO GO BACK IN MAIN MENU")
        main()
    else:
        print(f"{z}{R}INVALID/CHECKPOINT\n{line}")
        input(f"{z}{W}PRESS ENTER TO GO BACK IN MAIN MENU")
        main()
#__________________________________________#
def filee():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    token = str(input('TOKEN : '))
    print(f'{line}')
    try:
    	limit = int(input("HOW MANY IDS YOU WANT TO ADD? "))
    except ValueError:
    	print(f"{z}{R}PLEASE ENTER A VALID NUMBER.")
    	return
    print(f'{line}')
    file_name = input('FILE NAME : ')
    print(f'{line}')
    sepr = input('DO YOU WANT TO SEPARATE IDS (y/n): ')
    print(f'{line}')
    siid = []
    sep = []
    if sepr == 'y':
    	sep.append('y')
    	print("EXAMPLE: 100087, 100088 ETC")
    	print(f'{line}')
    	try:
    		sl = int(input('HOW MANY LINKS TO GRAB: '))
    	except ValueError:
    		sl = 1
    	for el in range(sl):
    		print(f'{line}')
    		sid = input(f'PUT LINK {el+1}: ')
    		print(f'{line}')
    		siid.append(sid)
    elif sepr == 'n':
    	sep.append('n')
    else:
    	print(f"{z}{R}INVALID CHOICE. DEFAULTING TO 'N'.")
    	sep.append('n')
    uid_list = []
    for i in range(limit):
    	uid = input(f"PUT ID {i+1}: ")
    	print(f'{line}')
    	uid_list.append(uid)
    with ThreadPoolExecutor(max_workers=100) as executor:
    	for uid in uid_list:
    	     executor.submit(ONE__,token,uid,file_name)
    print(f'{line}\nEXTRACTED SUCCESSFULLY DONE\nYOUR DUMP IDS SAVED IN : {file_name}\n{line}')
    exit()
#__________________________________________#
xuid = str(uuid.uuid4())
#__________________________________________#
def ONE__(token,uid,file_name):
    headers = {
        'Host': 'graph.facebook.com',
        'Priority': 'u=3, i',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Graphql-Client-Library': 'graphservice',
        'X-Fb-Privacy-Context': 'c0000000ebe595b4',
        'X-Fb-Background-State': '1',
        'User-Agent': "[FBAN/FB4A;FBAV/196.0.0.29.99;FBPN/com.facebook.katana;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]','[FBAN/FB4A;FBAV/196.0.0.29.99;FBPN/com.facebook.katana;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'X-Fb-Net-Hni': '47001',
        'X-Fb-Sim-Hni': '47001',
        'Authorization': f'OAuth {token}',
        'X-Fb-Connection-Type': 'MOBILE.LTE',
        'X-Fb-Device-Group': '2572',
        'X-Tigon-Is-Retry': 'False',
        'X-Fb-Friendly-Name': 'FriendListContentQuery',
        'X-Fb-Request-Analytics-Tags': 'graphservice',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
    }
    var = {"profile_id":uid,
           "profile_image_size":96,
           "friends_paginating_first":20}
    data = {
        'client_doc_id': '36431518109556416924349542983',
        'method': 'post',
        'locale': 'en_US',
        'pretty': 'false',
        'format': 'json',
        'purpose': 'fetch',
        'variables': json.dumps(var),
        'fb_api_req_friendly_name': 'FriendListContentQuery',
        'fb_api_caller_class': 'graphservice',
        'fb_api_analytics_tags': '["At_Connection","GraphServices"]',
        'server_timestamps': 'true',
    }
    try:
        response = requests.post('https://graph.facebook.com/graphql', headers=headers, data=data).json()
        for friend in response['data']['user']['friends']['edges']:
            friend_id = friend['node']['id']
            friend_name = friend['node']['name']
            print(f"{z}{ch(colors)}SUCCESSFULLY EXTRACTED ID : {friend_id}\033[0m")
            with open(file_name, 'a', encoding='utf-8') as f:
                f.write(friend_id+'|'+friend_name+'\n')
        e_c = response['data']['user']['friends']['page_info']['end_cursor']
    except Exception:
        exit('ERROR')
    return two9(e_c,token,uid,file_name)
#__________________________________________#
def two9(e_c,token,uid,file_name):
    sys.stdout.write(f'''\r\x1b[1;97m[ERROR-FILE] | [{color()}{str(len(open(file_name, 'r').readlines()))}\x1b[1;97m]\r''')
    sys.stdout.flush()
    headers = {
        'Host': 'graph.facebook.com',
        'Priority': 'u=3, i',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Graphql-Client-Library': 'graphservice',
        'X-Fb-Privacy-Context': 'c0000000ebe595b4',
        'X-Fb-Background-State': '1',
        'User-Agent': "[FBAN/FB4A;FBAV/196.0.0.29.99;FBPN/com.facebook.katana;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]','[FBAN/FB4A;FBAV/196.0.0.29.99;FBPN/com.facebook.katana;FBLC/en_US;FBBV/135374479;FBCR/SMART;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]",
        'X-Fb-Net-Hni': '47001',
        'X-Fb-Sim-Hni': '47001',
        'Authorization': f'OAuth {token}',
        'X-Fb-Connection-Type': 'MOBILE.LTE',
        'X-Fb-Device-Group': '2572',
        'X-Tigon-Is-Retry': 'False',
        'X-Fb-Friendly-Name': 'FriendListContentQuery',
        'X-Fb-Request-Analytics-Tags': 'graphservice',
        'X-Fb-Http-Engine': 'Liger',
        'X-Fb-Client-Ip': 'True',
        'X-Fb-Server-Cluster': 'True',
    }
    var = {
    "friends_paginating_at_stream_use_customized_batch": False,
    "profile_image_size": 96,
    "paginationPK": uid,
    "profile_id": uid,
    "friends_paginating_first": 20,
    "friends_paginating_after_cursor": e_c
    }
    data = {
        "client_doc_id": "24605340978403080720500702641",
        "method": "post",
        "locale": "user",
        "pretty": "false",
        "format": "json",
        "purpose": "fetch",
        "fb_api_client_context": '{"load_next_page_counter":1,"client_connection_size":20}',
        "variables": json.dumps(var),
        "fb_api_req_friendly_name": "FriendListContentQuery_At_Connection_Pagination_User_friends_paginating",
        "fb_api_caller_class": "ConnectionManager",
        "fb_api_analytics_tags": '["At_Connectikon","GraphServices"]',
        "client_trace_id": xuid,
        "server_timestamps": "true"
    }
    response = requests.post('https://graph.facebook.com/graphql', headers=headers, data=data).json()
    friends = response['data']['node']['friends']['edges']
    for friend in friends:
        print(f"{z}{ch(colors)}SUCCESSFULLY EXTRACTED ID : {friend['node']['id']}\033[0m")
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(friend['node']['id'] + '|' + friend['node']['name'] + '\n')
    e_c = response['data']['node']['friends']['page_info']['end_cursor']
    return two9(e_c,token,uid,file_name)
#__________________________________________#
def remove_duplicates():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
    file_path = input('FILE NAME : ')
    try:
        with open(file_path,'r') as file:
            lines = file.readlines()
        unique_lines = set(lines)
        with open(file_path,'w') as file:
            file.writelines(unique_lines)
        print(f'{line}')
        print(f'{z}{G}REMOVE DONE')
        print(f'{line}')
        input(f"{z}{W}PRESS ENTER TO GO BACK IN MAIN MENU")
        main()
    except FileNotFoundError:
        print(f'{line}')
        print(f'{z}{R}NO FILE FOUND')
        exit()
#__________________________________________#
if __name__=='__main__':
	main()
