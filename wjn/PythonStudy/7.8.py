# while循环
def nora2():
    
    n = list(range(0, 100, 5)) # 数据类型转换
    n1 = int(1.8) #整数数据类型转换只保留整数部分
    print(n)
    sum = 0
    counter = 1
    while counter <= 10:
        sum = sum + counter
        counter = 1 + counter
    else:
        print('dqq')
    print(sum)

#nora2()

# for循环
def nora1():
    list1 = range(0, 100, 5)
    # print((list1))
    sum = 0
    for y in list1:
        print(y)
        sum = sum + y
    #print(sum)

# nora1()


def nora3(x, y):
    print(x, y)
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return 'equal'


x = nora3(2, 3)
print(x)

listNum = [14, 10, 5, 32, 5, 2, 3, 7]
def nora4(list1):
    list2 = []
    list3 = []
    for q in list1:
        if q % 5 == 0:
            list2.append(q)
        else:
            list3.append(q)
    return {
        'list2':list2,
        'list3':list3
    }
T = nora4(listNum)
print(T['list2'].count(5)) # 统计5出现的次数
T['list2'].extend(T['list3']) #将T['list3']列表追加到T['list2']列表里
print(T['list2'])
print(T['list2'].index(14)) #index：索引
T['list2'].insert(5, 100) #在第5个索引插入一个值// insert(索引,值)
print(T['list2'])
T['list2'].pop(4) #删除指定索引值（默认删除最后一个值）
print(T['list2'])
T['list2'].remove(10) #移除指定元素第一个匹配值，remove(元素值)
print(T['list2'])
T['list2'].reverse() # 反转列表:[a,b,c]>> [c,b,a]
T['list2'].sort(reverse=True) # 列表排序 sort() 从小到大， sort(reverse=True)从大到小
print(T['list2'])
T['list2'].clear()
print(T['list2'])
listCopy = T['list2'].copy()
print(listCopy)
