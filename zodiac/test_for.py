#先学了字典，但是字典不够优雅，此处学习列表推导式。
#从解决问题开始
#1到10 所有偶数的平方
alist =[]
for i in range(1,11):
    if (i % 2 ==0):
        alist.append(i*i)

print(alist)


#以上写法为java习惯写法，若使用python可以进一步简化
blist =[i*i for i in range(1,11) if(i%2)==0]
print(blist)