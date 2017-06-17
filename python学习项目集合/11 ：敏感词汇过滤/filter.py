# coding=utf-8

'''
第11题：敏感词汇哦
'''
import os
def tranfromtheword(file):
	wor  = raw_input(">")
	# 判断是否含有的标志
	judge_flag = False
	with open(file) as f:
		# 主要是为了解决 中文问题
		text = f.read().decode('GBK').encode("utf-8")
		#text = f.read()
		# 根据空格将字符串分开	
		for i in text.split("\n"):
			if i == wor:
				judge_flag = True
		if judge_flag:
			print("Freedom")
		else:
			print("Human Rights")
if __name__ == "__main__":
	tranfromtheword("word.txt")