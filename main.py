import random
import tkinter as tk

class TenziesGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tenzies Dice Game")
        
        self.dice = [random.randint(1, 6) for _ in range(10)]  # Initial dice roll
        self.held = [False] * 10  # Track held dice
        self.roll_count = 0
        self.max_rolls = 10
        self.best_score = None
        self.rolling = False  # Prevent multiple clicks during animation

        self.create_widgets()
    
    def create_widgets(self):
        # Frame for dice
        self.dice_frame = tk.Frame(self.root)
        self.dice_frame.pack(pady=20)

        # Dice buttons
        self.dice_buttons = []
        for i in range(10):
            btn = tk.Button(self.dice_frame, text="⚀", font=("Arial", 24), width=4, height=2,
                            command=lambda i=i: self.toggle_hold(i))
            btn.grid(row=0, column=i, padx=5)
            self.dice_buttons.append(btn)

        # Roll button
        self.roll_button = tk.Button(self.root, text="Roll", font=("Arial", 18), command=self.roll_dice)
        self.roll_button.pack(pady=20)

        # Status label
        self.status_label = tk.Label(self.root, text="Roll the dice to start!", font=("Arial", 16))
        self.status_label.pack(pady=10)
    
    def toggle_hold(self, index):
        if self.rolling:  # Prevent holding during animation
            return
        self.held[index] = not self.held[index]
        self.update_dice_display()

    def roll_dice(self):
        if self.rolling:  # Prevent multiple rolls during animation
            return
        if self.roll_count >= self.max_rolls:
            self.status_label.config(text="Game over! Reset to play again.")
            return
        
        if len(set(self.dice)) == 1:  # Check if all dice are the same
            self.status_label.config(text="You already won! Reset to play again.")
            return

        # Start rolling animation
        self.rolling = True
        self.animate_rolls(0)  # Start animation sequence
    
    def animate_rolls(self, step):
        if step < 10:  # 10 steps of animation
            # Show temporary random dice faces
            temp_dice = [
                random.randint(1, 6) if not self.held[i] else self.dice[i]
                for i in range(10)
            ]
            self.update_dice_display(temp_dice)
            self.root.after(100, lambda: self.animate_rolls(step + 1))  # Delay 100ms
        else:
            # Final roll after animation
            self.dice = [
                self.dice[i] if self.held[i] else random.randint(1, 6)
                for i in range(10)
            ]
            self.roll_count += 1
            self.update_dice_display()
            self.check_game_status()
            self.rolling = False  # End animation
    
    def check_game_status(self):
        if len(set(self.dice)) == 1:  # Win condition
            win_message = f"Congratulations! You won in {self.roll_count} rolls."
            if self.best_score is None or self.roll_count < self.best_score:
                self.best_score = self.roll_count
                win_message += f" New best score: {self.best_score} rolls!"
            self.status_label.config(text=win_message)
        elif self.roll_count >= self.max_rolls:  # Game over condition
            self.status_label.config(text="Game over! No more rolls left.")
        else:
            self.status_label.config(text=f"Rolls: {self.roll_count} / {self.max_rolls}")

    def update_dice_display(self, temp_dice=None):
        dice_faces = {
            1: "⚀",
            2: "⚁",
            3: "⚂",
            4: "⚃",
            5: "⚄",
            6: "⚅"
        }
        for i, btn in enumerate(self.dice_buttons):
            value = temp_dice[i] if temp_dice else self.dice[i]
            btn.config(text=dice_faces[value])
            btn.config(bg="lightgreen" if self.held[i] else "SystemButtonFace")

    def reset_game(self):
        self.dice = [random.randint(1, 6) for _ in range(10)]
        self.held = [False] * 10
        self.roll_count = 0
        self.status_label.config(text="Roll the dice to start!")
        self.update_dice_display()

def main():
    root = tk.Tk()
    game = TenziesGame(root)

    # Reset Button
    reset_button = tk.Button(root, text="Reset", font=("Arial", 18), command=game.reset_game)
    reset_button.pack(pady=10)

    root.mainloop()

main()
