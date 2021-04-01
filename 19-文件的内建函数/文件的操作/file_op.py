#将小说的主要人物记录再文件中
file1 = open('name.txt','w')
#通过提示信息查看函数使用方法，比如打开、写入模式、读取模式等。
file1.write('诸葛亮')
file1.close()
#执行以上命令后，会创建name.txt 文件并写入诸葛亮

#读取某个文件
file2 = open('name.txt')
print(file2.read())
file2.close()




#更复杂的操作，读取一行，在原有基础上添加新的内容

file3 = open('name.txt','a')
file3.write('  刘备')
file3.close()


#尝试读取文件中的一行
file4 = open('name.txt')
print( file4.readline() )

file5 = open('name.txt')



