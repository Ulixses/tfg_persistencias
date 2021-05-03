class colors:
    OK = '\033[1;92m' #GREEN
    WARNING = '\033[1;93m' #YELLOW
    ERROR = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
    HEADER = '\033[94m'
    INFO = '\033[1;95m' #BLUE

def pGood(s):
    print(colors.OK + s + colors.RESET)

def pWarning(s):
    print(colors.WARNING + s + colors.RESET)

def pError(s):
    print(colors.ERROR + s + colors.RESET)

def pInfo(s):
    print(colors.INFO + s + colors.RESET)

def pTest(s):
    print(colors.HEADER + s + colors.RESET)

