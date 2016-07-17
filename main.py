from images import Images
from databases import Databases
from PIL import Image


def main():
    database = Databases("admin_data.csv", "base_data.sql")
    try:
        database.connect_db()
    except ConnectionError:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
    else:
        command = input("Please select an image number(1 or 2):")
        if command == "1":
            while True:
                image_1 = Images("image_1.png", "RGB", 500, 500, "white")
                try:
                    image_1.draw_on_image_version_1(database, 500, 500)
                except RuntimeError:
                    continue
                else:
                    image_1.save_image()
                    img = Image.open('image_1.png')
                    img.show()
                    break
        elif command == "2":
            while True:
                image_2 = Images("image_2.png", "RGB", 500, 500, "black")
                try:
                    image_2.draw_on_image_version_2(database, 500, 500)
                except:
                    continue
                else:
                    image_2.save_image()
                    img = Image.open('image_2.png')
                    img.show()
                    break

main()
