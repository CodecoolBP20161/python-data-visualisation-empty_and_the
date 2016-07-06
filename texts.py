from PIL import ImageFont


class Texts:
    def __init__(self, text_content, font, font_size, red, green, blue):
        self.text_content = text_content
        self.font = ImageFont.truetype(font, int(font_size))
        self.font_size = font_size
        self.text_size = self.font.getsize(text_content)
        self.r = red
        self.g = green
        self.b = blue

    def draw_text(self, x, y, img_object):
        text_options = {'fill': (self.r, self.g, self.b)}
        img_object.draw.text((x, y), self.text_content, font=self.font, **text_options)
