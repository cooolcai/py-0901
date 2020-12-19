# 序列：字符串有序排列。 通过下标偏移量可以访问到某个成员或者某介个成员。
# 序列包括：字符串、列表、元组。
# 字符串也是序列，可以使用下标记。

#chinese_zodiac = '鼠牛虎兔龙蛇马羊猴鸡狗猪'
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

#while循环当条件一直为真时，会循环后续代码块
while True:
    print('a')
    #使用break语句可以条出当前循环。
    break

#持续打印b，知道num大于10后中止循环
num = 5
while True:
    print('b')
    temp = num +1
    num = temp
    #上两行的写法可以写成 num = num + 1
    if num > 10:
        break

#如何使用continue？当满足if条件时，不执行本次循环，进入下一次while的循环块
import time
num_2 = 0
while True:
    num_2 = num_2 + 1
    if num_2 <10:
        continue
    #print打印从0开始的数字，当条件满足if时，则跳过当前代码块，直接continue到下一次循环。
    #注释if-continue则会从0开始打印。
    #不注释if-continue则会从11开始打印，因为0-10满足if条件，直接跳过并进入了下一次循环，此处便从11开始打印。
    print(num_2)
    time.sleep(1)

