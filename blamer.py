import argparse
import sys
from colorama import Fore, Style
from translate import translate
from tor import init_tor

header = Fore.YELLOW + """
__________.__                               
\______   \  | _____    _____   ___________ 
 |    |  _/  | \__  \  /     \_/ __ \_  __ \\
 |    |   \  |__/ __ \|  Y Y  \  ___/|  | \/
 |______  /____(____  /__|_|  /\___  >__|      by Teasel
        \/          \/      \/     \/       
""" + Style.RESET_ALL

print(header)

parser = argparse.ArgumentParser(description="Control script for Blamer."
                                            + " Use one of the following option.",
                                 epilog="Example usage: python3 " + sys.argv[0] + " -i myFile.cpp -o myFileTranslated.cpp -d \"fr\"")

parser.add_argument("-i", "--input",
                    help="Input file",
                    dest="input",
                    required=True)
                    
parser.add_argument("-o", "--output",
                    help="Output file",
                    dest="output",
                    required=True)

parser.add_argument("-l", "--language",
                    help="Destination language",
                    dest="language",
                    required=True)

parser.add_argument("-a", "--anonymous",
                    help="Anonymous translation using Tor",
                    action="store_true")

args = parser.parse_args()

if args.anonymous:
        print("Check anonymity before scraping...")
        
        if not init_tor():
                print("Tor check failed!")
                exit(1)
        else:
                print("Tor check successful!")


translate(args.input, args.output, args.language)
