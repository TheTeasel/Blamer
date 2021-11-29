import argparse
import sys
from colorama import Fore, Style
from translate import translate
from tor import check_tor

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
                    help="This is the file in which Blamer is going to search for comments to translate",
                    dest="input",
                    required=True)
                    
required_args.add_argument("-o", "--output",
                    help="This is the result file. If it doesn't exists then Blamer will create it for you",
                    dest="output",
                    required=True)

required_args.add_argument("-l", "--language",
                    help="The language in which to translate the comments",
                    dest="language",
                    required=True)

args = parser.parse_args()

# Checking anonymity
print("Check anonymity before scraping...")

if not check_tor():
        print(Fore.RED + "Blamer uses Google Translate's API in order to translate the comments."\
                "\nTo anonymously translate your files, we strongly recommend using Tor."
                + Style.RESET_ALL)
        
        # Ask users to continue or stop
        answer = ''
        while not (answer=='y' or answer=='n'):
                answer = input("You're not anonymous! Continue anyways? [y/n]: ")

        if answer=='n':
                exit(1)
else:
        print("Tor check successful!")

# Translating
translate(args.input, args.output, args.language)
