list1 = [1, 2, 3, 4]
it = iter(list1)
# print(next(it)) # 1
# print(next(it)) # 2


# print(next(it))
class iterClass:
    def __iter__(self):
        self.a = 3
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a = self.a + 1
            return x
        else:
            raise StopIteration
iterVal = iterClass()
myiter = iter(iterVal)
# print(next(myiter)) # 
for i in myiter:
    print(i)
print(next(myiter))
# 什么是质数： 质数又称素数。 一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；否则称为合数（规定1既不是质数也不是合数）。

def zhiShu():
    x
    u = int(input('input something num'))
    if u > 1:
        for uI in range(2,u):
            if u % uI == 0:
                x = 'u bszs'
                break
        else:                         #else可以跟在for循环后
            x = '是质数'
        
    else:
        x = 'bszs'
        #return 'Error'
    return x

'''
占位符
%s 字符串
%d 整数
%f 浮点数 默认保留6位小数
%.<num of digits>ƒ  保留小数点位数，四舍五入 例： %.2f 
%e 科学计数法 小写e
%E 科学计数法 大写e
%x  十六进制 字母大些
%X  十六进制 字母小写 1233456789abcdef 
%o 八进制
'''

x = 'good'
y = 1.5555
z = 10000000
b = 186
print('today is %s，and pick up %.1f'%(x,y))
print('%.2E have money'%z)
print('%x'%b)
# 类 类名
class gouYun:
    y = 1 # 公有变量
    __Nana = 7 # 私有变量

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    def showHeight(self):
        self.__showWeight()
        print('your height %dcm'%self.height)
    def __showWeight(self):
        print('gou yun id pig')

x = gouYun(100, 0) # 创建一个实例
x.showHeight()
# x.__showWeight()


