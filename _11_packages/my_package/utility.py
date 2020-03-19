def greet():
    print('hello')


def add(num1, num2):
    try:
        if num1 and num2:
            return int(num1) + int(num2)
        else:
            return 'please enter number'
    except ValueError as err:
        return err
