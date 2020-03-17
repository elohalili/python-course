# something = input('Tell me something:')

# print('\'' + something + '\' is all you got ?')
# print(type(something))
# print('You can do better than this :D ')

# print(bin(15))

# name = 'Name'
# surname = 'Surname'
# age = '23'

# birht_year = input('What year were you born? \n')
# age = 2020 - int(birht_year)
# print(f'''Ok!
# I guess your age is {age}
# ''')

# username = 'Username'
# password = '1342'

# print(f'''
# Hey {username}!
# The password you set {'*' * len(password)} is {len(password)} characters long.
# ''')

li = [1,2,3,4]
li.extend([1,2,'elo'])

print('elo' in li )
# print(li.pop())

print(list(range(10)))

print(' '.join(str(i) for i in li))