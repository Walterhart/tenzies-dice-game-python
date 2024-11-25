import tkinter as tk

class UIManager:
    """
    Handles all user interface elements for the Tenzies game.
    """

    def __init__(self, root, dice_image_manager, toggle_hold_callback, roll_dice_callback, reset_game_callback):
        """
        Initializes the UI manager.

        Args:
            root: The Tkinter root window.
            dice_image_manager: An instance of DiceImageManager for dice images.
            toggle_hold_callback: A function to call when a dice is toggled.
            roll_dice_callback: A function to call when the roll button is pressed.
            reset_game_callback: A function to call when the reset button is pressed.
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

        self.create_widgets()

    def create_widgets(self):
        """
        Creates UI widgets.
        """
        # Frame for dice
        self.dice_frame = tk.Frame(self.root)
        self.dice_frame.pack(pady=20)

        # Dice buttons
        for i in range(10):
            btn = tk.Button(
                self.dice_frame,
                image=self.dice_image_manager.get_image(1),
                command=lambda i=i: self.toggle_hold_callback(i),
                width=80,
                height=80,
            )
            btn.grid(row=0, column=i, padx=5)
            self.dice_buttons.append(btn)

        # Roll button
        self.roll_button = tk.Button(self.root, text="Roll", font=("Arial", 18), command=self.roll_dice_callback)
        self.roll_button.pack(pady=20)

        # Reset Button
        self.reset_button = tk.Button(self.root, text="Reset", font=("Arial", 18), command=self.reset_game_callback)
        self.reset_button.pack(pady=10)

        # Status label
        self.status_label = tk.Label(self.root, text="Roll the dice to start!", font=("Arial", 16))
        self.status_label.pack(pady=10)

    def update_dice_display(self, dice, held):
        """
        Updates the dice display based on current dice values and held status.

        Args:
            dice: List of dice values (1-6).
            held: List of boolean values indicating if dice are held.
        """
        for i, btn in enumerate(self.dice_buttons):
            value = dice[i]
            btn.config(image=self.dice_image_manager.get_image(value))
            btn.config(bg="lightgreen" if held[i] else "SystemButtonFace")

    def update_status_label(self, text):
        """
        Updates the status label with a given message.

        Args:
            text: The message to display.
        """
        self.status_label.config(text=text)

    def toggle_buttons(self, roll_visible, reset_visible):
        """
        Toggles the visibility of the roll and reset buttons.

        Args:
            roll_visible: Whether the roll button should be visible.
            reset_visible: Whether the reset button should be visible.
        """
        if roll_visible:
            self.roll_button.pack(pady=20)
        else:
            self.roll_button.pack_forget()

        if reset_visible:
            self.reset_button.pack(pady=10)
        else:
            self.reset_button.pack_forget()
