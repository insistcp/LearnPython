# -*-coding:utf-8 -*-
import os,glob
import re

'''
题目描述：给定一个文件夹。文件夹下面有很多文件现在让你统计每一个文件中的最重要n个词汇
'''
def count():
	# 键为文件名，值为dict保存文件中前n个词汇以及对应的频率
	dict = {}
	# 搜索dialy目录下所有的txt文件
	for dialy in glob.glob(r"dialy/*.txt"):
		# 将对应的文件的路径和文件名分离开来
		filepath,filename = os.path.split(dialy)
		# 将文件打开作为一个file
		with open(dialy) as file:
			# 读取文件中的数据
			data = file.read()
			# 设计好正则表达式，将所有的单词匹配出来
			words = re.compile("[a-zA-Z0-9]+")
			# 用来单个文件各个单词对应的频率
			dialyS = {}
			for word in words.findall(data):
				if word in dialyS:
					dialyS[word] = dialyS[word]+1
				else:
					dialyS[word]=1
			# 使用sort函数对我们的dic进行排序按照降序排列
			dict[filename] = sorted(dialyS.iteritems(),key=lambda d:d[1],reverse=True)[0:10]
	for ass in dict:
		print(ass,"==",dict[ass])
if __name__ == "__main__":
	count()	