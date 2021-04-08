#eg1
#i = j
#NameError: name 'j' is not defined

#eg2
#print())
#SyntaxError: invalid syntax

#eg3
#a = '123'
#print(a[3])
#IndexError: string index out of range
#元组总共三个元素，从0开始依次是 a[0] a[1] a[2]
#而a[3]超过了索引的长度，所以报错。as

#eg4 字典错误
#d = {'a':1,'b':2}
#print(d['c'])
#字典中不存在将要输出的key，所以此处报错。

###################
#以上错误通常是编码过程中出现的错误。
#另外有时候的错误是因为“输入过程中”数据类型不一致。
#比如：

#eg5
#year = int(input('input year:'))
#定义输入值为整数，如果此时输入字符串abc则会报错：ValueError: invalid literal for int() with base 10: 'agbd'

# try:
#     year = int(input('input year:'))
# except ValueError:
#     print('年份要输入数字')
#从try开始执行，此时出现错误时，回直接反馈提示。



#ctrl + / 批量注释



