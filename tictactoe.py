def check(list, s):
    # check diagonals
    if (set(s) == {list[0][0], list[1][1], list[2][2]} or
            set(s) == {list[0][2], list[1][1], list[2][0]}):
        return True
    for i in range(3):
        # check row or column
        if (set(s) == set(list[i]) or
                set(s) == {list[0][i], list[1][i], list[2][i]}):
            return True

    return False


matrix = [list("___"), list("___"), list("___")]
permitted_chars = {"X", "O", "_"}
digets = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
turn = 0

while True:
    turn +=  1
    print("---------")
    print(f"| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |")
    print(f"| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |")
    print(f"| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |")
    print("---------")

    # Win check
    if check(matrix, "X"):
        print("X wins")
        break
    elif check(matrix, "O"):
        print("O wins")
        break
    # draw check
    elif turn == 10:
        print("Draw")
        break
    else:
        # Game continues
        flag = True
        while flag:
            move = input()
            # check for numbers
            if {move[:1], move[2:3]}.issubset(digets):
                # check for coordinates
                if 0 < int(move[:1]) < 4 and 0 < int(move[2:3]) < 4:
                    # check for occupation, pun intended
                    if (matrix[int(move[:1]) - 1][int(move[2:3]) - 1] == "O" or
                            matrix[int(move[:1]) - 1][int(move[2:]) - 1] == "X"):
                        print("This cell is occupied! Choose another one!")
                    else:
                        # X begin and plays every odd turn
                        if turn % 2 == 0:
                            matrix[int(move[:1]) - 1][int(move[2:3]) - 1] = "O"
                        else:
                            matrix[int(move[:1]) - 1][int(move[2:3]) - 1] = "X"
                        flag = False
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")
