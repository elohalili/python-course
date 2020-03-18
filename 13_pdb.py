import pdb

# pdb is the python debugger tool


def add(num1, num2):
    # this is our debug point where the debugger will stop
    pdb.set_trace()
    t = 4 * 5
    return num1 + num2 + t


# this code will eventually raise a TypeError
add(12, 'wrong value')

# running this code will activate the pdb and it will stop the execution at line 8
# we can then examine the variables, functions, code....
# h -> help with the list of all the pdb commands
# s -> step to next line
# w -> indicates the most recent 'frame' (where are we at the current execution)
# l -> shows the code, pointing at the current line
