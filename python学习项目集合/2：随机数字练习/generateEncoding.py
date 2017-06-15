#-*-coding:utf-8 -*-
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random,string
# 获取一个随机字母
def rndChar():
	return chr(random.randint(65,90))
# 获取随机色（用于填充图片的背景色）
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 获取随机色2
def rndColor2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
# 图片的宽度
width = 60*4
# 图片的高度
height = 60
# 新建一张图片
image  = Image.new("RGB",(width,height),(255,255,255))
# 创建font对象
font = ImageFont.truetype("C:/windows/fonts/Arial.ttf",36)
# 创建画笔
draw = ImageDraw.Draw(image)
# 随机色填充每一个像素
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=rndColor())
# 生成验证码上的字符
for t in range(4):
	draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
# 添加滤镜
#image = image.filter(ImageFilter.BLUR)
image.save("code.jpg","jpeg")
