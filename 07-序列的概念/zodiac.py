
#小写的u代表Unicode避免中文出错。
#元组内容太长可以通过换行进行调整，不影响功能性使用。
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
           u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
#元组嵌套功能，元组就是多个字符串放到一个组里。
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

#列表和元组的区别：列表使用[],元组使用(),列表内的元素可以修改，元组内的元素不可修改。
#列表具有删除、增加的功能。
#本次需求中针对星座属性不存在修改操作，此处便使用元组。

#星座和日期的对应关系此处为：下标都一致。

# 单个字符串可以进行比较，元组内的元素可以比较，元组也可以比较。
#使用比较运算符输出bool值，即是结果。

#cmd 输入 (1,20)>(2,20)返回的bool值为false。


(month, day) = (3, 15)

zodiac_day = filter(lambda  x: x<=(month, day), zodiac_days)
# 从zodiac_days这个元组中，取出对象，定义的(month,day)符合条件的第一个元组元素将被取出。
#取出的元素赋值给zodiac_day，此处数据类型为filter类型，后续会讲。

print(zodiac_day)
#filter类型打印时会显示 <filter object at 0x00000250266CDAC8>
#打开本行运行结果就报错，不知为什么。print(list(zodiac_day))


zodiac_len = len(list(zodiac_day)) % 12
# zodiac_day首先被转换为了list类型，否则无法使用len()判断长度
print(len(list(zodiac_day)))
print(zodiac_len)

print(zodiac_name[zodiac_len])



