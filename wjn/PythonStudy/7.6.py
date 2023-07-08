
# 2种可以创建集合的方式：大括号或者set()函数
nora1 = { 
    "hello", "world", "hello", "hi", "hola"
} #集合：无序的不重复的元素序列
print(type(nora1)) #打印集合的数据类型

nora2 = "hello" 
print(nora2 in nora1) #判断nora2是否存在nora1中

A = set("123456")
B = set("5678910")
print(A)
print(B)

print(A - B) #集合A中包含的元素但是集合B中不包含
print(A | B) #集合A或B包含的所有的元素
print(A & B) #集合A和B都包含的元素
print(A ^ B) #集合A和B不同时包含的相同的元素


#在集合里添加一个元素
nora1.add('7')
print(nora1)

#
pigGouna = {
# key: value,
    'age': {
        'age1': 1,
        'age2': 2,
    },

}
print(pigGouna["age"])