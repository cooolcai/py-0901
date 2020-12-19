chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

#for循环
#遍历整个字符串的内容，若临时变量cz存在于字符串中，则打印cz。
for cz in chinese_zodiac:
    print(cz)


#遍历数字，range13。可接受两个值如(2,13)
for i in range(13):
    print(i)


#字符串替换功能：
for year in range(2000,2020):
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))
    print('%s 年的生肖是 %s' % ('year', chinese_zodiac[year % 12]))
    #打印的字符串中可以用%s进行替换，有几个%s旧在字符串完成后的()内写上几个目标字符串或者变量