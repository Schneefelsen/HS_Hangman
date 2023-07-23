import random


def parse_command():
    player_list = ["user", "easy", "medium", "hard"]
    command = input("Input command ")
    while True:
        if command == "exit":
            return []
        elif command.startswith("start"):
            if len(command.split()) != 3:
                command = input("Bad parameters!")
            elif (command.split()[1] not in player_list or
                    command.split()[2] not in player_list):
                command = input("Bad parameters!")
            else:
                return command.split()
        else:
            command = input("Bad parameters!")


def minimax(grid, depth, isMax, player, opponent):
    empty_pos = [k for k, v in grid.items() if v == "_"]
    if win_con(player, grid):
        return 10
    elif win_con(opponent, grid):
        return -10
    elif "_" not in grid.values():
        return 0
    if isMax:
        best = -1000
        for pos in empty_pos:
            grid[pos] = player
            best = max(best, minimax(grid, depth + 1, not isMax, player, opponent))
            grid[pos] = "_"
        return best
    else:
        best = 1000
        for pos in empty_pos:
            grid[pos] = opponent
            best = min(best, minimax(grid, depth + 1, not isMax, player, opponent))
            grid[pos] = "_"
        return best


def win_con(mark, grid):
    for i in range(3):
        if (mark == grid[str(i + 1) + " 1"] == grid[str(i + 1) + " 2"] == grid[str(i + 1) + " 3"] or
                mark == grid["1 " + str(i + 1)] == grid["2 " + str(i + 1)] == grid["3 " + str(i + 1)]):
            return True
    if (mark == grid["1 1"] == grid["2 2"] == grid["3 3"] or
            mark == grid["3 1"] == grid["2 2"] == grid["1 3"]):
        return True


class TicTacToe:

    def __init__(self):
        self.grid = {"1 1": "_", "1 2": "_", "1 3": "_",
                     "2 1": "_", "2 2": "_", "2 3": "_",
                     "3 1": "_", "3 2": "_", "3 3": "_"}
        self.mark1 = "X"
        self.mark2 = "O"

    def print_grid(self):
        print("---------")
        print(f"| {self.grid['1 1']} {self.grid['1 2']} {self.grid['1 3']} |")
        print(f"| {self.grid['2 1']} {self.grid['2 2']} {self.grid['2 3']} |")
        print(f"| {self.grid['3 1']} {self.grid['3 2']} {self.grid['3 3']} |")
        print("---------")

    def clear_grid(self):
        self.grid = {"1 1": "_", "1 2": "_", "1 3": "_",
                     "2 1": "_", "2 2": "_", "2 3": "_",
                     "3 1": "_", "3 2": "_", "3 3": "_"}

    def state(self, mark):
        if win_con(mark, self.grid):
            print(f"{mark} wins")
            self.clear_grid()
            return True
        elif "_" not in self.grid.values():
            print("Draw")
            self.clear_grid()
            return True

    def player_turn(self, mark):
        coords = input("Enter the coordinates: ")
        while True:
            if coords in self.grid:
                if self.grid[coords] != "_":
                    coords = input("This cell is occupied! Choose another one!")
                    continue
                self.grid[coords] = mark
                break
            if coords.split():
                for coord in coords.strip().split():
                    if not coord.isnumeric():
                        coords = input("You should enter numbers!")
                        break
                    elif not 0 < int(coord) < 3:
                        coords = input("Coordinates should be from 1 to 3!")
                        break
            else:
                print("You should enter numbers!")

    def level_easy(self, mark):
        while True:
            c1, c2 = random.choice([1, 2, 3]), random.choice([1, 2, 3])
            coords = f"{c1} {c2}"
            if self.grid[coords] != "_":
                continue
            self.grid[coords] = mark
            break

    def two_in_a_row(self, mark):
        mark_pos = [k.split() for k, v in self.grid.items() if v == mark]
        for pos1 in mark_pos:
            for pos2 in mark_pos:
                if pos1 != pos2:
                    # main diagonal test
                    if pos1[0] == pos1[1] and pos2[0] == pos2[1]:
                        for pos3 in [[1, 1], [2, 2], [3, 3]]:
                            if (pos3 not in mark_pos and
                                    self.grid[f"{pos3[0]} {pos3[1]}"] == "_"):
                                return f"{pos3[0]} {pos3[1]}"
                    # sub diagonal test
                    if pos1 in [[1, 3], [2, 2], [3, 1]] and pos2 in [[1, 3], [2, 2], [3, 1]]:
                        for pos3 in [[1, 3], [2, 2], [3, 1]]:
                            if (pos3 not in mark_pos and
                                    self.grid[f"{pos3[0]} {pos3[1]}"] == "_"):
                                return f"{pos3[0]} {pos3[1]}"
                    #  horizontal test
                    if pos1[0] == pos2[0]:
                        for pos3 in [1, 2, 3]:
                            if ([pos1[0], pos3] not in mark_pos and
                                    self.grid[f"{pos1[0]} {pos3}"] == "_"):
                                return f"{pos1[0]} {pos3}"
                    # vertical test
                    if pos1[1] == pos2[1]:
                        for pos3 in [1, 2, 3]:
                            if ([pos3, pos1[1]] not in mark_pos and
                                    self.grid[f"{pos3} {pos1[1]}"] == "_"):
                                return f"{pos3} {pos1[1]}"

    def level_medium(self, mark):
        if mark == self.mark1:
            other_mark = self.mark2
        else:
            other_mark = self.mark1
        twos = self.two_in_a_row(mark)
        other_twos = self.two_in_a_row(other_mark)
        if twos:
            self.grid[twos] = mark
        elif other_twos:
            self.grid[other_twos] = mark
        else:
            self.level_easy(mark)

    def find_best_move(self, board, mark):
        if mark == self.mark1:
            other_mark = self.mark2
        else:
            other_mark = self.mark1
        best_val = -1000
        best_move = "-1 -1"
        if mark == self.mark1:
            other_mark = self.mark2
        else:
            other_mark = self.mark1
        for i in range(1, 4):
            for j in range(1, 4):
                if board[f"{i} {j}"] == '_':
                    board[f"{i} {j}"] = mark
                    move_val = minimax(board, 0, False, mark, other_mark)
                    board[f"{i} {j}"] = '_'
                    if move_val > best_val:
                        best_move = f"{i} {j}"
                        best_val = move_val
        return best_move

    def level_hard(self, mark):
        best_move = self.find_best_move(self.grid, mark)
        self.grid[best_move] = mark

    def turn(self, players, mark):
        if mark == self.mark1:
            if players[1] == "user":
                self.player_turn(mark)
            elif players[1] == "easy":
                print('Making move level "easy"')
                self.level_easy(mark)
            elif players[1] == "medium":
                print('Making move level "medium"')
                self.level_medium(mark)
            elif players[1] == "hard":
                print('Making move level "hard"')
                self.level_hard(mark)
        else:
            if players[2] == "user":
                self.player_turn(self.mark2)
            elif players[2] == "easy":
                print('Making move level "easy"')
                self.level_easy(self.mark2)
            elif players[2] == "medium":
                print('Making move level "medium"')
                self.level_medium(self.mark2)
            elif players[2] == "hard":
                print('Making move level "hard"')
                self.level_hard(self.mark2)

    def play(self):
        while True:
            player_list = parse_command()
            if not player_list:
                break
            self.print_grid()
            while True:
                self.turn(player_list, self.mark1)
                self.print_grid()
                if self.state(self.mark1):
                    break
                self.turn(player_list, self.mark2)
                self.print_grid()
                if self.state(self.mark2):
                    break


if __name__ == "__main__":
    TicTacToe().play()
