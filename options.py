import menus
import ssh
import user
import reverse
import software

def optionsSSH():
    i = -1
    while i != 0:
        i = menus.menuSSH()
        if i == 1:
            ssh.copyKey()
        elif i == 2:
            ssh.getKey()

def optionsRev():
    i = -1
    while i != 0:
        i = menus.menuRev()
        if i == 1:
            reverse.reverse()
        elif i == 2:
            reverse.cronBoot()
        elif i == 3:
            reverse.cronLoop()
        elif i == 4:
            reverse.cronUser()


def optionsUser():
    i = -1
    while i != 0:
        i = menus.menuUser()
        if i == 1:
            user.sudoers()
        elif i == 2:
            user.hashes()
        elif i == 3:
            user.createUser()
        elif i == 4:
            user.root()          

def optionsSoftware():
    i = -1
    while i != 0:
        i = menus.menuSoftware()
        if i == 1:
            software.setuid()
        elif i == 2:
            software.backApt()                  