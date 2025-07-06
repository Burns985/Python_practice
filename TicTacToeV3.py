import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Helvetica", 20), width=5, height=2,
                                   command=lambda row=row, col=col: self.on_click(row, col))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Result", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_board_full():
                messagebox.showinfo("Result", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "X" if self.current_player == "O" else "O"

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_board_full(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.board[row][col] = " "
                self.buttons[row][col].config(text="")
        self.current_player = "X"


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
