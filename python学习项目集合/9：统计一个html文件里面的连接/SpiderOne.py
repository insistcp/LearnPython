#!/usr/bin/python
#coding=utf-8

"""
第 0009 题：一个HTML文件，找出里面的链接
"""

from bs4 import BeautifulSoup
import os,glob
def find_the_link():
	# 用来保存所有的每一个文件对应的连接的字典
	dic = {}
	# 遍历当前文件夹下面对应的html文件
	for ht in glob.glob(r"html\\*.html"):
		# 用来存一个文件对应的连接
		links = []
		# 得到当前文件的文件名和文件路径
		filepath,filename = os.path.split(ht)
		with open(ht) as f:
			text = f.read()
			bs =BeautifulSoup(text,"lxml")
			for i in bs.find_all('a'):
			    links.append(i['href'])
			dic[filename] = links
			print(dic)
	return dic

if __name__ == '__main__':
    print find_the_link()