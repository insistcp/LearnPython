#!/usr/bin/python
#coding=utf-8

"""
第 00010 题：生成验证码
"""
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
# 获取随机字符
def getChar():
	return chr(random.randint(65,90))
# 获取随机背景颜色
def getRandom1():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
# 获取字符的随机颜色
def getRandom2():
	return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
# 定义验证码的宽度
width = 64*4
# 定义验证码的高度
height = 60
# 生成验证码的图片
image = Image.new("RGB",(width,height),(255,255,255))
# 生成字体
font = ImageFont.truetype("C:/windows/fonts/Arial.ttf",36)
# 生成画板
draw = ImageDraw.Draw(image)
for x in range(width):
	for y in range(height):
		draw.point((x,y),fill=getRandom1())
# 生成验证码上面的字符
for f in range(4):
	temp = getChar()
	print(temp)
	draw.text((60*f+10,10),temp,font= font,fill = getRandom2())
image = image.filter(ImageFilter.BLUR)
image.save("result.jpg","jpeg")
