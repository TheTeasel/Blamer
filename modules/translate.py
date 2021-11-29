import yaml
import re
import os
from googletrans import Translator
from modules.logging import printMessage

translator = Translator()
dest_lang = 'ru'

# Translate a given match (regex)
def comment_replacer(match):
    start,mid,end = match.group(1,2,3)
    if mid is None:
        # single line comment
        return translator.translate(str(match.group(0)), dest=dest_lang).text
    elif start is not None or end is not None:
        # multi line comment at start or end of a line
        return translator.translate(str(match.group(0)), dest=dest_lang).text
    elif '\n' in mid:
        # multi line comment with line break
        return '\n'
    else:
        # multi line comment without line break
        return ' '

# Return the regex (to extract the comments) based on the extension
def getRegex(extension):
    regex = ""

    with open("config/regex.yaml", "r") as configFile:
        try:
            documents = yaml.full_load(configFile)

            for key, value in documents.items():
                if key=="default":
                    regex = value
                if key==extension:
                    regex = value
            
            return regex

        except Exception as e:
            printMessage("error", str(e))
        finally:
            configFile.close()

# Translate a whole file
def translate(input, output, lang):
    # Check if the input is correct
    if not os.path.isfile(input):
        printMessage("error", "The input file couldn't be loaded. Please make sure it exists and is not a directory.")
        exit(1)

    # Destination language
    global dest_lang
    dest_lang = lang

    # Open the file and translate comments
    with open(input, "r") as srcFile:
        try:
            # Load the whole file in RAM since they shouldn't be too big
            srcContent = srcFile.read()

            # Translate and write to destination file
            with open(output, "w+") as dstFile:
                try:
                    filename, file_extension = os.path.splitext(input)
                    comment_re = re.compile(getRegex(file_extension), re.DOTALL | re.MULTILINE)
                    dstFile.write(comment_re.sub(comment_replacer, srcContent))
                
                except Exception as e:
                    printMessage("error", str(e))
                finally:
                    dstFile.close()
        
        except Exception as e:
            printMessage("error", str(e))
        finally:
            srcFile.close()

    printMessage("success", "Successfully translated " + input + " into " + output)