#使用Calc

#1.通过import导入: import 文件名

import calc

#导入之后使用calc模块中的方法：包名加类名

#cl = calc.Calc()
#print(cl.add1(3,4))

#通过 from .... import 导入: from 包名 import 类名/函数/方法

from calc import Calc

cl = Calc()
print(cl.add2(3,4))

