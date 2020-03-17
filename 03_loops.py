#loops
item = 'item'
for item in range(0, 10):
    print(item)

print(item)

print('___________________________')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for num in my_list:
    total += num

print('The total is: ', total)

print('___________________________')

for i in enumerate({'name': 'Elo', 'age': 23}.items()):
    print(i)

print('___________________________')

for index, value in enumerate(list(range(100))):
  print(index, value) if value == 50 else None

i = 0
while i < 50:
  print(i)
  i+=1
else:
  print('loop reached 50')

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]

for x, v in enumerate(picture):
    line = []
    for y, v in enumerate(picture[x]):
        line.append(' ') if picture[x][y] == 0 else line.append('*')
    print(''.join(line))

#prettier version
for row in picture:
    for pixel in row:
        print(' ', end='') if not pixel else print('*', end='')
    print('')

list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

for char in list:
  if list.count(char) > 1:
    print(char)