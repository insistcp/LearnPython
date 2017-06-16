# -*-coding:utf-8 -*-
import os,glob
import re
'''
**第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
包括空行和注释，但是要分别列出来。
'''
def count():
	# 键为文件名，值为dict保存文件中前n个词汇以及对应的频率
	dict = {}
	# 搜索dialy目录下所有的txt文件
	for dialy in glob.glob(r"coding/*.*"):
		# 将对应的文件的路径和文件名分离开来
		filepath,filename = os.path.split(dialy)
		# 将文件打开作为一个file
		NoteCount =0
		AllCount = 0
		otherCount = 0
		nullCount = 0
		code = {}
		with open(dialy) as file:
			# 读取文件中的数据
			#data = len(file.readlines())
			#  用来控制特殊的“'''”注释
			flag=0
			while 1:
				line = file.readline()
				if not line:
					break
				if ("#" in line) & (flag==0):
					NoteCount = NoteCount+1
					print("this is node")
				elif (not line.strip()) & (flag==0):
				 
					nullCount = nullCount+1
					print("s is null")
				elif "'''" in line:
					if flag==0:
						flag=1
						NoteCount = NoteCount+1
					else:
						flag=0
						NoteCount = NoteCount+1
				 
				elif flag==1:
					NoteCount = NoteCount+1
				elif flag==0:
					otherCount = otherCount+1
				AllCount = AllCount+1

		 
			code["NoteCount"] = NoteCount
			code["nullCount"] = nullCount
			code["otherCount"] = otherCount
			code["AllCount"] = AllCount
		dict[filename] = code 
	for ass in dict:
		print(ass,"==",dict[ass])
if __name__ == "__main__":
	count()	