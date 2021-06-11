import re
import string 
import random
import os
from colors import *

ipv4 = r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def isIpv4(ip):
    if(re.search(ipv4, ip)):
        return True
    else:
        return False

def stringGenerator(size=6):
    return ''.join(random.choices(string.ascii_letters, k=size))

def addCron(cmd, condition = "@reboot",user="root"):
    job = condition + " bash -c '" + cmd + "'"
    cron = f'(crontab -l; echo "{job}" ) | crontab -'
    pGood(f'Cronjob {job} added.')
    os.system(cron)