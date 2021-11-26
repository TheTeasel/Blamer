# Needs googletrans==3.1.0a0
import re
from googletrans import Translator

translator = Translator()
dest_lang = 'fr'
comment_re = re.compile(r'(^)?[^\S\n]*/(?:\*(.*?)\*/[^\S\n]*|/[^\n]*)($)?', re.DOTALL | re.MULTILINE)

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

def translate_comments(text):
    return comment_re.sub(comment_replacer, text)


with open("source.cpp", "r") as srcFile:
    srcContent = srcFile.read()
    print(translate_comments(srcContent))