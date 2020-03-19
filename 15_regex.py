# Regex
import re

# we can create our own pattern that we can later use
# the 'r' at the beginning of the string indicates 'raw' string
pattern = re.compile(r'(^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$)')
# ()        -> group
# ^         -> first char
# [a-z...]  -> set of characters
# +         -> one or more times
# \.        -> literal point (.)
# @         -> literal @
# $         -> end of string
string = 'mail@mail.com'

print(pattern.search(string))

# must contain letters, numbers and $%#@
# at least 8 char long
# ends with a number
password_check = re.compile(r'[a-zA-Z0-9$%#@]{8,}\d')
# {n}       -> exacly n char long
# {n,}      -> n char long or more
# \d        -> any digit

password = 'thisIsMySuperLongPassword123#1'

print(password_check.fullmatch(password))
