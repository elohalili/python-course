import sys
from random import randrange

# use random module to create a guessing game
# the game will receive in sys inputs the starting and ending for the sequence of number
# the game will pick randomly one number
# the user has to guess the exact number
# until then the game will continue running

try:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
except:
    print('Dude you have to instert integer numbers :|')

print(f'''
############################################
Welcome to this useless guessing game :D
You have to guess between {start} and {end}
Good luck!
############################################
''')

number = randrange(start, end)


def get_user_input():
    try:
        num = int(input('\nWhat\'s your guess? '))
        if start <= num <= end:
            return num
        else:
            raise ValueError
    except:
        print(f'''What\'s wrong with you...
        \nYou have to choose a number between {start} and {end}''')
        return get_user_input()


while True:
    chosen_num = get_user_input()
    if chosen_num == number:
        print('You won! Yay :D')
        break
    else:
        print('Nope, you\'re wrong!')
