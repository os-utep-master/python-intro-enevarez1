import sys
from collections import Counter
file = open(sys.argv[1], 'r')
def read_all_words(file):
    text = file.read()
    return text
def clean_punctuation(text):
    for char in '-.,"\n':
        text= text.replace(char, ' ')
    text= text.lower()
    text= text.split()
    return text

def write_file(text):
    file = open(sys.argv[2],"w+")
    for k,v in sorted(Counter(text).most_common()):
            file.write( "{} {}\n".format(k,v) )

text = read_all_words(file)
text = clean_punctuation(text)
write_file(text)



