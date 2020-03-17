# Decorators
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('superboosted')
        func(*args, **kwargs)
        print('superboosted')

    return wrapper


@my_decorator
def greet():
    print('hello')


greet()
'''
With decorators we can simply wrap our functions into higher order ones
that can "super boost" it by giving us a way to manipulate the behaviour
'''
#that would be the equivalent of this
greet2 = my_decorator(greet)()

# Higher Order Function HOF
'''
any function that accepts as args a function
or returns one can be called HOF
'''


def hof(function):
    function()


def hof2():
    def function():
        return True

    return function


#exercise
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took: {t2 - t1}')
        return result

    return wrapper


@performance
def long_function():
    for i in range(1000000):
        i**2


# long_function()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid':
    False  #changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            fn(*args, **kwargs)

    return wrapper


@authenticated
def message_friends(user, asd, asds):
    print('message has been sent')


message_friends(user1, True, False)
