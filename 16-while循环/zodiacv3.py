#小写的u代表Unicode避免中文出错。
#元组内容太长可以通过换行进行调整，不影响功能性使用。
zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座',
           u'巨蟹座', u'狮子座', u'处女座', u'天秤座', u'天蝎座', u'射手座')
#元组嵌套功能，元组就是多个字符串放到一个组里。
zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
              (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

int_month = int(input('请输入月份：'))
int_day = int(input('请输入日期：'))

#使用for循环实现
# for zd_num in  range(0,len(zodiac_name)):
#     if zodiac_days[zd_num] >=(int_month,int_day):
#         print(zodiac_name[zd_num])
#         #此处会持续打印持续执行if循环，需要跳出。
#         break
#     elif int_month == 12 and int_day >23:
#         print(zodiac_name[0])
#         break

#使用while循环实现
n = 0
while zodiac_days[n] < (int_month,int_day):
    if int_month ==12 and int_day>23:
        break
        #若值大于12月23，则在执行n+=1之前，就已经跳出循环体，此时n=0，没来得及加1，
        #所以循环体最外层的print打印是正常的zodiac_name[0]也就是摩羯座。
    n += 1
#通过缩进来判断循环体语句块，缩进靠前则就是已经跳出了语句块
print(zodiac_name[n])
