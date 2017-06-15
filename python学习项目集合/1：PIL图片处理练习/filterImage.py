from PIL import Image, ImageDraw, ImageFont
'''
给定一张图片在这张图片上加一个小标签
'''
def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=40)
    fillcolor = "#ffffffff"
    width, height = img.size
    draw.text((0, 0), '1', font=myfont, fill=fillcolor)
    img.save('result1.jpg','jpeg')

    return 0
if __name__ == '__main__':
    image = Image.open('image.jpg')
    add_num(image)