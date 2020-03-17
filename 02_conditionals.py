#conditional logic

if False or True:
    print('First condition is true')
    print('something else')
elif None:
    print('First condition is false and second one is True')
else:
    print('None of the previous conditions were met')

is_magician = False
is_expert = True

if is_expert and is_magician:
    print('You are a master magician')
elif is_magician and not is_expert:
    print('At least you\'re getting there')
else:
    print('You need magic powers')

letters_list = ['a', 'b', 'c']
copied_list = letters_list

print(letters_list is copied_list)