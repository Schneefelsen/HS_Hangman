import random


def generate_domino_list():
    """Generates a complete set of dominos as a List of its possible combinations."""
    domino_list = []
    for digit1 in range(7):
        for digit2 in range(7):
            if digit2 >= digit1:
                domino_list.append([digit1, digit2])
    return domino_list


def split_shuffle(_list):
    """splits a given _list into three parts at random after shuffling, one twice as long as the other two
    and sorts each part afterwords"""
    random.shuffle(_list)
    split_list = (_list[:len(_list)//2],
                  _list[len(_list)//2:len(_list)*3//4],
                  _list[len(_list)*3//4:])
    return split_list


def sort_nested_list(_list):
    """sorts the content of every outermost element of a _list"""
    s_list = []
    for i in range(len(_list)):
        s_list.append(sorted(_list[i]))
    return s_list


def who_first(com_piece, player_piece):
    """Determines if com has the highest value piece or else the highest double and returns it"""
    if (com_piece[-1][0] + com_piece[-1][1] >
            player_piece[-1][0] + player_piece[-1][1]):
        return com_piece.pop(-1), True
    elif (com_piece[-1][0] + com_piece[-1][1] <
          player_piece[-1][0] + player_piece[-1][1]):
        return player_piece.pop(-1), False
    com_double = []
    pl_double = []
    for i in range(7):
        if [i, i] in com_piece:
            com_double = [i, i]
        if [i, i] in player_piece:
            pl_double = [i, i]
    if com_double != [] and pl_double != []:
        if com_double > pl_double:
            com_pieces.remove(com_double)
            return com_double, True
        else:
            player_pieces.remove(pl_double)
            return pl_double, False
    elif com_double:
        com_pieces.remove(com_double)
        return com_double, True
    elif pl_double:
        player_pieces.remove(pl_double)
        return pl_double, False
    return []


def enforce_domino_rule(domino, domino_list, plus):
    """Checks, if an added domino block is allowed at its position
    and returns it in its correct orientation"""
    if plus:
        if domino[0] == domino_list[-1][1]:
            return domino
        elif domino[1] == domino_list[-1][1]:
            return domino[::-1]
        else:
            return []
    else:
        if domino[1] == domino_list[0][0]:
            return domino
        elif domino[0] == domino_list[0][0]:
            return domino[::-1]
        else:
            return []


def rarity_check(computer_list, check_list):
    """This function assigns a rarity value to each element of computer list
    and returns a sorted computer_list"""
    rarity_numbers = []
    rarity_list = []
    for i in range(7):
        rarity_numbers.append(sum(x.count(i) for x in check_list or computer_list))
    for j in range(len(computer_list)):
        rarity_list.append([rarity_numbers[computer_list[j][0]] +
                            rarity_numbers[computer_list[j][1]],
                            computer_list[j]])
        rarity_list.sort(reverse=True)
    return rarity_list


while True:
    start_dominos = sort_nested_list(split_shuffle(generate_domino_list()))
    stock = start_dominos[0]
    com_pieces = start_dominos[1]
    player_pieces = start_dominos[2]
    first_player = who_first(com_pieces, player_pieces)
    if first_player:
        snake = [first_player[0]]
        status = first_player[1]
        break

while True:
    print("=" * 70)
    print(f"Stock size: {len(stock)}")
    print(f"Computer pieces: {len(com_pieces)}\n")
    if len(snake) < 7:
        for piece in snake:
            print(piece, end="")
    else:
        for n in range(0, 3):
            print(snake[n], end="")
        print("...", end="")
        for n in range(0, 3):
            print(snake[-3 + n], end="")
    print(f"\n\nYour pieces:")
    for piece_num in range(len(player_pieces)):
        print(f"{piece_num + 1}:{player_pieces[piece_num]}")
    if not player_pieces:
        print("Status: The game is over. You won!")
        break
    elif not com_pieces:
        print("Status: The game is over. The computer won!")
        break
    elif snake[0][0] == snake[-1][1]:
        number_count = 0
        for piece in snake:
            if piece[0] == snake[0][0]:
                number_count += 1
            if piece[1] == snake[0][0]:
                number_count += 1
        if number_count == 8:
            print("Status: The game is over. It's a draw!")
            break
    if status:
        status = False
        print("\nStatus: It's your turn to make a move. Enter your command.")
        while True:
            while True:
                try:
                    user_input = int(input())
                    if (-len(player_pieces) > user_input or
                            len(player_pieces) < user_input):
                        print("Invalid input. Please try again.\n")
                        continue
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please try again.\n")
            if user_input < 0:
                insert_domino = enforce_domino_rule(player_pieces[-user_input - 1], snake, False)
                if not insert_domino:
                    print("Illegal move. Please try again.\n")
                    continue
                else:
                    player_pieces.pop(-user_input - 1)
                    snake.insert(0, insert_domino)
                    break
            elif user_input > 0:
                insert_domino = enforce_domino_rule(player_pieces[user_input - 1], snake, True)
                if not insert_domino:
                    print("Illegal move. Please try again.\n")
                    continue
                else:
                    player_pieces.pop(user_input - 1)
                    snake.append(insert_domino)
                    break
            else:
                if stock:
                    player_pieces.append(stock.pop(random.randrange(0, len(stock))))
                break
    else:
        status = True
        while input("\nStatus: Computer is about to make a move. Press Enter to continue...\n"):
            continue
        rarity_score = rarity_check(com_pieces, snake)
        for element in rarity_score:
            insert_domino = enforce_domino_rule(element[1], snake, False)
            if insert_domino:
                snake.insert(0, insert_domino)
                com_pieces.remove(element[1])
                break
            insert_domino = enforce_domino_rule(element[1], snake, True)
            if insert_domino:
                snake.append(insert_domino)
                com_pieces.remove(element[1])
                break
        else:
            if stock:
                com_pieces.append(stock.pop(random.randrange(0, len(stock))))
