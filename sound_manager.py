import pygame

class SoundManager:
    """
    A class to manage sound effects for the tenzies game.

    This class initializes the Pygame mixer. It acts as a simple sound management 
    system, where sound files are loaded once and played as needed.
    """
    def __init__(self):
        """
        Initializes the SoundManager instance.
        """
        pygame.mixer.init() 
        self.sounds = {
            "roll": pygame.mixer.Sound("sounds/dice_roll_1.wav"),
            "win": pygame.mixer.Sound("sounds/winner.wav"),
            "lose": pygame.mixer.Sound("sounds/game_over.wav"),
        }

    def play_sound(self, sound_name):
        """
        Plays a sound effect based on the given sound name.

        Args:
            sound_name (str): The key representing the sound to play 
                              (e.g., "roll", "win", "lose").
        
        If the sound name exists in the `sounds` dictionary, it plays the 
        inputed sound. Otherwise, it prints an error message.
        """
        if sound_name in self.sounds:
            pygame.mixer.stop()
            self.sounds[sound_name].play()
        else:
            print(f"Sound '{sound_name}' not found.")
