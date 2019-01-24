class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token


class Game:
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def __repr__(self):
        row = ""
        grid = []
        for i in range(len(self.board)):
            row = [str(cell) for cell in self.board[i]]
            row = "|".join(row)
            grid.append(row)
        grid = '\n'.join(grid)
        return grid

    def move(self, number, player):
        coordinates = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0), '8': (2, 1), '9': (2, 2)}
        y, x = coordinates[number]
        if type(self.board[y][x]) is int:
            if player.token == "X":
                self.board[y][x] = ("X")
            else:
                self.board[y][x] = ("O")
        else:
            print("Space taken")
            return "Space taken"

    def calc_winner(self):
        for i in range(len(self.board)):
            if self.board[i] == ["X", "X", "X"]:
                return "X wins!"
            elif self.board[i] == ["O", "O", "O"]:
                return "O wins!"
            elif self.board[0][i] == self.board[1][i] == self.board[2][i]:
                if self.board[0][i] == "X":
                    return "X wins!"
                else:
                    return "O wins"
            elif self.board[0][0] == self.board[1][1] == self.board[2][2]:
                if self.board[0][i] == "X":
                    return "X wins!"
                else:
                    return "O wins!"
            elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
                if self.board[0][i] == "X":
                    return "X wins!"
                else:
                    return "O wins!"
        return None

    def is_full(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "O" or self.board[i][j] == "X":
                    continue
                else:
                    return False
                    break
        return True

    def is_game_over(self):
        if self.is_full():
            print("It's a tie!")
            print("Game over.")
            return True
        if self.calc_winner():
            print(self.calc_winner())
            print("Game over.")
            return True
        else:
            return False


def main():
    player_1 = input("Player 1(X), please enter your name: ")
    player_1_token = 'X'
    player_2_token = 'O'
    player_2 = input("Player 2(O), please enter your name: ")
    p1 = Player(player_1, player_1_token)
    p2 = Player(player_2, player_2_token)
    new_game = Game()
    player_turn = 1
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print(new_game)
    while not new_game.is_game_over():
        print(f"Turn: {player_turn}")
        if player_turn % 2 != 0:
            p1_number = input(f'{player_1}, please enter a number: ')
            if p1_number not in numbers:
                continue
            move = new_game.move(p1_number, p1)
            if move == "Space taken":
                continue
            print(new_game)
            player_turn += 1
        else:
            p2_number = input(f'{player_2}, please enter a number: ')
            if p2_number not in numbers:
                continue
            move = new_game.move(p2_number, p2)
            if move == "Space taken":
                continue
            print(new_game)
            player_turn += 1


main()
