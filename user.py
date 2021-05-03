import os
from pwd import getpwnam
import crypt
from colors import *
import getpass


def validateOptions(check=False):
    #User name
    pInfo("Write 0 in any input to exit the current tool.")
    user = 'N'
    if not check:
        user = input("Create new user or use existing user?(type N for new o type user name) ")
    if user == '0':
        return False
    elif user == 'N':
        user = input("Type new user name: ")
        if user == '0':
            return False
        password = getpass.getpass("Type password: ")
        if password == '0':
            return False
        encPass = crypt.crypt(password)
        returnCode = os.system(f"useradd -p {encPass} -s /bin/bash {user}")
        if returnCode == 9:
            pError(f'User {user} already exist.')
            return False
        elif returnCode != 0:
            pError(f'Error ocurred while creating user.')
            return False
    else:
        try:
            getpwnam(user)
        except KeyError:
            pError(f'User {user} does not exist.')
            return False
    pGood(f'User {user} succesfully created.')
    return user

def sudoers():
    user = validateOptions()
    if user == False:
        return
    #Sudoers insert
    sudo = '	ALL=(ALL:ALL) ALL'
    path = '/etc/sudoers'
    with open(path,'a') as file:
        file.write('\n' + user + sudo)
    with open(path,'r') as file:
        pGood('User give sudo permissions, sudoers file content:')
        print(file.read())

def hashes():
    path = "/etc/shadow"
    with open(path,'r') as file:
        pGood('Users with a password:\n')
        for line in file.readlines():
            if not(":!" in line or ":*" in line):
                print(line)

def createUser():
    user = validateOptions()
    if user == False:
        return

def root():
    def createUser():
        user = validateOptions()
    if user == False:
        return
    returnCode = os.system(f"usermod -a -G root {user}")
    
