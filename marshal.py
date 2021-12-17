
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
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
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
nice=("")
import os, sys, time, base64, marshal, zlib, py_compile
R = '\x1b[1;31m'
G = '\x1b[1;32m'
Y = '\x1b[1;33m'
B = '\x1b[1;34m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.01)
print('')
slowprint(G + ' Launching Encryption Tool...')
time.sleep(2)
print('')
file = input(G + 'File name' + C + ' > ' + Y)
print('')
c = input(G + ' Output File Name' + C + ' > ' + Y)
print('')
slowprint(G + ' Encrypting...')
print('')
fileopen = open(file).read()
sa = compile(fileopen, 'dg', 'exec')
sb = marshal.dumps(sa)
sc = zlib.compress(sb)
sd = base64.b85encode(sc)
b = '#https://t.me/U_A_P_TEAM\nimport marshal,zlibbase64\nexec(marshal.loads(zlib.decompress(base64.b85decode(' + repr(sd) + '))))'
d = open(c, 'w')
d.write(b)
d.close()
time.sleep(3)
slowprint(G + ' Encryption Completed...')
time.sleep(3)
print('')
print(G + ' Output File Name: ' + Y, c)
print('')
print(W)
os.system('cd /sdcard/UAP-TEAM')
#os.system('python my_project.py')
os.system('python my_projects.py')