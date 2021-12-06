class TicTacToe:
    def __init__(self):
        self.board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
    def display_board(self):
        print(f"+---+---+---+\n| {self.board[0]} | {self.board[1]} | {self.board[2]} |\n+---+---+---+\n| {self.board[3]} | {self.board[4]} | {self.board[5]} |\n+---+---+---+\n| {self.board[6]} | {self.board[7]} | {self.board[8]} |\n+---+---+---+")
New_Game = TicTacToe()
New_Game.display_board()