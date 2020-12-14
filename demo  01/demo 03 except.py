

#try ... except语句


"""
try:
    代码块
except Exception as e:
   异常代码块
"""

#除法
def div(x,y):


    try:
        z = x / y
        return z
    except Exception as e:
        print(e)

print(div(6,3))
print(div(6,0))
print("abc")


#try ... except ... finally

f = None

try:
    f = open('a.txt','r')
    contents = f.readlines()
    for x in contents:
        print(x)


except Exception as e:
    print(e)

finally:
    print("~~~~~~~")
    if f:                #如果有对象的时候进行关闭操作，如果没有对象则不执行下面的代码
         f.close()


