file4 = open('name.txt')
print(file4.readline())

file5 = open('name.txt')
for line in file5.readlines():
    print(line)
    print('=========')
