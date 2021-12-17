
import os
try:
    import uuid
except:
    os.system('pip install uuid')
try:
    import sys
except:
    os.system('pip install sys')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os,sys
        from time import sleep
        import webbrowser
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4

B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White 

try:
	import pathlib
except:
	os.system('pip install pathlib')
try:
    code='# Enc by :UAP-TEAM\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))(\'\',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),"exec"))(%s,compile))'
    computer=0
    file=input(f'\n{R}File : {G}')
    count=int(input(f'\n{R}Count : {G}'))
    if(count<300):
        out=input(f'\n {R}Output : {G}')
        read1=open(file).read()
        repr1=repr(zlib.compress(read1.encode('utf-8')))
        new1=open(out, 'w')
        new1.write(code % repr1)
        new1.close()
        while(count>=computer):
        	read2=open(out).read()
        	repr2=repr(zlib.compress(read2.encode('utf-8')))
        	new2=open(out, 'w')
        	new2.write(code % repr2)
        	new2.close()
        	computer+=1
        	print('\n\033[1;97mobfuscating file at | '+Y+f'{computer}')
        	print(f'\n\033[1;92mencrypt success | '+Y+f'{out}')
except ValueError:
    print('\033[1;31mEnter a number in the count')
except KeyboardInterrupt:
	print('\n\033[1;31mBe stopped')
v=input(P+"prees enter to resume to UAP-TEAM:  ")
if v =="":
    os.system('python my_projects.py')