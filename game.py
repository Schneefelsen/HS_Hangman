import random


class RockPaperScissors:

    def __init__(self):
        self.hands = {"rock": [0, -1, 1], "paper": [1, 0, -1], "scissors": [-1, 1, 0]}
        self.name = ""
        self.score = 0
        self.known_user = False

    def check_name(self):
        rating = open("rating.txt", "r")
        for line in rating:
            if line.startswith(self.name):
                self.score = int(line.split()[1])
                self.known_user = True
                break
        rating.close()

    def update_score(self):
        if self.known_user:
            rating = open("rating.txt", "r+")
            ratings = rating.readlines()
            for num, elem in enumerate(ratings):
                if elem.startswith(self.name):
                    ratings[num] = f"{self.name} {self.score}"
            rating.writelines(ratings)
        else:
            rating = open("rating.txt", "a")
            print(f"{self.name} {self.score}", file=rating)
        rating.close()

    def update_hands(self, options):
        option_dict = {}
        if options != [""]:
            weak_strong_list = [0]
            for _ in range(len(options) // 2):
                weak_strong_list.insert(1, -1)
                weak_strong_list.append(1)
            if len(options) % 2:
                weak_strong_list.pop()
            for pos, option in enumerate(options):
                option_dict.update({option: weak_strong_list.copy()})
                weak_strong_list.insert(0, weak_strong_list.pop())
            self.hands = option_dict

    def get_result(self, player, computer):
        computer_position = list(self.hands.keys()).index(computer)
        if self.hands[player][computer_position] == -1:
            print(f"Sorry, but the computer chose {computer}")
        elif self.hands[player][computer_position] == 1:
            print(f"Well done. The computer chose {computer} and failed")
            self.score += 100
        else:
            print(f"There is a draw {computer}")
            self.score += 50

    def play(self):
        self.name = input("Enter your name: ")
        self.check_name()
        print(f"Hello, {self.name}")
        wanted_hands = input().split(",")
        self.update_hands(wanted_hands)
        print("Okay, let's start")
        while True:
            possible_hands = list(self.hands.keys())
            com_hand = random.choice(possible_hands)
            user_hand = input()
            try:
                if user_hand == "!exit":
                    print("Bye!")
                    self.update_score()
                    break
                elif user_hand == "!rating":
                    print(f"Your rating: {self.score}")
                else:
                    self.get_result(user_hand, com_hand)
            except KeyError:
                print("Invalid input")


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()
