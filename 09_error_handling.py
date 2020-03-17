# Error handling

while True:
    try:
        age = int(input('What\'s your age ? '))
        print(10 / age)
        raise BufferError('RANDOM ERROR')
    except ValueError as err:
        print('Please enter a number.', err)
    except (ZeroDivisionError, EOFError) as err:
        print('Please enter a number higher than zero.', err)
    else:
        print('done')
        break
    finally:
        # the 'finally' statement runs always at the end of the try block
        # also if there's a break
        print('Finally')
