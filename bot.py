def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


def test():
    while True:
        print("Let's test your programming knowledge.")
        print("Why do I program this?")
        print("1. Because I am bored.")
        print("2. Because hyperskill rewards me with fake currency afterwards.")
        print("3. Because I genuinely struggle with this.")
        print("4. Cookies are icky.")
        guess = input()
        if guess != "2":
            print("Please, try again.")
        else:
            break

def end():
    print('Congratulations, have a nice day!')


greet('Aid', '2023')  # change it as you need
remind_name()
guess_age()
count()
test()
end()
