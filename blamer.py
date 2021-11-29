import argparse
from colorama import Fore, Style
from modules.translate import translate
from modules.tor import check_tor
from modules.logging import printMessage

header = Fore.YELLOW + """
__________.__                               
\______   \  | _____    _____   ___________ 
 |    |  _/  | \__  \  /     \_/ __ \_  __ \\
 |    |   \  |__/ __ \|  Y Y  \  ___/|  | \/
 |______  /____(____  /__|_|  /\___  >__|      by Teasel
        \/          \/      \/     \/       
""" + Style.RESET_ALL

print(header)

parser = argparse.ArgumentParser(description= Fore.YELLOW + "Control script for Blamer."
                                                + Style.RESET_ALL)

required_args = parser.add_argument_group("required arguments")

required_args.add_argument("-i", "--input",
                    help="file in which Blamer is going to search for comments to translate",
                    dest="input",
                    required=True)
                    
required_args.add_argument("-o", "--output",
                    help="result file in which Blamer will write the result",
                    dest="output",
                    required=True)

required_args.add_argument("-l", "--language",
                    help="language in which to translate the comments",
                    dest="language",
                    required=True)

args = parser.parse_args()

# Checking anonymity
printMessage("debug", "Check anonymity before scraping...")

if not check_tor():
        printMessage("warning", "Tor is not installed on the machine!")
        
        # Ask users to continue or stop
        answer = ''
        while not (answer=='y' or answer=='n'):
                answer = input(Fore.YELLOW + "You're not anonymous! Continue anyways? [y/n]: "
                                + Style.RESET_ALL)

        if answer=='n':
                exit(1)
        else:
                printMessage("warning", "Running Blamer non-anonymously")
else:
        printMessage("success", "Tor check successful!")

# Translating
printMessage("debug", "Starting translation...")
translate(args.input, args.output, args.language)
