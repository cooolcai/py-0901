# 记录生肖，根据年份来判断生肖，判断星座根据月份和日期
# 可以使用变量，但一个年份对应一个生肖的话，太繁琐。
# 一个变量可以是特殊类型
# 序列：字符串有序排列。 通过下标偏移量可以访问到某个成员或者某介个成员。
# 序列包括：字符串、列表、元组。
# 字符串也是序列，可以使用下标记。

#chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
# 字符串可以使用单引号和双引号，字符串内的值存在单引号是，为避免配对，最外层应该使用双引号。
print(chinese_zodiac[3])
print(chinese_zodiac[0:3])
print(chinese_zodiac[-1])

#年份与生肖的对应关系是取余数
year = 2018
print(year % 12)
#2018年取余数等于2，下标值为2时，2018年实际上时狗年。
#此处可以调整字符串先后关系，进行准确对应。
# 将第8行注释,修改为第9行内容。若print在变量定义之前执行，则会报错。
print(chinese_zodiac[year % 12])



# 序列的基本操作：成员关系操作符、连接操作符、重复操作符、切片操作符号。
# (in not in + * ：),读取某几个字符串中的对象就是分片操作。
#演示关系操作
print('狗' in chinese_zodiac)
print('狗' not in chinese_zodiac)
#演示连接操作:可连接已定义的字符串，也可以连接自定义的字符串
print(chinese_zodiac + 'abcd')
#演示重复操作
print(chinese_zodiac * 3)



# chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'
#
# # print (chinese_zodiac[0:4] )
#
# # print (chinese_zodiac[-1])
#
# year = 2018
# print (year % 12)
#
# print (chinese_zodiac[year % 12])
#
# print ( '狗'  not in chinese_zodiac )
#
# print (chinese_zodiac + 'abcd')
#
# print (chinese_zodiac * 3 )
