from csvfiles import CSVfiles
from databases import Databases
from projects import Projects
from texts import Texts
from images import Images
from random import randint


def get_database():
    csv_file = CSVfiles("admin_data.csv")
    list_data = csv_file.get_data()
    database = Databases(list_data[0], list_data[1], list_data[2], list_data[3])
    database.connect_db()
    Databases.create_table('base_data.sql')
    return database


def draw_on_image_2(image_2, database):
    list_from_sql = database.run_sql_command("""SELECT name, main_color, budget_value, budget_currency FROM project
    WHERE name IS NOT NULL and main_color IS NOT NULL;""")
    list_of_arguments = ["name", "main_color", "budget_value", "budget_currency"]
    projects_object_list = Projects.get_projects_object_list(list_of_arguments, list_from_sql)
    list_text_objects = []
    for element in projects_object_list:
        list_text_objects.append(Texts(element.name, "arial.ttf", int(element.budget_eur/200), element.main_color[0],
                                 element.main_color[1], element.main_color[2]))
    for element in list_text_objects:
        element.draw_text(randint(0, 500), randint(0, 500), image_2)


def main():
    database = get_database()
    image_2 = Images("image_2.png", "RGB", 500, 500, "white")
    draw_on_image_2(image_2, database)
    image_2.save_image()

main()
