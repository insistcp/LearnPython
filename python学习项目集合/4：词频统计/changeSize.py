#-*-coding:utf-8-*-
from PIL import Image
# glob 是文件路径搜索模块:按照指定的路径查找相应的文件
import glob,os
def resize():
	for file in glob.glob(r"image/*.JPG"):
		# 把路径分割成dirname和basename，返回一个元组
		filepath,filname = os.path.split(file)
		# 分割路径，返回路径名和文件扩展名的元组
		fname,fext = os.path.splitext(filname)
		print(fname,"====",fext)
		ima = Image.open(file)
		w,h = ima.size
		if w>640:
			x = w/640.0
			w = 640
			h = int(h/x)
		if h>1136:
			x = h/1136.0
			h = 1136
			w = int(w/x)
		print("new size:",w,h)
		imo = ima.resize((w,h),Image.ANTIALIAS)
		imo.save("0005"+filname)
if __name__ == "__main__":
	print("===")
	resize()