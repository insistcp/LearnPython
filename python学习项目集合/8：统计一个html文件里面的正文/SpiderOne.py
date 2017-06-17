#-*- coding: UTF-8 -*-
'''
008:用来统计一个html文件中所有的正文内容
'''
import os,glob
from bs4 import BeautifulSoup
def findContent(url):
	# 打开本地文件
	with open(url) as f:
		# 使用BeautifulSoup框架将其以lxml文件的格式打开
		text = BeautifulSoup(f,"lxml")
		# 获取其中除去标签之后的内容
		content = text.get_text().strip("\n")
		#content = text.get_text()
		cont = content.encode("gbk","ignore")
		print(cont)
		t = open("demo1.txt","w")
		t.write(cont)
		return cont
if __name__ == "__main__":
	findContent("html/index.html")