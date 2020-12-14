"""
def add1(*args):
    print(args)
    print(type(args))
    for x in args:
        print(x,end = " ")
a = ["z","c","v"]
print(add1(a))
"""
"""
def add2(x,y,*args):
    sum = x + y
    for z in args:
        sum += z
    return sum

a = [5,8]
print(add2(3,4,*a))
"""
"""
def add3(**kwargs):
    print(kwargs)
print(add3(key1=2,key2=3))
c = {"name":"张三","class":2}
print(add3(**c))
"""
"""
class mox():
    a = "按钮"
    max_people = 15
    fools = 8

    def open(self):
        print("开门")

    def close(self):
        print("关门")

    def run(self,nums):
        print("我要去{}楼".format(nums))

vx = mox()
vx.run(3)
"""
"""
class students():
    name = " "
    grade = " "

    def study(self):
        print("我叫{},现在上{}年级".format(self.name,self.grade))

vm = students()
vm.name = "李四"
vm.grade = 6
vm.study()
"""

class students():
    #属性:
    name = " "
    grade = " "

    #构造方法：
    def __init__(self,name,grade):
       self.name = name
       self.grade = grade


    #方法:
    def study(self,age):
        self.age = age

        print("我叫{},现在上{}年级,今年{}岁".format(self.name,self.grade,self.age))

#lisi = students("李四",3)
#lisi.name = "王五"lisi.study()
#lisi.study()

#通过对象访问：
#lisi = students("李四",3)
#lisi.name = "王五"
#lisi.study()

#通过类名访问：
#students.name = "麻子"
#students().study()

#访问实例变量只能通过对象：
#zs = students("张三",6)
#zs.study(6)