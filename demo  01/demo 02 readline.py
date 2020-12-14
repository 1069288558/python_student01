#常用的读取方法:
#1.read()
#2.readline() 一行一行读取数据，适用于大文件
#3.readlines()一次性读取文件所有内容，适合小文件

#写内容
#write()

#读取文件的两种方式:
#1.f = open(filename,'mode')
#2.with open(filename,'mode') as f:



#通过readline读取文件

"""
#1.打开文件
f = open('a.txt','r')


#2.读取文件内容(读取所有内容):readlines
contents = f.readlines()
for x in contents:
    print(x)

#3.关闭文件
f.close()
"""

"""
f = open('a.txt','r')
while True:
    content = f.readline()
    print(content)
    if not content:
        break
"""

#通过with进行读取文件

#格式 : with open(f,'r') as f



with open('a.txt','r') as f:
    all_lines = f.readlines()
    for x in all_lines:
        print(x)