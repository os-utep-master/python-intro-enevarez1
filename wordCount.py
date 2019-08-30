import sys
from collections import Counter
file = open("C:\\Users\\admin\\Desktop\\Coding Projects\\OS Theory\\Word Count\\declaration.txt")
def read_all_words(file):
    text = file.read()
    return text
def clean_punctuation(text):
    for char in '-.,\n':
        text=text.replace(char, ' ')
    text=text.lower()
    text= text.split()
    return text

#def count_words(text):
 #   Counter(text).most_common()
def write_file(text):
    file = open("myOutput.txt","w+")
    for k,v in sorted(Counter(text).most_common()):
            file.write( "{} {}\n".format(k,v) )

text = read_all_words(file)
text = clean_punctuation(text)
write_file(text)



