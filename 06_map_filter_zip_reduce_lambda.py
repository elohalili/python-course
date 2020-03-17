from functools import reduce

my_list = [1, 2, 3, 4]
your_list = [10, 20, 30, 40]

# like map in js
print(list(map(lambda item: item * 2, my_list)))

# like filter in js
print(list(filter(lambda item: item % 2 != 0, my_list)))

# creates an array of tuples that contains
# the data of each iterable at that specific index
# [(1, 10), (2, 20), (3, 30), (4, 40)]
print(list(zip(my_list, your_list)))

# just a reducer...
print(reduce(lambda acc, item: acc + item, my_list, 0))

print('_____________________')
#EXERCISE
# sort array a by the second item of the tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]

# extract sorting values
y_values = list(map(lambda t: t[1], a))
sorted_y_values = sorted(y_values)


def sort_a(e):
    return a[y_values.index(e)]


print(list(map(sort_a, sorted_y_values)))

# short version
a.sort(key=lambda e: e[1])
print(a)
