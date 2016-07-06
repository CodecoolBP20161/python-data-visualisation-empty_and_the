from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from csvfiles import CSVfiles
from databases import Databases
from projects import Projects

csv_file = CSVfiles("admin_data.csv")
list_data = csv_file.get_data()
database = Databases(list_data[0], list_data[1], list_data[2], list_data[3])
database.connect_db()
Databases.create_table('base_data.sql')
list_from_sql = database.run_sql_command("""SELECT name, main_color, budget_value, budget_currency FROM project
WHERE name = 'Voltsillam';""")
list_of_arguments = ["name", "main_color", "budget_value", "budget_currency"]
projects_object_list = Projects.get_projects_object_list(list_of_arguments, list_from_sql)
for element in projects_object_list:
    print(element.name, element.budget_eur, element.main_color)




img = Image.new("RGB", (500, 500), "white")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
font = ImageFont.truetype("arial.ttf", 16)
text_options = {
    'fill': element.main_color
}
text_content = "Sample Text"
text_size = font.getsize(text_content)
print(text_size)
# draw.text((x, y),text_content,(r,g,b))
draw.text((250, 250), text_content, font=font, **text_options)
draw.text((0, text_size[1]), text_content, **text_options)
draw.text((text_size[0], 0), text_content, **text_options)
draw.text(text_size, text_content, **text_options)
img.save('image2.png')
