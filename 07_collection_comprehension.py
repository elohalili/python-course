# collection comprehension
# lists, sets and dictionaries
# short way to generate collections

# ['expression' - 'for loop' - 'expression']
my_list = [num for num in range(10)]
my_list = [num * 2 for num in range(10) if num % 2 == 0]

print(my_list)

my_dict = {num: num * 2 for num in [1, 2, 3]}

print(my_dict)

list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = [char for char in list if list.count(char) > 1]

print(duplicates)