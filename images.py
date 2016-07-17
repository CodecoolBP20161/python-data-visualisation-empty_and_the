import os
from PIL import Image
from PIL import ImageDraw
from texts import Texts
from random import randint
from projects import Projects
from companies import Companies


class Images:

    def __init__(self, name, rgb, width, height, color):
        self.name = name
        self.rgb = rgb
        self.width = width
        self.height = height
        self.color = color
        self.img = Image.new(self.rgb, (self.width, self.height), self.color)
        self.draw = ImageDraw.Draw(self.img)
        self.current_file_path = os.path.dirname(os.path.abspath(__file__))
        self.occupied_x = [{"a", "b"}]
        self.occupied_y = [{"a", "b"}]

    def save_image(self):
        self.img.save(self.name)

    def draw_list_text_objects(self, list_text_objects, x_image, y_image):
        list_text_objects.sort(key=lambda x: x.font_size, reverse=True)
        k = 0
        for element in list_text_objects:
            while True:
                break_boolean = False
                x_text = randint(0, x_image-element.text_size[0])
                y_text = randint(0, y_image-element.text_size[1])
                x_text_end = x_text + element.text_size[0]
                y_text_end = y_text + element.text_size[1]
                set_x_element = set(range(x_text, x_text_end))
                set_y_element = set(range(y_text, y_text_end))
                for i in range(len(self.occupied_x)):
                    if (set_x_element & self.occupied_x[i]) != set() and (set_y_element & self.occupied_y[i]) != set():
                        break_boolean = False
                        k += 1
                        if k > 20000:
                            raise RuntimeError("Image creation aborted!")
                        break
                    else:
                        break_boolean = True
                if break_boolean:
                    break
            self.occupied_x.append(set_x_element)
            self.occupied_y.append(set_y_element)
            element.draw_text(x_text, y_text, self)

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
        list_doge = ["so", "much", "very", "many", "wow", "such", "good", "how"]
        for element in companies_object_list:
            list_text_objects.append(
                Texts(list_doge[randint(0, 7)] + ' ' + element.name, self.current_file_path + "/fonts/Prototype.ttf",
                      int(element.number_of_projects * 6),
                      element.avg_color[0],
                      element.avg_color[1], element.avg_color[2]))
        file_title = open("doge_head.txt", "r")
        doge_head = file_title.read()
        text = Texts(doge_head, self.current_file_path + "/fonts/Cousine-Regular.ttf", 14, 0, 0, 0)
        self.occupied_x.append(set(range(0, 220)))
        self.occupied_y.append(set(range(200, 500)))
        text.draw_text(0, 200, self)
        self.draw_list_text_objects(list_text_objects, x_image, y_image)

    def draw_on_image_version_2(self, database, x_image, y_image):
        list_of_arguments = ["name", "main_color", "budget_value", "budget_currency"]
        list_from_sql = database.run_sql_command("""SELECT name, main_color, budget_value, budget_currency FROM project
        WHERE name IS NOT NULL and main_color IS NOT NULL;""")
        projects_object_list = Projects.get_projects_object_list(list_of_arguments, list_from_sql)
        list_text_objects = []
        for element in projects_object_list:
            list_text_objects.append(
                Texts(element.name, self.current_file_path + "/fonts/28_days_later.ttf", int(element.budget_eur / 250),
                      element.main_color[0],
                      element.main_color[1], element.main_color[2]))
        self.draw_list_text_objects(list_text_objects, x_image, y_image)
