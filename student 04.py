def add2(x,y,*args):
    sum = x + y
    for z in args:
        sum += z
    return sum

a = [5,8]
print(add2(3,4,*a))