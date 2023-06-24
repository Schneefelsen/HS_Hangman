class CoffeeMachine:
    """
    This class represents a coffeemachine object.
    """

    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def buy(self, amount, type):
        enough = True
        coffee_dict = {"1": [250, 0, 16, 4], "2": [350, 75, 20, 7], "3": [200, 100, 12, 6]}
        if type != "back":
            for key in coffee_dict.keys():
                if type == key:
                    water_vol = coffee_dict[type][0]
                    milk_vol = coffee_dict[type][1]
                    bean_vol = coffee_dict[type][2]
                    cost = coffee_dict[type][3]
                    if water_vol != 0:
                        if self.water / water_vol < amount:
                            enough = False
                            print("Sorry, not enough water!")
                    if milk_vol != 0:
                        if self.milk / milk_vol < amount:
                            enough = False
                            print("Sorry, not enough milk!")
                    if bean_vol != 0:
                        if self.beans / bean_vol < amount:
                            enough = False
                            print("Sorry, not enough beans!")
                    if self.cups < amount:
                        enough = False
                        print("Sorry, not enough cups!")
                    if enough:
                        self.water -= (water_vol * amount)
                        self.beans -= (bean_vol * amount)
                        self.milk -= (milk_vol * amount)
                        self.money += (cost * amount)
                        self.cups -= amount
                        print("I have enough resources, making you a coffee!")
                    else:
                        break
    def fill(self):
        self.water += int(input("Write how many ml of water you want to add:\n"))
        self.milk += int(input("Write how many ml of milk you want to add: \n"))
        self.beans += int(input("Write how many grams of coffee beans you want to add: \n"))
        self.cups += int(input("Write how many disposable cups you want to add: \n"))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def display_output(self):
        print("The coffee machine has:\n"
              f"{self.water} ml of water\n"
              f"{self.milk} ml of milk\n"
              f"{self.beans} g of coffee beans\n"
              f"{self.cups} disposable cups\n"
              f"${self.money} of money")

    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == "buy":
                coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
                self.buy(1, coffee_type)
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.display_output()
            elif action == "exit":
                break

if __name__ == "__main__":
    cm = CoffeeMachine()
    cm.start()