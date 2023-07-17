test = '66'
print('你是真的厉害,{test}') # 这个方式实在python3.6版本之后才能使用该语法
# %s, 字符串占位符，
# %d，整数占位符，
# %f, 浮点数占位符，
# %.<number of digits>f 保留n位小数, 例如 %.2f 保留两位小数
# %x, 十六进制小写
# %X, 十六进制大写
# %o, 八进制数
# %e, 科学计数法，小写e
# %E, 科学计数法，大写E

print('笑死%s了，你是不是%d'%('我', 250))
print('一共赚了%e'%1000000)

# 类 类名：
class Myclass:
    def __init__(self):
        print(self) # self和类指向的同一个地址
        print('创建类的时候就会调用我')
    __i = 555 # 私有变量，类的外部访问不到
    # 类的私有方法，外部方法无法调用
    def __run(self):
        return '狗娜快跑'
    i = '12345'
    def play(self, name, age):
      self.name = name
      self.age = age
    # def study(self, )

class w:
    pass # 占位符，避免语法错误，保证程序运行
ren = Myclass()
print(ren)
# print(ren.play())
# print(ren.i)
# print(ren.name)