import random


def hangman():
    word_list = ["python", "java", "swift", "javascript"]
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    chosen_word = random.choice(word_list)
    chosen_letters = set(chosen_word)
    guessed_letters = set()
    hint = "-" * (len(chosen_word))
    tries = 8

    while tries > 0:
        print("\n" + hint)
        # error handling:
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("Please, input a single letter.")
        elif guess not in alphabet:
            print("Please, enter a lowercase letter from the English alphabet.")
        elif guess in guessed_letters:
            print("You've already guessed this letter.")
        # new letter guessed:
        elif guess in chosen_letters \
                and guess not in guessed_letters:
            guessed_letters.add(guess)
            # This is the win clause:
            if chosen_letters.issubset(guessed_letters):
                print(f"\nYou guessed the word {chosen_word}!")
                print("You survived!")
                return True
            # Find the positions of the correct letter
            # and paste them into the hint string:
            position = chosen_word.index(guess)
            for c in range(chosen_word.count(guess)):
                hint = hint[:position] + guess + hint[position + 1:]
                position = chosen_word.find(guess, position + 1)
        else:
            print("That letter doesn't appear in the word.")
            guessed_letters.add(guess)
            tries -= 1

    if tries == 0:
        print("\nYou lost!")
        return False


win_count = 0
loss_count = 0
print("H A N G M A N")
while True:
    menu_input = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if menu_input == "play":
        result = hangman()
        if result:
            win_count += 1
        else:
            loss_count += 1
    elif menu_input == "results":
        print(f"You won: {win_count} times")
        print(f"You lost: {loss_count} times")
    elif menu_input == "exit":
        break


