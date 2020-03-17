def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


# age = input("What is your age?: ")

# checkDriverAge(age)

# def highest_even(li=[]):
#     highest_even_num = 0
#     for n in li:
#         if n % 2 == 0 and n > highest_even_num:
#             highest_even_num = n
#     return highest_even_num


def highest_even(li=[]):
    for n in li:
        if max(li) % 2 == 0:
            return max(li)
        else:
            li.remove(max(li))
        print(n, li)


print(highest_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]))