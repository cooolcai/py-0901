#记录12生肖，根据年份来判断生肖

chinese_zodiac = "猴鸡狗猪鼠牛虎兔龙蛇马羊"
#print(chinese_zodiac[0:4])
#print(chinese_zodiac[-2])

# year = int(input('请用户输入出生年份')) #int方法，强制转换用户输入年份，将字符串转换成数字类型。
#
# if (chinese_zodiac[year % 12]) == '狗':
#     print ('狗年运势ok')
##################################################33
# for cz in chinese_zodiac:
#     print(cz)
#
# for i in range(1,13):
#     print(i)
#
# for year in range(2000,2019):
#     print('%s 年的生肖是 %s' %(year,chinese_zodiac[year % 12]))
#######################################################
# print('狗' in chinese_zodiac) #成员关系操作符 in或者not in打印true
#
#
# print(chinese_zodiac + chinese_zodiac) #连接操作符，重复并且连接
#
# print(chinese_zodiac*3)#循环操作符，重复连续打印
########################################################
import time
num = 5
while True:
#    print('a')
#    temp = num +1
#    num = temp
    num = (num + 1)
    if num == 10 :
        continue #跳过当前次的循环

    print(num)
    #time.sleep(2)
