# -*-coding:utf-8-*-
import re
'''
dsadasda

dsadas
'''


def count(url):
	filet = open(url)
	dic = {}
	# 一下子将所有文件都读进来
	line = filet.read()
	words = line.split()
	dic = {}
	for word in words:
		if dic.__contains__(word):
			dic[word] = dic[word]+1
		else:
			dic[word] = 1
	print(dic)
	#while line.split
	return 0
def num(path):
	with open(path,"r") as file:
		data = file.read()
		# 正则表达式 匹配匹配每一个单词：主要目的将标点符号过滤掉
		#compile好像是必须用的，用来格式转换什么的,然后才能进行匹配之类的操作
		print(words)
		words=re.compile('[a-zA-Z0-9]+') 
		dict={}
		for x in words.findall(data):
			if x in dict:
				dict[x]+=1
			else:
				dict[x] =1;
		print(dict)
if __name__ == "__main__":
	count("demo.txt")
	num("demo.txt")