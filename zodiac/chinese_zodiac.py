#记录12生肖，根据年份来判断生肖

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
#print(chinese_zodiac[0:4])
#print(chinese_zodiac[-2])

year = 2018
print(year % 12)
print(chinese_zodiac[year % 12])


print('狗' in chinese_zodiac) #成员关系操作符 in或者not in打印true


print(chinese_zodiac + chinese_zodiac) #连接操作符，重复并且连接

print(chinese_zodiac*3)#循环操作符，重复连续打印