from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.new("RGB", (512, 512), "red")
draw = ImageDraw.Draw(img)
# font = ImageFont.truetype(<font-file>, <font-size>)
# font = ImageFont.truetype("sans-serif.ttf", 16)
list_companies =  ['Jaxnation', 'Wikizz', 'Brainbox', 'Ozu', 'Youspan', 'Youbridge', 'Skinix', 'Npath', 'Skyndu', 'Twinder', 'Divavu', 'Oyonder', 'Camimbo', 'Bubbletube', 'Skivee', 'Eadel', 'Thoughtbridge', 'Feedfish', 'Edgetag', 'Oozz', 'Skiba', 'Jabbersphere', 'Talane', 'Meemm', 'Viva', 'Brainverse', 'Rhybox', 'Oyoba', 'Tagtune', 'Tambee', 'Lazzy', 'Fiveclub', 'Skynoodle', 'Lajo', 'Gabcube', 'Brainsphere', 'Buzzster', 'Gigashots', 'Photofeed', 'Kazio', 'Yotz', 'Gigabox', 'Browsebug', 'Tanoodle', 'Muxo', 'Topicware', 'Yodo']
list_avg_colors =  [[46, 102, 153], [146, 136, 153], [110, 74, 91], [95, 121, 78], [187, 195, 187], [34, 51, 255], [221, 255, 204], [204, 85, 136], [187, 153, 221], [34, 170, 153], [59, 51, 204], [102, 110, 187], [102, 204, 110], [221, 119, 127], [255, 153, 136], [117, 154, 170], [138, 124, 96], [153, 51, 119], [0, 17, 102], [34, 221, 34], [136, 170, 136], [102, 136, 0], [229, 51, 102], [0, 68, 136], [221, 51, 136], [221, 0, 238], [144, 144, 76], [45, 96, 28], [170, 255, 119], [153, 85, 51], [187, 102, 0], [25, 119, 187], [119, 119, 238], [34, 102, 51], [102, 204, 170], [119, 238, 136], [255, 34, 17], [102, 102, 221], [136, 17, 238], [72, 178, 85], [212, 136, 221], [116, 146, 144], [51, 187, 187], [119, 85, 170], [191, 119, 157], [17, 76, 204], [110, 93, 51]]
number_of_projects =  [4, 5, 8, 8, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 1, 9, 6, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 3, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 4, 2, 8, 1, 1, 4, 2, 2]
text_options = {
    'fill': (255, 255, 255)
}
text_content = "Sample Text"
text_size = draw.textsize(text_content)
# draw.text((x, y),text_content,(r,g,b))
draw.text((0, 0), text_content, **text_options)
draw.text((0, text_size[1]), text_content, **text_options)
draw.text((text_size[0], 0), text_content, **text_options)
draw.text(text_size, text_content, **text_options)
img.save('sample-out.png')
