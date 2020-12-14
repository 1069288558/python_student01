
def add(x,y):
    if not (isinstance(x,int)) or (isinstance(x,float)):
        return  "输入的参数x必须是整数或浮点数"
    if not (isinstance(y,int)) or (isinstance(y,float)):
        return  "输入的参数y必须为是不为0的整数或浮点数"
    if y == 0:
        return "输入的参数y必须为是不为0的整数或浮点数"
    return x / y
