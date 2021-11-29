from colorama import Fore, Style
from datetime import datetime

def getDate():
        return datetime.today().strftime('%Y-%m-%d')

def printMessage(level, message):
    if level == "debug": 
        print(Fore.WHITE 
            + str(datetime.now()) 
            + " [DEBUG] " 
            + str(message) 
            + Style.RESET_ALL)
    elif level == "warning":
        print(Fore.YELLOW 
            + str(datetime.now()) 
            + " [WARNING] " 
            + str(message)
            + Style.RESET_ALL)
    elif level == "error":
        print(Fore.RED 
            + str(datetime.now()) 
            + " [ERROR] " 
            + str(message) 
            + Style.RESET_ALL)
    elif level == "success":
        print(Fore.GREEN 
            + str(datetime.now()) 
            + " [SUCCESS] " 
            + str(message) 
            + Style.RESET_ALL)