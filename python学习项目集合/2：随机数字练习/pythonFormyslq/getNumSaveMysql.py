#-*- coding: UTF-8 -*-
import uuid
import pymysql
# �����������
def getRandom(num):
	codeList = []
	for i in range(num):
		code = str(uuid.uuid4()).replace("-","").upper()
		print(code,"===",len(code),"===",uuid.uuid4())
		while code in codeList:
			code = str(uuid.uuid4()).replace("-","").upper()
		codeList.append(code)
	return codeList
# �����ݲ��뵽mysql���ݿ���
def saveIntoMysql(codelist):
	try:
		# ��ȡ���ݿ�����
		conn = pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="mysql")
		# 
		cur = conn.cursor()
	except BaseException as e:
		print("------",e)
	else:
		try:
			# �������ݿ����Ӧ�����ݱ�
			cur.execute("create database if not exists activation_code")
			cur.execute("use activation_code")
			cur.execute('''create table if not exists code(
				id int not null auto_increment,
				code varchar(32) not null,
				primary key(id)
			)''')
			# �����ݿ��в�������
			for x in codelist:
				cur.execute("insert into code(code) value(%s)",(x))
				cur.connection.commit()
		except BaseException as e:

			print("========",e)
	finally:
		cur.close()
		conn.close()
if __name__ == "__main__":
	saveIntoMysql(getRandom(10))
	print("OK!")