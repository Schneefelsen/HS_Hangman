import random
try:
    people = int(input("Enter the number of friends joining (including you):\n"))
except TypeError:
    print("Please use whole numbers.")
else:
    friends = {}
    if people < 1:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        for friend in range(people):
            friends[input()] = 0
        friends_list = [keys for keys in friends]
        bill = float(input("\nEnter the total bill value:\n"))
        lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
        if lucky == "Yes":
            lucky_person = random.choice(friends_list)
            print(f"\n{lucky_person} is the lucky one!")
            split_bill = round(bill / (people - 1), 2)
            if split_bill % 1 == 0:
                split_bill = int(split_bill)
            friends.update({key : split_bill for key in friends if key != lucky_person})
            print(f"\n{friends}")
        elif lucky == "No":
            print("No one is going to be lucky")
            split_bill = round(bill / people, 2)
            if split_bill % 1 == 0:
                split_bill = int(split_bill)
            friends = {key: split_bill for key in friends}
            print(f"\n{friends}")
