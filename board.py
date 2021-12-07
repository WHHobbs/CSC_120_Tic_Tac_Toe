def intput(content):
    loop = True
    while loop:
        try:
            prompt = int(input(content))
            loop = False
            return prompt
        except ValueError:
            print("Due to an improper input, a ValueError occurred.")
class TicTacToe:
    def __init__(self):
        self.board = {"1": "-", "2": "-", "3": "-", "4": "-", "5": "-", "6": "-", "7": "-", "8": "-", "9": "-"}
        self.gameover = False
    def player_1_move(self):
        loop = True
        while loop:
            choice = intput("Choose a number from 1 to 9 to move.")
            if 1 <= choice <= 9 and self.board[str(choice)] not in ["x", "o"]:
                self.board[str(choice)] = "x"
                loop = False
            else:
                print("Invalid place")
    def player_2_move(self):
        loop = True
        while loop:
            choice = intput("Choose a number from 1 to 9 to move.")
            if 1 <= choice <= 9 and self.board[str(choice)] not in ["x", "o"]:
                self.board[str(choice)] = "o"
                loop = False
            else:
                print("Invalid place")
    def display(self):
        print(f"""
+---+---+---+
| {self.board["1"]} | {self.board["2"]} | {self.board["3"]} |
+---+---+---+
| {self.board["4"]} | {self.board["5"]} | {self.board["6"]} |
+---+---+---+
| {self.board["7"]} | {self.board["8"]} | {self.board["9"]} |
+---+---+---+""")
    def check_win(self):
        if self.board["1"] == "x" and self.board["2"] == "x" and self.board["3"] == "x" or self.board["1"] == "x" and self.board["4"] == "x" and self.board["7"] == "x" or self.board["1"] == "x" and self.board["5"] == "x" and self.board["9"] == "x" or self.board["2"] == "x" and self.board["5"] == "x" and self.board["8"] == "x" or self.board["3"] == "x" and self.board["6"] == "x" and self.board["9"] == "x" or self.board["3"] == "x" and self.board["5"] == "x" and self.board["7"] == "x" or self.board["4"] == "x" and self.board["5"] == "x" and self.board["6"] == "x" or self.board["7"] == "x" and self.board["8"] == "x" and self.board["9"] == "x":
            print("Player 1 wins!")
            self.gameover = True
        elif self.board["1"] == "o" and self.board["2"] == "o" and self.board["3"] == "o" or self.board["1"] == "o" and self.board["4"] == "o" and self.board["7"] == "o" or self.board["1"] == "o" and self.board["5"] == "o" and self.board["9"] == "o" or self.board["2"] == "o" and self.board["5"] == "o" and self.board["8"] == "o" or self.board["3"] == "o" and self.board["6"] == "o" and self.board["9"] == "o" or self.board["3"] == "o" and self.board["5"] == "o" and self.board["7"] == "o" or self.board["4"] == "o" and self.board["5"] == "o" and self.board["6"] == "o" or self.board["7"] == "o" and self.board["8"] == "o" and self.board["9"] == "o":
            print("Player 2 wins!")
            self.gameover = True
        elif self.board["1"] in ["x", "o"] and self.board["2"] in ["x", "o"] and self.board["3"] in ["x", "o"] and self.board["4"] in ["x", "o"] and self.board["5"] in ["x", "o"] and self.board["6"] in ["x", "o"] and self.board["7"] in ["x", "o"] and self.board["8"] in ["x", "o"] and self.board["9"] in ["x", "o"]:
            print("It is a tie!")
def play_game():
    NewGame = TicTacToe()
    while not NewGame.gameover:
        NewGame.player_1_move()
        NewGame.check_win()
        NewGame.display()
        if NewGame.gameover == False:
            NewGame.player_2_move()
            NewGame.check_win()
            NewGame.display()
play_game()