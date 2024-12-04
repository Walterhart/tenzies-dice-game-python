import tkinter as tk
from tkinter import ttk


class UIManager:
    """
    Handles all user interface elements for the Tenzies game.
    """

    def __init__(self, root, dice_image_manager, toggle_hold_callback, roll_dice_callback, reset_game_callback):
        """
        Initializes the UIManager with the main window and required callbacks.

        Args:
            root (tk.Tk): The main application window.
            dice_image_manager: Manages dice images for the game.
            toggle_hold_callback (function): Callback to handle toggling dice hold.
            roll_dice_callback (function): Callback to handle rolling dice.
            reset_game_callback (function): Callback to handle resetting the game.
        """
        self.root = root
        self.dice_image_manager = dice_image_manager
        self.toggle_hold_callback = toggle_hold_callback
        self.roll_dice_callback = roll_dice_callback
        self.reset_game_callback = reset_game_callback

        self.dice_buttons = []
        self.status_label = None
        self.roll_button = None
        self.reset_button = None

        # Custom styling
        self.root.configure(bg="#282c34")  
        self.create_widgets()

    def create_widgets(self):
        """
        Creates and styles the UI widgets including the title, dice buttons, roll/reset buttons, and status label.
        """
        # Configure the grid for layout management
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)  # Title
        self.root.rowconfigure(1, weight=3)  # Dice
        self.root.rowconfigure(2, weight=1)  # Buttons
        self.root.rowconfigure(3, weight=1)  # Status/Instructions

        # Title Label
        title_label = tk.Label(
            self.root,
            text="🎲 Tenzies Dice Game 🎲",
            font=("Comic Sans MS", 24, "bold"),
            bg="#282c34",
            fg="#61dafb",
        )
        title_label.grid(row=0, column=0, pady=20, sticky="n")

        # Frame for dice
        self.dice_frame = tk.Frame(self.root, bg="#282c34")
        self.dice_frame.grid(row=1, column=0, pady=10, sticky="n")
        for i in range(10):
            btn = tk.Button(
                self.dice_frame,
                image=self.dice_image_manager.get_image(1),
                command=lambda i=i: self.toggle_hold_callback(i),
                bg="#61dafb",
                activebackground="#21a1f1",
                relief="groove",
                width=80,
                height=80,
            )
            btn.grid(row=0, column=i, padx=5)
            self.dice_buttons.append(btn)

        # Buttons (Roll and Reset)
        button_frame = tk.Frame(self.root, bg="#282c34")
        button_frame.grid(row=2, column=0, pady=20)
        self.roll_button = ttk.Button(button_frame, text="🎲 Roll", command=self.roll_dice_callback)
        self.roll_button.grid(row=0, column=0, padx=10)

        self.reset_button = ttk.Button(button_frame, text="🔄 Reset", command=self.reset_game_callback)
        self.reset_button.grid(row=0, column=1, padx=10)

        # Status label (Instructions)
        self.status_label = tk.Label(
            self.root,
            text="Roll the dice to start!",
            font=("Arial", 16),
            bg="#282c34",
            fg="#ffffff",
        )
        self.status_label.grid(row=3, column=0, pady=10, sticky="n")

    def update_dice_display(self, dice, held):
        """
        Updates the dice display based on the current dice values and held status.

        Args:
            dice (list[int]): List of current dice values.
            held (list[bool]): List of dice hold statuses where True means held.
        """
        for i, btn in enumerate(self.dice_buttons):
            value = dice[i]
            btn.config(image=self.dice_image_manager.get_image(value))
            btn.config(bg="lightgreen" if held[i] else "#61dafb")

    def update_status_label(self, text):
        """
        Updates the status label with a given message.

        Args:
            text (str): The message to display in the status label.
        """
        self.status_label.config(text=text)

    def toggle_buttons(self, roll_visible, reset_visible):
        """
        Toggles the visibility of the roll and reset buttons.

        Args:
            roll_visible (bool): If True, the roll button is shown; otherwise hidden.
            reset_visible (bool): If True, the reset button is shown; otherwise hidden.
        """
        if roll_visible:
            self.roll_button.grid()
        else:
            self.roll_button.grid_remove()

        if reset_visible:
            self.reset_button.grid()
        else:
            self.reset_button.grid_remove()
