import re
import os.path
from googletrans import Translator

translator = Translator()
dest_lang = 'ru'
comment_re = re.compile(r'(^)?[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?', re.DOTALL | re.MULTILINE)

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

# Get all the matches (regex) and translate them
def translate_comments(text):
    return comment_re.sub(comment_replacer, text)

# Translate a whole file
def translate(input, output, lang):
    # Check if the input is correct
    if not os.path.isfile(input):
        print("Input doesn't exists")
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
                    dstFile.write(translate_comments(srcContent))
                
                except Exception as e:
                    print(str(e))
                finally:
                    dstFile.close()
        
        except Exception as e:
            print(str(e))
        finally:
            srcFile.close()