import pygame

class SoundManager:
    """
    A class to manage sound effects and background music for the Tenzies game.

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
        self.background_music = "sounds/background_music_loop_1.mp3"
        self.is_music_paused = False  # Track the paused state of music

        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.set_volume(0.5)  # Initial background music volume
        pygame.mixer.music.play(-1)  # Loop indefinitely

    def play_sound(self, sound_name):
        """
        Plays a sound effect, pausing the background music for specific sounds.

        Args:
            sound_name (str): The key representing the sound to play.
        """
        if sound_name in self.sounds:
            # For win or lose, pause the background music
            if sound_name in ["win", "lose"]:
                self.pause_music()  
                self.sounds[sound_name].play()

                # Set a timer to resume music after the sound finishes
                sound_length = self.sounds[sound_name].get_length()
                pygame.time.set_timer(pygame.USEREVENT, int(sound_length * 1000))
            else:
                # Play other sounds (e.g., "roll") without affecting music
                self.sounds[sound_name].play()
        else:
            print(f"Sound '{sound_name}' not found.")

    def pause_music(self):
        """
        Pauses the background music if it is currently playing.
        """
        if not self.is_music_paused:
            pygame.mixer.music.set_volume(0.0)  # Fade to silence
            pygame.mixer.music.pause()
            self.is_music_paused = True

    def resume_music(self):
        """
        Resumes the background music from where it was paused.
        """
        if self.is_music_paused:
            pygame.mixer.music.unpause()
            pygame.mixer.music.set_volume(0.5)  # Restore volume
            self.is_music_paused = False

    def handle_music_restore(self):
        """
        Handles the restoration of the background music after the timer event.
        """
        self.resume_music()
