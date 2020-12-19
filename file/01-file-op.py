#文件操作非常重要，通常是指Windows常见文件。
#python抽象操作为文件
#基本操作：常见内建函数，指的是不用创建，内带使用。
#写入时一定记得要执行close，否则会丢失信息。
#尝试新建file_op.py

#注释应用功能：将小说的主要人物记录在文件当中
#open('name.txt')
#以上操作是以只读方式进行文件打开，无法写入，需要指定
file1 = open("name.txt",'w')
file1.write('诸葛亮/n123123123123')
file1.close()
#文件基本操作包括open write close
#下一步读取文件
#file1和file2都是变量
file2 = open('name.txt')
print(file2.read())


#通常除了普通文件，还会涉及到打开url之类的操作，所以read也叫做输入，write也叫做输出。

#希望读取一行，希望原有内容新增内容。
file3=open('name.txt','a')
file3.write('刘备')
#此处若不执行close操作，下一步进行读取时，将不会对"刘备"进行保存，所以输出会更file2一样。
file3.close()

file4=open('name.txt','r')
print(file4.read())