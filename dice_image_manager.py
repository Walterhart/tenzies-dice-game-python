from PIL import Image, ImageTk

class DiceImageManager:
    """
    A class to manage images for dice for the tenzies game.
    """
    def __init__(self, image_dir="images", size=(80, 80)):
        """
        Initializes the DiceImageManager instance and loads dice images.
        """
        self.image_dir = image_dir
        self.size = size
        self.images = self.load_images()

    def load_images(self):
        """
        Load images for dice faces into a dictionary and resize them.
        :return: Dictionary of dice face images {1: image1, ..., 6: image6}.
        """
        images = {}
        for i in range(1, 7):
            try:
                # Open and resize image
                img_path = f"{self.image_dir}/dice_{i}.png"
                pil_image = Image.open(img_path)
                resized_image = pil_image.resize(self.size, Image.Resampling.LANCZOS)

                # Convert to a PhotoImage object for Tkinter
                images[i] = ImageTk.PhotoImage(resized_image)
            except Exception as e:
                print(f"Error loading image for dice {i}: {e}")
        return images

    def get_image(self, value):
        """
        Returns the image for the given dice face value.
        :param value: Dice face value (1 to 6).
        :return: Corresponding image object.
        """
        return self.images.get(value, None)
