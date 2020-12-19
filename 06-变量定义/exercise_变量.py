# 练习一 变量的定义和使用

# 1. 定义两个变量分别为美元和汇率
# 2. 通过搜索引擎找到美元兑人民币汇率
# 3. 使用Python计算100美元兑换的人民币数量并用print( )进行输出

dollar = 100

exchange = 6.4696

print('美元兑换的人民币总数是')

print('{dol}美元兑换的人民币总数是{yuan}'.format(dol=dollar,yuan=dollar * exchange))
#print函数里可以通过{}定义参数，使用.format函数可以对参数赋值，赋值的对象是已经定义过的变量值。