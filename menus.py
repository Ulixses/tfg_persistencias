from colors import *
from util import *
def askOption(first, last):
    i = -1
    while i < first or i > last:
        i = input(f"Choose an option [{first},{last}]: ")
        print()
        if not isInt(i):
            pWarning("Not a number.")
            i = -1
        i = int(i)
    return i

def menuBasic():
    menu = """
1. SSH persistences.
2. Reverse shell persistences.
3. User persistences.
4. Software persistance
0. Exit.
    """
    print(menu)
    return askOption(0, 4)

def menuSSH():
    menu = """1. Copy key.
2. Get private key.
0. Back.
    """
    pWarning("Only works if the machine is running ssh sever.")
    print(menu)
    return askOption(0, 2)

def menuUser():
    menu = """
1. Create sudoers user.
2. Obtain /etc/shadow hashes.
3. Create basic user (Less noisy).
4. Create root user.
0. Back.
    """
    print(menu)
    return askOption(0, 4)

def menuRev():
    menu = """
1. Create Reverse Shell.
2. Create cronjob on boot.
3. Create cronjob always running.
4. Create a custum cronjob.
0. Back.
    """
    print(menu)
    return askOption(0, 4)


def menuSoftware():
    menu = """
1. Create setuid binary.
2. APT module backdoor
0. Back.
    """
    print(menu)
    return askOption(0, 2)