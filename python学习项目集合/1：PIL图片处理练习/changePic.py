from PIL import Image, ImageDraw, ImageFont,ImageFilter
'''
给定一张图片在这张图片上加一个小标签
'''
def filterImage(img):
	im2 = img.filter(ImageFilter.BLUR)
	im2.save("r.jpg","jpeg")
if __name__ == '__main__':
    image = Image.open('image.jpg')
    filterImage(image)