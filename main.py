from images import Images
from databases import Databases


def main():
    database = Databases("admin_data.csv", "base_data.sql")
    database.connect_db()
    image_2 = Images("image_2.png", "RGB", 500, 500, "white")
    image_2.draw_on_image_version_2(database)
    image_2.save_image()

main()
