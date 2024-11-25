import random
import tkinter as tk
from sound_manager import SoundManager
from dice_image_manager import DiceImageManager
from ui_manager import UIManager
import pygame

class TenziesGame:
    """
    Handles the main game logic for the Tenzies Dice Game.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Tenzies Dice Game")

        self.sound_manager = SoundManager()
        self.image_manager = DiceImageManager()

        self.dice = [random.randint(1, 6) for _ in range(10)]  # Initial dice roll
        self.held = [False] * 10  # Track which dice are held
        self.roll_count = 0
        self.max_rolls = 10
        self.best_score = None
        self.rolling = False  # Prevent multiple clicks during animation
        self.game_started = False  # Prevent interaction until the first roll

        # Initialize the UIManager
        self.ui_manager = UIManager(
            root=self.root,
            dice_image_manager=self.image_manager,
            toggle_hold_callback=self.toggle_hold,
            roll_dice_callback=self.roll_dice,
            reset_game_callback=self.reset_game,
        )

    def toggle_hold(self, index):
        """
        Toggles the hold state of a dice.
        """
        if not self.game_started:
            self.ui_manager.update_status_label("Please roll the dice to start!")
            return
        if self.rolling:  # Prevent holding during animation
            return
        self.held[index] = not self.held[index]
        self.ui_manager.update_dice_display(self.dice, self.held)

    def roll_dice(self):
        """
        Handles the rolling of dice.
        """
        if self.rolling:  # Prevent multiple rolls during animation
            return
        if self.roll_count >= self.max_rolls:
            self.ui_manager.update_status_label("Game over! Reset to play again.")
            self.ui_manager.toggle_buttons(roll_visible=False, reset_visible=True)
            return

        if len(set(self.dice)) == 1:  # Check if all dice are the same
            self.ui_manager.update_status_label("You already won! Reset to play again.")
            self.ui_manager.toggle_buttons(roll_visible=False, reset_visible=True)
            return

        # Play roll sound and start animation
        self.sound_manager.play_sound("roll")
        self.rolling = True
        self.game_started = True
        self.animate_rolls(0)

    def animate_rolls(self, step):
        """
        Animates the rolling of dice.
        """
        if step < 10:  # 10 animation frames
            temp_dice = [
                random.randint(1, 6) if not self.held[i] else self.dice[i]
                for i in range(10)
            ]
            self.ui_manager.update_dice_display(temp_dice, self.held)
            self.root.after(100, lambda: self.animate_rolls(step + 1))  # 100ms delay
        else:
            # Final roll after animation
            self.dice = [
                self.dice[i] if self.held[i] else random.randint(1, 6)
                for i in range(10)
            ]
            self.roll_count += 1
            self.ui_manager.update_dice_display(self.dice, self.held)
            self.check_game_status()
            self.rolling = False

    def check_game_status(self):
        """
        Checks if the player has won or lost.
        """
        if len(set(self.dice)) == 1:  # All dice are the same
            win_message = f"Congratulations! You won in {self.roll_count} rolls."
            if self.best_score is None or self.roll_count < self.best_score:
                self.best_score = self.roll_count
                win_message += f" New best score: {self.best_score} rolls!"
            self.ui_manager.update_status_label(win_message)
            self.sound_manager.play_sound("win")
            self.ui_manager.toggle_buttons(roll_visible=False, reset_visible=True)
        elif self.roll_count >= self.max_rolls:  # No rolls left
            self.ui_manager.update_status_label("Game over! No more rolls left.")
            self.sound_manager.play_sound("lose")
            self.ui_manager.toggle_buttons(roll_visible=False, reset_visible=True)
        else:
            self.ui_manager.update_status_label(f"Rolls: {self.roll_count} / {self.max_rolls}")

    def reset_game(self):
        """
        Resets the game to its initial state.
        """
        self.dice = [random.randint(1, 6) for _ in range(10)]
        self.held = [False] * 10
        self.roll_count = 0
        self.game_started = False
        self.ui_manager.update_status_label("Roll the dice to start!")
        self.ui_manager.update_dice_display(self.dice, self.held)
        self.ui_manager.toggle_buttons(roll_visible=True, reset_visible=True)


def main():
    """
    Entry point for the Tenzies Dice Game.
    """
    pygame.init()
    root = tk.Tk()
    game = TenziesGame(root)

    # Event handling for music restoring
    def handle_pygame_events():
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                game.sound_manager.handle_music_restore()

    # Call the event handler periodically
    def check_events():
        handle_pygame_events()
        root.after(100, check_events)

    check_events()  # Start checking events
    root.mainloop()
    pygame.quit()
    
if __name__ == "__main__":
    main()
