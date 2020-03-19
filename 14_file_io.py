# File I/O
from translate import Translator

# this will return a TextIOWrapper object
readme_file = open('./README.md')

# the read method returns the whole content of the file
# moving the cursor at the end of it
readme_file.read()
# seek will move the cursor to the given index
# so that we can read again the file's content
readme_file.seek(0)
# 'readline' will return only one line leaving the cursor at the end of it
readme_file.readline()
# 'readlines' will return a list with all the lines of the file as items
readme_file.readlines()
# close will simply close the current file
readme_file.close()


# standard way to read file w/out needing to close it
# default mode is read, with 'r+' we can read and write
# r -> read
# w -> write (also creates a new file if needed)
# a -> append
# even tho r+ seems to append in python 3.7.3 🤷
# with open('./files.txt', mode='r+') as file:
# text = file.write(' :D')
# print(file.readlines())

#######################################################
# Exercise: translate the content of a file

_translate = Translator(to_lang="it")

try:
    with open('./file.txt', mode='r+', encoding='utf8') as file:
        text_lines = file.readlines()
        translated_text = '\r'.join(
            [_translate.translate(line) for line in text_lines])
        print(translated_text)
        text = ''.join(text_lines)
        open('./file_translated.txt',
             mode='w', encoding='utf8').write(f'{text}\n\n#Translated text#\n\n{translated_text}')
except Exception as err:
    raise err
