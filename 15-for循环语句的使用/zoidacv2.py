#小写的u代表Unicode避免中文出错。
#元组内容太长可以通过换行进行调整，不影响功能性使用。
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
           u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
#元组嵌套功能，元组就是多个字符串放到一个组里。
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

#列表和元组的区别：列表使用[],元组使用(),列表内的元素可以修改，元组内的元素不可修改。
#列表具有删除、增加的功能。

#输入需要的月份和日期，但是后续会需要使用数字进行计算比较。
#input输入的内容默认为字符串类型，可通过以下代码进行验证
#此处为便于使用，将month直接写成str_month
# str_month = input('请输入月份：')
# str_day = input('请输入日期：')
# print(type(str_month))
# print("str_month的内容是 %s ，类型是 %s " % (str_month,type(str_month)))

# 可以对上述输入的内容进行强制转换
int_month = int(input('请输入月份：'))
int_day = int(input('请输入日期：'))
print("int_month的内容是 %s ，类型是 %s " % (int_month,type(int_month)))#可以使用type()查看属性。

for zd_num in  range(0,len(zodiac_name)):
    if zodiac_days[zd_num] >=(int_month,int_day):
        print(zodiac_name[zd_num])
        #此处会持续打印持续执行if循环，需要跳出。
        break
    elif int_month == 12 and int_day >23:
        print(zodiac_name[0])
        break
#zodiac_day = filter(lambda  x: x<=(month, day), zodiac_days)
# 从zodiac_days这个元组中，取出对象，定义的(month,day)符合条件的第一个元组元素将被取出。
#取出的元素赋值给zodiac_day，此处数据类型为filter类型，后续会讲。

#print(zodiac_day)
#filter类型打印时会显示 <filter object at 0x00000250266CDAC8>
#打开本行运行结果就报错，不知为什么。print(list(zodiac_day))


#zodiac_len = len(list(zodiac_day)) % 12
# zodiac_day首先被转换为了list类型，否则无法使用len()判断长度
#print(len(list(zodiac_day)))
#print(zodiac_len)

#print(zodiac_name[zodiac_len])