

#文件的操作步骤



# 1.需要打开文件:open()
f = open('a.txt','r')

"""
#2.读取文件:read()
content = f.read() 
print(content)
#  写文件:write()


#3.关闭文件:close()
f.close()
"""

#1.需要打开文件:open()
f = open('a.txt','w')


# 2.写文件:write()
f.write('python java')


#3.关闭文件:close()
f.close()