""""
score = 69
if score >= 90:
    print("优秀")
elif score >= 70:
    print("良")
elif score >= 60:
    print("及格")
else:
    print("不及格")

sum = 0
a = 1
while a <= 100:
    sum += a
    a += 1
print(sum)


b = 1
while b <= 100:
    if b % 3 == 0:
        print(b)
    b += 1


t = 1,2,3,4
for e in t:
    print(e)



for w in range(0,8,1):
    print(w)


c = 1
while c <= 5:
    print(c)
    c += 1
    if c == 3:
        break

for q in range(0,10,1):
    if q == 3:
        break
    print(q)

d = 0
while d <= 8:
    d += 1
    if d == 6:
        continue
    print(d)

print("="*50)

for a in range(0,11,1):
    if a == 8:
        continue
    print(a)


list = [1,2,3,4,5]
for x in list:
    print(x)
print("="*100)


list = ["red","class","as"]
list.insert(0,"ix")
list.insert(1,"as")
list.append("sed")
list.clear()
print(list)


print("="*100)
a = (0,"red","x")
print(a)
for x in a:
    print(x)


c = 1
while c <= 5:
    print(c)
    c += 1
    if c == 3:
        break
print("+"*100)

b = {"city":"上海","name":"张三","age":10}
print(b["city"])
b["city"] = "北京"
print(b)
b["class"] = 10
print(b)
print("获取city对应的值",b.get("city"))
for key,value in b.items():
    print("key=",key,"value=",value)
for key in b.keys():
    print("key=",key)
for value in b.values():
    print("value=",value)
c = {'zhangsan': 23, 'lisi': 35}
print(c)
b.update(c)
print(b)
print("今天星期{0},今天花了{x}元,还剩{1}元".format(1,32,x=10))
list = ["is","and",1,2,"have"]
print("打印第五个元素",list[-1])
print("切取第二到第四个元素",list[1:4:1])
a = [1,2,3,4]
b = ["red","mox","six"]
c = a + b
print(c)
print("检查red是否在列表c中","red" not in c)
"""
"""
print("="*100)
print([x*2 for x in range(1,11,1) if x % 2 == 0])

print([y+str(x) for x in range(1,11,1) for y in ["a","b","c","d"]])
"""
#def add(a,b):
#    return a + b
#print(add(2,3))
"""

def add1(one,two):
    z = "{}年级,{}岁".format(one,two)
    return z
print(add1(two=3,one="张三"))

def add2(s,u=5):
    d = "{}年,{}月".format(s,u)
    return d
print(add2(u=6,s=8))
"""

#print([x for x in range(1,101,1) ])


























