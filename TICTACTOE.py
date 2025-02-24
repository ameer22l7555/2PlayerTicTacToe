import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        # Initialize the main window
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.resizable(False, False)  # Prevent resizing for a fixed layout
        self.player = 'X'  # Start with player 'X'
        self.board = [[None, None, None],
                      [None, None, None],
                      [None, None, None]]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.x_wins = 0
        self.o_wins = 0
        self.draws = 0

        # Header frame for score and turn indicator
        self.header_frame = tk.Frame(self.window)
        self.header_frame.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.score_label = tk.Label(self.header_frame, text="X: 0 | O: 0 | Draws: 0", font=('normal', 20))
        self.score_label.pack(side='left')
        self.turn_label = tk.Label(self.header_frame, text="Turn: X", font=('normal', 20))
        self.turn_label.pack(side='right')

        # Grid frame for the game board with gray background for grid lines
        self.grid_frame = tk.Frame(self.window, bg='gray')
        self.grid_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Create buttons for the game board
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.grid_frame, text='', font=('normal', 40), width=5, height=2,
                                               command=lambda r=i, c=j: self.click(r, c), relief='groove')
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        # Footer frame for the new game button
        self.footer_frame = tk.Frame(self.window)
        self.footer_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.new_game_button = tk.Button(self.footer_frame, text="New Game", command=self.reset)
        self.new_game_button.pack()

    def click(self, row, col):
        # Handle button clicks
        if self.buttons[row][col]['text'] == '' and not self.check_winner():
            color = 'blue' if self.player == 'X' else 'red'
            self.buttons[row][col].config(text=self.player, fg=color)
            self.board[row][col] = self.player
            self.buttons[row][col]['state'] = 'disabled'  # Disable the clicked button
            if self.check_winner():
                if self.player == 'X':
                    self.x_wins += 1
                else:
                    self.o_wins += 1
                messagebox.showinfo("Game Over", f"{self.player} wins!")
                self.update_score()
                self.disable_all_buttons()
            elif self.check_draw():
                self.draws += 1
                messagebox.showinfo("Game Over", "Draw!")
                self.update_score()
                self.disable_all_buttons()
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                self.update_turn()

    def check_winner(self):
        # Check for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != None:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != None:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
            return True
        return False

    def check_draw(self):
        # Check for a draw
        for row in self.board:
            if None in row:
                return False
        return True

    def reset(self):
        # Reset the game board
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state='normal', fg='black')
                self.board[i][j] = None
        self.player = 'X'
        self.update_turn()

    def update_score(self):
        # Update the score display
        self.score_label.config(text=f"X: {self.x_wins} | O: {self.o_wins} | Draws: {self.draws}")

    def update_turn(self):
        # Update the turn indicator
        self.turn_label.config(text=f"Turn: {self.player}")

    def disable_all_buttons(self):
        # Disable all buttons when the game ends
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['state'] = 'disabled'

    def start(self):
        # Start the main event loop
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.start()