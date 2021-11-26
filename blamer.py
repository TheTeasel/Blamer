import argparse
import sys
from colorama import Fore, Style
from translate import translate

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

parser.add_argument("-d", "--destination",
                    help="Destination language",
                    dest="destination",
                    required=True)

args = parser.parse_args()

#print("input: " + args.input)
#print("output: " + args.output)
#print("destination: " + args.destination)
translate(args.input, args.output, args.destination)