from images import Images
from databases import Databases


def main():
    database = Databases("admin_data.csv", "base_data.sql")
    database.connect_db()

    while True:
        image_1 = Images("image_1.png", "RGB", 500, 500, "white")
        try:
            image_1.draw_on_image_version_1(database, 500, 500)
        except:
            continue
        else:
            image_1.save_image()
            break

    while True:
        image_2 = Images("image_2.png", "RGB", 500, 500, "black")
        try:
            image_2.draw_on_image_version_2(database, 500, 500)
        except:
            continue
        else:
            image_2.save_image()
            break

main()
