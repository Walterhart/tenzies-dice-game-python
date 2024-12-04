# Tenzies Dice Game

Tenzies Dice Game is a Python-based game where players attempt to roll all ten dice to show the same number within a limited number of rolls. The project uses Tkinter for the GUI, Pygame for sound management, and Pillow (PIL) for handling dice images. The game includes animations, sound effects, and a user interface.

## Features

    Interactive Gameplay:
        Roll up to 10 dice.
        Hold specific dice between rolls.
        Win by matching all dice faces within 10 rolls.

    Sound Effects:
        Dice rolling, winning, and losing sounds.
        Background music with auto-resume after events.

    User Interface:
        Dice buttons with visual states for "held" and "rolling."
        Roll and Reset buttons with status updates.

    Animations:
        Dice rolling animations for a dynamic experience.

## Project Structure

`main.py`

    Manages the core game logic and initializes all managers (UI, sound, images).
    Includes game state controls such as rolling, holding, and resetting dice.

`sound_manager.py`

    Handles sound effects and background music using Pygame.
    Features auto-pause/resume for background music during significant events.

`ui_manager.py`

    Manages the GUI using Tkinter.
    Includes dice buttons, status messages, and control buttons.

`dice_image_manager.py`

    Loads and manages dice images using Pillow.
    Dynamically resizes images to fit the UI.

##Requirements

    Python 3.8+
    Dependencies:
        `pygame`
        `pillow`

Install dependencies with:

```bash
pip install pygame pillow
```

## How to Run

    Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd tenzies-dice-game-python
```

Ensure the `images/` and `sounds/` directories contain appropriate assets:

    Images: `dice_1.png`, `dice_2.png`, ..., `dice_6.png`
    Sounds: `dice_roll_1.wav`, `winner.wav`, `game_over.wav`, `background_music_loop_1.mp3`

Run the game:

```bash
python main.py
```


## Assets

The following assets were used in this project. Proper credit is given to the original authors:

1. **Win Sound Effect**  
   Source: [Win Sound Effect](https://opengameart.org/content/win-sound-effect)  
   Author: **Little Robot Sound Factory**

2. **Music Box - Game Over III**  
   Source: [Music Box - Game Over III](https://opengameart.org/content/music-box-game-over-iii)  
   Author: **Joth**

3. **Simple Dice 2**  
   Source: [Simple Dice 2](https://opengameart.org/content/simple-dice-2)  
   Author: **Lamoot**

4. **Tavern Music**  
   Source: [Tavern Music](https://pixabay.com/music/folk-medieval-citytavern-ambient-235876/)  
   Author: **Pixabay Contributors**