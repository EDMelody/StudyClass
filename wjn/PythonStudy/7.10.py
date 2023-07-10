# name = input()
# print(name)

# 闰年：能被4整除，不能被100整除 或 能被400整
def gouYun(): # def 定义函数方法
    year = int(input('请输入年份'))
    # boolean 布尔类型
    gou = (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)
    if gou:
        return '闰年'
    else:
        return '平年'

# print(gouYun())


print(type(1))
# print(isinstance(123, int)) #判断变量数据类型

val = '123' 
print(val.isdigit()) # isdigit()判断字符串是否由数字字符组成

# 输入一个数字，判断一下这个数字是大于小于还是等于0
def yep():
    y = input('请输入数字')
    if y.isdigit():
        print()
    else:
        yep()
    y = int(y)
    if y > 0:
        return '大于0'
    elif y == 0: # 一个=是赋值；两个==是判断
        return '等于0'
    else:
        return '小于0'
    

# 判断质数：质数又称素数。 一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数（规定1既不是质数也不是合数）。
def w():
    q = int(input('请输入数字'))
    if q > 1:
        for a in range(2, q): # range(start, stop, step) 计数开始，计数结束（不包括当前值），步长
            if q % a == 0: #除数除完被除数，余数为0
                print('bushizhishu')
                break
        else:
            print('是质数')
    else:
        print('不是质数')


























