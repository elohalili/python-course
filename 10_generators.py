# Generators
# range(100) this is a generator function
# generators are subsets of iterables hence they will have __iter__
def make_list(num):
    result = []
    for i in range(num):
        result.append(i * 2)

    return result


# this way I'm wasting memory cause the result list gets
# stored in memory before it returns
my_list = make_list(100)


# Example of generator
def generator_fn(num):
    # this will simply loop through a given number range
    for i in range(num):
        # and it will stop iterating at this 'yield' keyword
        # untill the next function gets called on the generator obj
        yield i


# here we'll have a generator object
g = generator_fn(10)
# with the next function we will receive the first yielded value
print(next(g))
# so unlike the make_list function we could create a list without ever
# needing to store data during the iteration
# resulting in added performance

my_list2 = []
# for loops will take care of the generator object
# until it reaches the end (StopIteration error)
for n in generator_fn(10):
    my_list2.append(n)

print(my_list2)


#######################################
# How for loops works under the hood
def special_for(iterable):
    # uses the __iter__ method of the iterator that we gave
    iterator = iter(iterable)
    # loops endlessly
    while True:
        try:
            # uses __next__ method to go on with the iteration
            print(next(iterator))
        except StopIteration:
            # ends the loop at the raise of StopIteration Exception
            break


special_for([1, 2, 3, 4, 5])


#######################################
# So if we wanted to implement our own range, it would be something like this
class MyGen():
    # this is the state holder
    current = 0

    def __init__(self, last, first=0):
        self.last = last
        MyGen.current = first

    # rewrite iter
    def __iter__(self):
        return self

    # rewrite next to manage the iteration
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


special_for(MyGen(10, 5))

# for i in MyGen(10):
#     print(i)

print('#######################################')

#######################################
# Exercise: Fibonacci sequence


def fib(num):
    # pair of index values
    f1 = 0
    f2 = 1
    for i in range(num):
      yield(f1)
      temp = f1
      f1 = f2
      f2 = f1 + temp
        # if i - 1 >= 0:
        #     res = f1 + f2
        #     f1 = f2
        #     f2 = res
        #     yield (res)
        #     pass
        # else:
        #     yield (i)


for n in fib(20):
    print(n)
