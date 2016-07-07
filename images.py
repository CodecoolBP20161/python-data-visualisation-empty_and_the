from PIL import Image
from PIL import ImageDraw
from texts import Texts
from random import randint
from projects import Projects
from databases import Databases


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

    def draw_on_image_version_2(self, database, x_image, y_image):
        list_of_arguments = ["name", "main_color", "budget_value", "budget_currency"]
        list_from_sql = database.run_sql_command("""SELECT name, main_color, budget_value, budget_currency FROM project
        WHERE name IS NOT NULL and main_color IS NOT NULL;""")
        projects_object_list = Projects.get_projects_object_list(list_of_arguments, list_from_sql)
        list_text_objects = []
        for element in projects_object_list:
            list_text_objects.append(Texts(element.name, "arial.ttf", int(element.budget_eur/200), element.main_color[0],
                                     element.main_color[1], element.main_color[2]))
        for element in list_text_objects:
            element.draw_text(randint(0, x_image), randint(0, y_image), self)
