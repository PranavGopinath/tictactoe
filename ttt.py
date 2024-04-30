import tkinter as tk
from tkinter import ttk
import numpy as np

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = np.full((3, 3), "", dtype=str)
        self.game_history = {'X': 0, 'O': 0}
        self.most_recent_winner = None

        # Initialize the game board at the start of the program
        self.create_game_board()

    def create_game_board(self):
        # Clear the window and set a more visually appealing background
        self.clear_window()
        self.root.configure(bg='#F2EFEA')  # Light beige background

        # Create buttons for the Tic-Tac-Toe grid with improved styling
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('Helvetica', 20), width=6, height=3,
                                   command=lambda row=i, col=j: self.on_click(row, col), bg='black', fg='#FFD700')  # Black button, Gold (bright yellow) text
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

        # Create a label to display the current player with a colored text
        self.status_label = tk.Label(self.root, text="Current Player: X", font=('Arial', 16), fg='#2E4057')  # Dark blue text
        self.status_label.grid(row=3, column=0, columnspan=3, pady=10)

    def on_click(self, row, col):
        # Handle button click event on the game board
        if self.board[row, col] == "":
            self.board[row, col] = self.current_player
            self.buttons[3 * row + col].config(text=self.current_player,
                                               fg='#FF6347' if self.current_player == 'X' else '#00BFFF')  # Tomato (bright red) for X, DodgerBlue (bright blue) for O

            # Check for a winner or tie, and update the game accordingly
            if self.check_winner():
                self.most_recent_winner = self.current_player
                self.game_history[self.current_player] += 1
                self.show_game_history()
            elif np.count_nonzero(self.board == "") == 0:
                self.show_game_history()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.update_status_label(f"Current Player: {self.current_player}")

    def check_winner(self):
        # Check if the current player has won the game
        for i in range(3):
            if np.all(self.board[i, :] == self.current_player) or np.all(self.board[:, i] == self.current_player):
                return True
        if np.all(np.diag(self.board) == self.current_player) or np.all(np.diag(np.fliplr(self.board)) == self.current_player):
            return True
        return False

    def show_game_history(self):
        # Display the game history screen with win counts and most recent winner
        self.clear_window()

        # Set a more visually appealing background for the history frame
        history_frame = ttk.Frame(self.root, style='TFrame.TFrame')
        history_frame.grid(row=0, column=0, padx=50, pady=50)

        # Configure styles for labels and buttons
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('Arial', 16), foreground='#2E4057')  # Dark blue text
        self.style.configure('TButton', font=('Arial', 14), padding=10, background='black', foreground='#FFD700')  # Black button, Gold (bright yellow) text

        # Create labels to display game history information
        label = ttk.Label(history_frame, text="Game History", style='TLabel', foreground='#5499C7')  # Steel blue text
        label.grid(row=0, column=0, columnspan=3, pady=20)

        x_wins_label = ttk.Label(history_frame, text=f"X Wins: {self.game_history['X']}", style='TLabel', foreground='#E74C3C')  # Red text
        x_wins_label.grid(row=1, column=0, padx=20)

        o_wins_label = ttk.Label(history_frame, text=f"O Wins: {self.game_history['O']}", style='TLabel', foreground='#3498DB')  # Blue text
        o_wins_label.grid(row=1, column=1, padx=20)

        recent_winner_label = ttk.Label(history_frame, text=f"Most Recent Winner: {self.most_recent_winner}", style='TLabel', foreground='#58D68D')  # Green text
        recent_winner_label.grid(row=2, column=0, columnspan=2, pady=20)

        # Create a button to continue to the next round
        continue_button = ttk.Button(history_frame, text="Continue to Next Round", style='TButton', command=self.create_game_board)
        continue_button.grid(row=3, column=0, columnspan=2, pady=20)

    def clear_window(self):
        # Clear all widgets in the main window
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    # Set a more visually appealing background for the main window
    root = tk.Tk()
    root.configure(bg='#F2EFEA')  # Light beige background

    # Create an instance of the TicTacToe class
    game = TicTacToe(root)

    # Run the Tkinter main loop
    root.mainloop()