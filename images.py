import os
from PIL import Image
from PIL import ImageDraw
from texts import Texts
from random import randint
from projects import Projects
from companies import Companies

current_file_path = os.path.dirname(os.path.abspath(__file__))


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

    def draw_on_image_version_1(self, database, x_image, y_image):
        list_of_arguments = ["name", "number_of_projects", "avg_color"]
        list_from_sql_1 = database.run_sql_command("""SELECT company_name, COUNT(*), NULL
                                                      FROM project WHERE main_color is NOT NULL
                                                      GROUP BY company_name""")
        list_from_sql_2 = database.run_sql_command("""SELECT company_name, main_color FROM project
                                                      WHERE main_color is NOT NULL""")
        list_from_sql = []
        for i in range(len(list_from_sql_1)):
            list_from_sql.append(list(list_from_sql_1[i]))
            list_from_sql[i][2] = []
        for i in range(len(list_from_sql_2)):
            for j in range(len(list_from_sql)):
                if list_from_sql_2[i][0] == list_from_sql[j][0]:
                    list_from_sql[j][2].append(list_from_sql_2[i][1])
        companies_object_list = Companies.get_companies_object_list(list_of_arguments, list_from_sql)
        list_text_objects = []
        for element in companies_object_list:
            list_text_objects.append(Texts(element.name, current_file_path + "/fonts/Prototype.ttf",
                                           element.number_of_projects * 10, element.avg_color[0], element.avg_color[1],
                                           element.avg_color[2]))
        for element in list_text_objects:
            element.draw_text(randint(0, x_image), randint(0, y_image), self)

    def draw_on_image_version_2(self, database, x_image, y_image):
        list_of_arguments = ["name", "main_color", "budget_value", "budget_currency"]
        list_from_sql = database.run_sql_command("""SELECT name, main_color, budget_value, budget_currency FROM project
        WHERE name IS NOT NULL and main_color IS NOT NULL;""")
        projects_object_list = Projects.get_projects_object_list(list_of_arguments, list_from_sql)
        list_text_objects = []
        for element in projects_object_list:
            list_text_objects.append(
                Texts(element.name, current_file_path + "/fonts/Prototype.ttf", int(element.budget_eur / 200),
                      element.main_color[0],
                      element.main_color[1], element.main_color[2]))
        for element in list_text_objects:
            element.draw_text(randint(0, x_image), randint(0, y_image), self)
