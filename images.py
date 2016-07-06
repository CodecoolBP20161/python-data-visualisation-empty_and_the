from PIL import Image
from PIL import ImageDraw


class Images:

    def __init__(self, name, rgb, width, height, color):
        self.name = name
        self.rgb = rgb
        self.width = width
        self.height = height
        self.color = color
        self.img = Image.new(self.rgb, (self.width, self.height), self.color)
        self.draw = ImageDraw.Draw(self.img)

    def save_image(self):
            self.img.save(self.name)
