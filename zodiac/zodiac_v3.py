zodiac_name = (u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
# #此处内容没有单引号，所以外侧可用单引号。
zodiac_days = ((1,20),(2,19),(3,21),(4,21),(5,21),(6,22),(7,23),(8,23),(9,23),(10,23),(11,23),(12,23))
# #元组可以使用嵌套功能。
chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"

cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0
z_num ={}
for i in zodiac_name:
    z_num[i] = 0

while True:

    #用户输入月份和日期
    int_year = int(input('请输入年份'))
    int_month = int(input('请输入月份：'))
    int_day = int(input('请输入日期：'))

    for zd_num in  range(len(zodiac_days)):
        if zodiac_days[zd_num] >= (int_month,int_day):
            print(zodiac_name[zd_num])
            break
        elif int_month == 12 and int_day > 23:
            print(zodiac_name[0])
            break
    print('%s 年的生肖是 %s' % (int_year, chinese_zodiac[int_year % 12]))


    cz_num[chinese_zodiac[int_year % 12]] += 1
    z_num[zodiac_name[zd_num]] += 1

    #输出统计信息
    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个' %(each_key,cz_num[each_key]))

    for each_key in z_num.keys():
        print('星座 %s 有 %d 个' %(each_key,z_num[each_key]))

