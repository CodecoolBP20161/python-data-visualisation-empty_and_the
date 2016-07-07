from images import Images
from databases import Databases


def main():
    database = Databases("admin_data.csv", "base_data.sql")
    database.connect_db()

    image_1 = Images("image_1.png", "RGB", 500, 500, "white")
    image_1.draw_on_image_version_1(database, 500, 500)
    image_1.save_image()

    image_2 = Images("image_2.png", "RGB", 500, 500, "white")
    image_2.draw_on_image_version_2(database, 500, 500)
    image_2.save_image()

main()
