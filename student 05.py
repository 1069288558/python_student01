"""
class Demo():
    name = " "
    age = 10

    def add1(self):


        print(self.age,self.name)

vm = Demo()
vm.add1()

class Students():
    s_name = " "
    s_age = 0

    def get_age(self,age):
        return self.s_age

#访问Demo中的方法：
    def show(self):
        d = Demo()
        d.add1()
"""

"""
class people():


    def say(self):
        print("可以说话")


class students(people):
    def __init__(self,sf):
        self.sf = sf

    def study(self):
#如果想使用父类中的方法使用 super().方法即可
        super().say()
        print("学生学习")

    def say(self):
        print("{}可以说话".format(self.sf))

class Teachers(people):

    def teach(self):
        print("老师教书")

zs = students("初中生")
zs.study()
"""



