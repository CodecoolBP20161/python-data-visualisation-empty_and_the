from PIL import Image
from PIL import ImageDraw
from csv_handler import CSVFile
from sql_handler import Databases

csv_file = CSVFile("admin_data.csv")
list_data = csv_file.get_data()
database = Databases(list_data[0], list_data[1], list_data[2], list_data[3])
database.connect_db()
Databases.create_table('base_data.sql')
sometext = database.run_sql_command("""SELECT company_name FROM project WHERE id = 1;""")
somenumber = database.run_sql_command("""SELECT budget_value FROM project WHERE id = 1;""")

img = Image.new("RGB", (512, 512), "red")
draw = ImageDraw.Draw(img)
text_options = {
    'fill': (255, 255, 255)
}
text_content = sometext[0][0] + somenumber[0][0]
text_size = draw.textsize(text_content)
draw.text((0, 0), text_content, **text_options)
draw.text((0, text_size[1]), text_content, **text_options)
draw.text((text_size[0], 0), text_content, **text_options)
draw.text(text_size, text_content, **text_options)
img.save('sample-out.png')
