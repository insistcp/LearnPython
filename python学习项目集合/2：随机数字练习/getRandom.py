#-*-coding:utf-8 -*-
import random,string
forSelect = string.ascii_letters+"0123456789"
print(forSelect)
def generate(count,length):
	dic = {}
	for x in range(count):
		Re = ""
		for y in range(length):
			Re+=random.choice(forSelect)
		dic[x] = Re
		print(dic)
if __name__ == "__main__":
	generate(10,10)