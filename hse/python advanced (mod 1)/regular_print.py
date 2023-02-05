import sys
import re

complete_text = ''
for line in sys.stdin:
    if line == '\n':
        break
    complete_text += line.rstrip('\n')
italic = [string_[3:-4] for string_ in re.findall('<i>.*?</i>', complete_text)]
print(*italic, sep='\n')
