# 1.三种写注释的方法：# ''' """
# 单行注释
'''
多行注释
'''
"""
多行注释
"""
'''
2.字符串要加括号和引号-('')
3.Python中单引号双引号通用-既可以使用单引号''，也可以使用双引号""
'''
print("Hello world")

# 4.转义符:\ \n:换行 r:使\不发生转义 r后面不要空格
print("臭狗韵,\n 太对了！")
print(r"言之有理,\n 哼")

# 注意缩进
if True:
    print('True')
else:
    print('False')

'''
5.注意缩进。在python里搜行缩进不对也是会报错的。以下是缩进不一致导致的错误
一般在缺少空格或者缩进的时候出现IndentationError

if True:
    print('True')
else:
print('false')
'''

"""
6.标识符=变量，可以随意命名（就像给狗韵起外号一样），但是命名有一定的规则：
    （1）第一个字符必须是字母或者下划线_
    （2）标识符的其他部由字母、数字和下划线组成
    （3）标识符对大小写敏感
    （4）标识符!=关键字
"""

"""
7.python中常用的关键字：
    ['False', 'None', 'True', 'and', 'as', 'assert',
    'break', 'class', 'continue', 'def', 'del', 'elif',
    'else', 'except', 'finally', 'for', 'from', 'global',
    'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not',
    'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

"""
整数变量 = 999
浮点型变量 = 0.99
字符串 = '999'
"""
counter = 999
count = 0.99
strCount = '999'
val1,val2,val3 = 999, 0.99, '999'
print(count + counter) #浮点数和整数相加，输出的数据类型为浮点数
#print(count + strCount) #浮点数/整数和字符串不能相加
#True和False是布尔类型，True=1，False=0
nora1 = True 
nora2 = False 

print(nora1 + count) 
print('------显目--------')
nora3 = isinstance(nora1,str) #isinstance:判断变量是否为指定的字符类型，返回值为布尔类型True 或 False
print(nora3)


gouYun = ['哪个','是','数','据','随','便','加']
    #索引：  0     1   2    3    4    5   6
print(gouYun[1]) #打印索引为1的元素
print(gouYun[2:]) #从第二个元素打印到最后
print(gouYun[2:4]) #从第二个元素打印到第四个元素，但是不包含第四个
print(gouYun[2:7])  
print(gouYun[2:7:3]) #从第二个开始到第七个每间隔两个（步长为3）
print(gouYun * 2) # *n:重复字符n遍

gou = ['哪个','是','数','据','随','便','加']
print(gouYun + gou) # 连接列表
print(type(gou)) #打印类型为列表list
print(type(count)) #打印类型为浮点型float
print(type(counter))
print(type(strCount))

yun = ('哪个','是','数','据','随','便','加') #元组Tuple
print(yun)
#yun[0] = 1 #元组里的元素不能被修改
yun1 = ('哪个','是','数','据','随','便','加') 
yun2 = yun + yun1 #连接元组
print(yun2)

gou[3] = 7 #元组不能修改，但是列表里的元素可以被修改
print(gou)


#print('5 > 4')
print(5 > 4)
print(5 < 4)
print(5 == 4) #等于
print(5 != 4) #不等于
#以上4个是比较运算符，以下3个是逻辑运算符
print(True and False) #真真为真，真假为假，假假为假
print(True or False) #其中一个为真即为真
print(not True) 

#类型转换
print(int(True))
print(float(False))
print(str(False))

#类型转换里的查看类型
print(type(str(True)))

print()
print()
print()






