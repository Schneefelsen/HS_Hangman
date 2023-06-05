import string
import random

def bot_func(number):
    if number % 4 == 0:
        return 3
    elif (number + 1) % 4 == 0:
        return 2
    elif (number + 2) % 4 == 0:
        return 1
    elif 1 < number < 4:
        return number - 1
    elif number == 1:
        return 1
    else:
        return int(random.uniform(1, 3.99))

pencils = input("How many pencils would you like to use:\n")
names = ["John", "Bot"]
permitted_num = ["1", "2", "3"]

while True:
    for letter in pencils:
        if letter not in string.digits:
            pencils = input("The number of pencils should be numeric\n")
            break
    else:
        pencils = int(pencils)
        if pencils == 0:
            pencils = input("The number of pencils should be positive\n")
            continue
        break

name = input(f"Who will be the first ({names[0]}, {names[1]}):\n")

while pencils != 0:
    if name not in names:
        name = input(f"Choose between {names[0]} and {names[1]}\n")
        continue
    pencils_str = "|" * pencils
    print(pencils_str)
    print(f"{name}'s turn:\n")
    if name == names[0]:
        takeaway = input()
        while takeaway not in permitted_num:
            takeaway = input("Possible values: '1', '2' or '3'\n")
        while pencils - int(takeaway) < 0:
            takeaway = input("Too many pencils were taken")
        name = names[1]

    else:
        takeaway = bot_func(pencils)
        print(takeaway)
        name = names[0]

    pencils = pencils - int(takeaway)
print(f"{name} won!")
