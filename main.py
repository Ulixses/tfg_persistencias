#!/usr/bin/env python

import base64, os
import menus,options
from colors import *



def main():
    pInfo("Welcome to the persistance tool designed for unix systems.")
    i = -1
    if os.geteuid()==0:
        pGood("Running as root.")
    else:
        pError("User is not root.")
        return
    while i != 0:
        i = menus.menuBasic()
        if i == 1:
            options.optionsSSH()
        elif i == 2:
            options.optionsRev()
        elif i == 3:
            options.optionsUser()
        elif i == 4:
            options.optionsSoftware()
    
if __name__ == '__main__':
    main()