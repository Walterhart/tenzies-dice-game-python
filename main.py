import random
import tkinter as tk
from sound_manager import SoundManager
from dice_image_manager import DiceImageManager  

class TenziesGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tenzies Dice Game")
        self.sound_manager = SoundManager()

        self.image_manager = DiceImageManager()

        self.dice = [random.randint(1, 6) for _ in range(10)]  # Initial dice roll
        self.held = [False] * 10  # Track held dice
        self.roll_count = 0
        self.max_rolls = 10
        self.best_score = None
        self.rolling = False  # Prevent multiple clicks during animation
        self.game_started = False  # Prevent interaction until the first roll

        self.create_widgets()

    def create_widgets(self):
        # Frame for dice
        self.dice_frame = tk.Frame(self.root)
        self.dice_frame.pack(pady=20)

        # Dice buttons
        self.dice_buttons = []
        for i in range(10):
            btn = tk.Button(
                self.dice_frame,
                image=self.image_manager.get_image(1), 
                command=lambda i=i: self.toggle_hold(i),
                width=80,  
                height=80,
            )
            btn.grid(row=0, column=i, padx=5)
            self.dice_buttons.append(btn)

        # Roll button
        self.roll_button = tk.Button(self.root, text="Roll", font=("Arial", 18), command=self.roll_dice)
        self.roll_button.pack(pady=20)

        # Reset Button
        self.reset_button = tk.Button(self.root, text="Reset", font=("Arial", 18), command=self.reset_game)
        self.reset_button.pack(pady=10)

        # Status label
        self.status_label = tk.Label(self.root, text="Roll the dice to start!", font=("Arial", 16))
        self.status_label.pack(pady=10)

    def toggle_hold(self, index):
        if not self.game_started:  # Prevent holding until the game starts
            self.status_label.config(text="Please roll the dice to start!")
            return
        if self.rolling:  # Prevent holding during animation
            return
        self.held[index] = not self.held[index]
        self.update_dice_display()

    def roll_dice(self):
        if self.rolling:  # Prevent multiple rolls during animation
            return
        if self.roll_count >= self.max_rolls:
            self.sound_manager.play_sound("lose")
            self.status_label.config(text="Game over! Reset to play again.")
            self.roll_button.pack_forget()
            return

        if len(set(self.dice)) == 1:  # Check if all dice are the same
            self.sound_manager.play_sound("win")
            self.status_label.config(text="You already won! Reset to play again.")
            self.roll_button.pack_forget()
            return

        # Start rolling animation
        self.sound_manager.play_sound("roll")
        self.rolling = True
        self.game_started = True  # Allow interaction after the first roll
        self.animate_rolls(0)  # Start animation sequence

    def animate_rolls(self, step):
        if step < 10:  
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

            if self.roll_count >= self.max_rolls or len(set(self.dice)) == 1:
                self.roll_button.pack_forget()

            self.rolling = False  # End animation

    def check_game_status(self):
        if len(set(self.dice)) == 1:  # Win condition
            win_message = f"Congratulations! You won in {self.roll_count} rolls."
            if self.best_score is None or self.roll_count < self.best_score:
                self.best_score = self.roll_count
                win_message += f" New best score: {self.best_score} rolls!"
            self.status_label.config(text=win_message)
            self.sound_manager.play_sound("win")
        elif self.roll_count >= self.max_rolls:  # Game over condition
            self.status_label.config(text="Game over! No more rolls left.")
            self.sound_manager.play_sound("lose")
        else:
            self.status_label.config(text=f"Rolls: {self.roll_count} / {self.max_rolls}")

    def update_dice_display(self, temp_dice=None):
        for i, btn in enumerate(self.dice_buttons):
            value = temp_dice[i] if temp_dice else self.dice[i]
            btn.config(image=self.image_manager.get_image(value))
            btn.config(bg="lightgreen" if self.held[i] else "SystemButtonFace")

    def reset_game(self):
        self.dice = [random.randint(1, 6) for _ in range(10)]
        self.held = [False] * 10
        self.roll_count = 0
        self.game_started = False  # Prevent interaction after reset
        self.status_label.config(text="Roll the dice to start!")
        self.update_dice_display()

        self.roll_button.pack_forget()
        self.reset_button.pack_forget()
        self.roll_button.pack(pady=20)
        self.reset_button.pack(pady=10)


def main():
    root = tk.Tk()
    game = TenziesGame(root)
    root.mainloop()


main()
