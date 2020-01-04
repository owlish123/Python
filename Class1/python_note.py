# -*- coding: utf-8 -*-
"""
Created on Fri Jan 03 16:15:04 2020

@author: 86152
"""
##加速度的程序
#v0 = input('The starting velocity is:'    )
#v1 = input('The ending velocity is:'    )
#t = input('The time span is:'    )
#formula = (v1-v0)/t
#print 'The average velocity is: ', formula
##加速度程序的优化版本
#def acceleration(v0, v1, t):
#    return (v1-v0)/t
#v0 = float(input('Enter the v0:'))
#v1 = float(input('Enter the v1:'))
#t  = float(input('Enter the t:'))
#print ('The acceleration is %.2fm/s**2' %acceleration(v0, v1, t))
##最简单的版本！！！
#v0, v1, t = input('enter v0, v1, t:')
#print (v1-v0)/t
##ps:return 后面的内容需要顶格写；%f默认6位小数，%.3f则保留3位小数;
#
#

##飞机起飞的最短距离
#v = input('The speed is:')
#a = input('The acceleration is:')
#formula = v**2/(2*a)
#print ('The minium length to take off is: ', formula)
##飞机起飞最短距离的优化版本
#def minium_length(v, a):
#    return v**2/(2*a)
#v = input('please enter the v:')
#a = input('please enter the a:')
#print ('the minium_length to take off is: %.2f' % minium_length(v, a))
#
##ps:手写中的2a得表达成2*a;分母注意加括号；数据不转换成float也能运算出结果来
#
#
#
##计算BMI指数
#height = input('Enter your height in inches:')
#weight = input('Enter your weight in pounds:')
#formula = weight/height**2
#print ('Your BMI is: ') , formula
##计算BMI指数的优化版本
#def BMI(h, w):
#    return(w/h**2)
#h = input('please enter your height:')
#w = input('please enter your weight:')
#print ('Your MBI is: %.2f '% BMI(h, w))
#
#
##计算利息
#def income(basis, rate, year):
#    return basis*(1+rate/100)**year
#basis, rate, year = input('basis, rate, year:')
#print ('%.2f'%income(basis, rate, year))
##ps:简化版，只有公式，输入和输出；同时输入多个数据，用逗号隔开即可；'%.2f'%保留小数位数
#
#
##%d, %f, %s用法
#print ('the integer of 9.9 is: %d ' %9.9)
#print ('the float of 9 is: %f' %9)
#print ('my name is %s, and i am %s' % ('hujia', '24'))
#
#
##逻辑运算法则and, or, not
#print ('you love me' == 'i love you', 'you love me' != 'i love you ')
#print ('you love me' == 'i love you' and 'you love me' != 'i love you ')
#print ('you love me' == 'i love you' or'you love me' != 'i love you ')
##ps:and全为真才是真，or一个为真则真，那么not呢？
#
#
##求n次方；取绝对值；开二次方; 向上取整； 向下取整；
#print (pow(2, 3))
#print (abs(-9))
#print (sqrt(9))
#print (ceil(9.9))
#print (floor(9.9))
##输入math后并没有特殊值供选择？？
#
#
##同时输入多个信息
#a, b, c = input('please enter three numbers:')
#print a, b, c
##比如
#v0, v1, t = input('enter v0, v1, t:')
#print (v1-v0)/t
#
#
#print (not True, not False)
#
#
#tag = True
#
#if not tag:
#    print(tag)
#else:
#    print('')


#if条件为真，则if下的代码会被执行，如果为假，则不会被执行，而直接执行后面的代码*****
#if True:
#    print('you love me')
#print ('i love you')
#
#if False:
#    print('you do not love me')
#print('you do not love me')

#多重判断句elif，只会执行其中的一个***************************************
#w = int(input('enter your weight:' ))
#if w<=45:
#    print ('you are not heavy!')
#elif w>45 and w<50:
#    print ('perfect!')
#elif 50 <= w <= 55:
#    print ('good!')
#else:
#    print ('please cut weight!')

#if…else*******************************
#ans = raw_input('Do you miss me?' )
#if ans == 'yes':
#    print ('I miss you,too')
#else:
#    print ('白想你了！')

#if 嵌套************************************************执行顺序有问题
#ans1 = raw_input('寒假出来玩吗？')
#if ans1 == 'yes':
#    print ('我们一起玩！')
#    ans2 = raw_input('想去散步吗？')
#    if ans2 == 'yes':
#        print ('走，去乡下！')
#    else:
#        print ('走，城里high!')
#else:
#    print ('打扰了！')

#三目运算符 IF成立执行的代码　if 条件 else 不成立执行的代码(值)***********
#a = 1
#b = 2
##if a > b:
##    c = a-b
##else:
##    c = b - a
#c = (a - b) if a > b else (b - a) # variable = val1 if statement else val2
#print c 

#从1加至100***********************************
#result = 0
#i = 1
#while i <= 100:
#    result += i
#    i += 1
#print result

#计算100以内偶数的和***************************
#result = 0
#i = 1
#while i <= 100:
#    if i % 2 == 0:
#        result = result + i
#    i = i + 1
#print result

#break的使用,小孩子数10以内的数，看能数到第几位*************
#i = 0
#while i <= 10:
#    if i == 7:
#        break
#    i += 1
#    print ('小孩能数到%d'%i)

#continue的使用************************
#i = 0
#while i <= 10:
#    if i == 7:
#        print ('小孩不能数%d'%i)
#        i += 1
#        continue
#    print ('小孩能数%d'%i)
#    i += 1

#range[  )**************************
#sum = 0
#for tmp in range(1, 10): # (start, end) i=start, i+=1, i<end 
#    print (tmp)
#    sum += tmp
#print (sum, 9*10/2)

#range 分别输出和装在列表里输出**********************
#for tmp in range(1, 10, 2): #(start, end, step_size)
#    print (tmp)
#
#container = range(1, 10, 2)
#print (container)

#字符串、列表和元组可以乘以倍数，集合不可以*********************
#print('I Love you! '*3)
#print([1, 2, 3] *3)
#print((1,2),(3, 4))*3

#九九乘法表**************************************其中几个代码是否多余？
#print ' '*36, 'Multiplication Table' #center也可以
##print ('\t\t')
#for i in range(1, 10):
#    print '\t%d'%i,
#print ''
#print '-'*100
#for i in range(1, 10):
#    print '%d |\t'%i,
#    for j in range(1, 10):
#        print'%d\t' % (i*j), 
#    print ''

#九九乘法表**********************************末尾的逗号为何如此重要？
#print ' '*40, 'Multiplication Table'
#for i in range(1,10):
#    print '\t%d'%i, #末尾有逗号就是横着展开，没有就竖着展开
#print '-'*105
#
#for i in range(1, 10):
#    print '%d|'%i,
#    for j in range(1, 10):
#        print '\t%d'%(i*j),

#函数求一个序列的和，先定义函数，再应用函数***********************
#def num(head, tail):
#    ans = 0
#    for i in range(head, tail+1):
#        ans += i
#    return ans
#print num(1, 10), num(20, 37), num(35, 49)

#shownone**********************************************什么用法？
#def showNone():
#    print ('Love you!')
#    print num(1, 99)
#
#print showNone()

#全局变量和局部变量*************************
#a = 1
#def func1():
#    print a
#func1() #全局变量
#
#def func2():
#    global a
#    b = 2
#    a = 2
#    print b, a
#func2() #局部变量
#
#print(a) #************经过了上面局部的改造，也成局部变量了？
#print(b)

#全局变量*******************
#ans = 0
#
#def func3():
#    global ans
#    ans += 99
#
#func3()
#print ans
#func3()
#print ans
#func3()
#print ans

#查找回文质数******************************************************************
#import math
#def zhishu(n):
#    if n < 4:
#        return True
#    if n % 2 == 0:
#        return False
#    for i in range(3, int(math.sqrt(n)+1), 2):
#        if n % i == 0:
#            return False
#    return True


#def testZhishu():
#    for i in range(1, 100):
#        if zhishu(i):
#            print(i)
#
#def huiwen(n):
#    container = [] # container = list()
#    while n:
#        container.append(n%10)
#        n /= 10
#    print (container)
#    length = len(container)
#    for i in range(length/2):
#        if container[i] != container[length-i-1]:
#            return False
#    return True
#
#def toHuiwen(n):
#    container = [] # container = list()
#    while n:
#        container.append(n%10)
#        n /= 10
#    ans = 0
#    basis = 1
#    for i in range(len(container)-1, -1, -1):
#        ans += container[i]*basis
#        basis *= 10
#    return ans
#
#def printHuiwen(n):
#    for i in range(1, n):
##        print (i, toHuiwen(i))
#        if zhishu(i) and zhishu(toHuiwen(i)):
#            print (i)
##printHuiwen(30)
#printHuiwen(1000)


#and, or*********************************************0和1的情况
#print (False and True)

# 位运算：&(and) |(or) ^ ~
#print (0 and 1)
#print (1 and 2)
#print (2 and 1)
#print (0 or 1)
#print (1 or 2)
#print (2 or 1)

#while循环***********************
#i = 0
#while i < 5:
#    print ('*****')
#    i += 1


#for temp in sequence:****************
#for i in 'I am not happy now':
#    if i == 'n':
#        continue
#    print(i)

#while……else; for……else********************
#i = 1
#while i <= 5:
#    print ('You need more practice!')
#    i += 1
#else:
#    print ('Have a rest!')

#单引号、双引号、三引号（支持换行输出）都可以***************
#print ('I am hujia')
#print ('I\'m hujia')
#print ("I'm hujia")
#print ('''I am hujia''')

#下标找到精确的数字,储存的序号是从0开始的*************
#name = 'hujia'
#print name
#print name[2]

#切片 sequence[start下标 : end下标 : step]步长为负数，则取倒序*************
#name = '123456'
#print name [2 : 5]
#print name [ : 3]
#print name [1 : ]
#print name [ : ]
#print name [0 : 3 : 2 ]
#print name [ : : -1 ]
#print name [-1 : -5 : -2]

#查找字符串的方法 find, index, count**********************
#a = 'Python is very fun, and I love python very much.'
#print a.find ('very')
#print a.find ('very', 15, 20)
#print a.index ('very')
#print a.index ('very', 15, 20)
#print a.count ('very')

#字符串修改replace, split, join（没看到这个函数）***************
#a = 'Python is very fun, and I love python very much.'
#print (a.replace ('and', 'but'))
#print (a.split('very', 1))
#b = ['Python', 'is', 'fun']

#大小写转换*****************************
#a = 'python is fun'
#print (a.capitalize()) #句子首字母
#print (a.title()) #每个单词首字母
#print (a.upper()) #全大写
#print (a.lower())

#删除空白字符lstrip(左侧空白), rstrip(右侧空白)，strip(两侧)******************
#a = '   Python is fun, and i love it very much. '  
#print (a.lstrip())
#print (a.rstrip())
#print (a.strip())

#字符串对齐(length, 填充物),ljust,rjust, 居中是center************************
#a = 'miss'
#print (a.ljust(8, '*'))
#print (a.rjust(5, '*'))
#print (a.center(12, '*'))

#判断字符串是否以某个子串开头或者结尾**********************
#a = 'you love python.'
#print (a.startswith('yo', 0, 10))
#print (a.endswith('pyth'))

#判断字符串是否是字母、数字、空白等等********************
#a = 'i love python 233333'
#print (a.isalpha())
#print (a.isalnum())
#print (a.isdigit())
#print (a.islower())
#print (a.isspace())
#print (a.istitle())
#print (a.isupper())

#列表中查找数据——下标,一次只能输入一个下标吗？ps:index, count***************
#list = ['A', 'B', 'C']
#print (list[0])
#print (list.count('A'))
#print (list.index('A'))

#判断是否在列表或字符串等中，in, not in***************
#list = ['apple', 'pear', 'banana']
#print ('dog' in list)
#print ('dog' not in list)
#
#追加数据append, 可以追加字符串和列表*********************
#list1 = ['apple', 'pear', 'banana']
#list.append('watermelon')
#print list
#list1.append(['watermelon'])# append(*)
#print list1
#list1.append('watermelon')
#print list1

#追加数据extend*******************************
#list1 = ['apple', 'pear', 'banana']
#list1.extend(['water', 'abs']) #拆开逐个增加
#print list1
#print (list1.extend(['watermelon', 'strawberry'])) #直接单个加入列表
#print list1

#插入数据insert********************
#list1 = ['apple', 'pear', 'banana']
#list1.insert(3, 'watermelon')
#print list1


#删除数据del,clear没有，有pop, remove**********************
#list1 = ['apple', 'pear', 'banana']
#del list1[1]
#print list1
#print list1.pop()
#print list1
#print (del(list1[0])) #没有del函数?
#print (list1.pop()) #默认删除最后一个
#print (list1.pop(1))
#print list1
#list1.remove('pear')
#print list1


#修改数据***********************
#list = ['apple', 'pear', 'banana']
#list[0] = 'watermelon'
#print list

#逆序*************************
#list1 = ['apple', 'pear', 'banana']
#list1.reverse()
#print list1 

#排序 sort()默认升序(sort(reverse = False))**************************
#list = [1, 2, 5, 4, 6]
#list.sort()
#print (list)
#list.sort(reverse = True)
#print (list)

#import copy************************deepcopy?
##复制数据copy, 不能复制吗？************
#a = ['apple', 'pear', 'banana']
#d = a
#print d
#d[0] = '-'
#print d
#print a
#
#print '\ncopy'
#b = copy.copy(a)
#c = copy.deepcopy(a)
#print b
#print c
#
#print 'Modify'
#b[0] = 'Yeah'
#c[0] = 'Oh'
#print a
#print b
#print c

#依次打印列表中的数据,while and for, but 'for' is more convenient***************
#a = ['apple', 'pear', 'watermelon']
#i = 0
#while i < len (a):
#    print (a[i])
#    i += 1

#for i in a:
#    print (i)

#列表嵌套*****************************
#a = [ ['apple', 'pear', 'watermelon'], ['a', 'b', 'c'], [1, 2, 3] ]
#print (a[1][2])

#将10个学生随机分给三个班级*******************************
#import random
#students = ['A', 'B', 'C', 'D', 'E', 'F', 'G',  'H', 'I', 'J']
#classes = [[], [], []]
#for name in students:
#    num = random.randint(0, 2)
#    classes[num].append(name)
#print classes
#for name in classes:
#    print (len (name), (name))

#单个数据的元组和多个数据的元组**********************
#a = (1, 2, 3)
#print (type(a))
#b = (1)#如果不加逗号，原来是什么数据类型就是什么类型
#print (type(b))
#c = (1,)
#print (type(c))

#在元组中查找数据***************************
#a = ('A', 'B', 3)
#print (a[0])
#print (a.count('A'))
#print (a.index(3))
#print (len(a))

#元组数据不支持修改，但元组里列表中的数据可以修改*****************
#a = ('A', 'B', [1, 2, 3])
#print (a[2][1])
#a[2][1] = 5
#print a

#创建字典***************************
#a = {'name' : 'hujia', 'age' : '24', 'gender' : 'female'}
#print (type(a))
#b = {}
#print (type(b))
#c = dict()
#print (type(c))

#字典新增，序列[key]:value,有则改，无则增; 清空列表***********************
#a = {'name' : 'hujia', 'age' : '24', 'gender' : 'female'}
#a ['name'] ='jiahu'
#print a
#
#a['hobby'] = 'nature'
#print a

#a.clear()
#print a

#在字典中新增********************************
#a = {'name' : 'hujia', 'age' : '24', 'gender' : 'female'}
#print (a.get('name'))
#print (a.get('names', 'age')) #只能查找出第一个，如果第一个不存在，才查找第二个
#print (a.keys()) #查找出字典中所有的key
#print (a.values()) #查找出key对应的值
#print (a.items()) #将键值对按元组的方式表达出来

#for key in a.keys():
#    print key
#for value in a.values():
#    print value
#for i in a.items():
#    print i

#for key, value in a.items():
#    print key, value  #用两个临时变量拆包

#集合set具有去重复的功能，没有顺序，没有下标**********************
#a = {'hujia'}
#print type(a)
#b = {1, 2, 2, 3}
#print b
#c = set ('hujia')
#print c
#d = set () #创建空集合
#print d

#在集合中增加数据 add, update**********************************
#a = {'hujia', 'love', 'a', 'dog'}
#a.add ('does') #add添加一个数据
#print a
#a.update ([1, 2, 3]) #update增加一个序列
#print a

#在集合中删除数据**********************************
#a = {1, 2, 3, 4, 5}
#a.remove(2)
#print a
#a.discard(3)
#print a
#a.pop()
#print a

#在集合中查找数据in ,not in***************************
#a = {10, 20, 50, 20}
#print 20 in a
#print 30 not in a
#print max(a)

#公共用法 ********************************
# +， *， in, not in, len, del, max, min, range(供for循环使用)， enumerate
#a = 'hujia'
#for i in enumerate(a, start = 5):
#    print i

#推导式 只适合列表，字典，集合********************************
#while的代码数多于for的，更多于列表推导式的
#i = 1
#list1 = []
#while i <= 10:
#    list1.append(i)
#    i += 1
#print list1

#list1 = []
#for i in range(1, 10):
#    list1.append(i)
#print list1

#list1 = [i for i in range(1, 10)]#左侧是返回值
#print list1

#list2 = [i for i in range(10) if i % 2 == 0] #for and if
#print list2

#list3 = [(i, j) for i in range(5) for j in range(5)]
#print list3

#dict1 = {i : i**2 for i in range(1, 10)}
#print dict1

#合并***************************************
#a = [1, 2, 3]
#b = [1, 4, 9]
#c = {a[i]:b[i] for i in range(len(a))} #将两个列表合并为一个集合，数据个数必须相等
#print c

#提取数据*****************************
#a = {'me' : 24, 'you' : 25}
#b = [key for key, value in a.items() if value > 24.5]
#print b


#函数先定义，再调用**************************
#def sentence():
#    print ('I miss you!') #只有这两行是不会打印的，因为目前只是定义而已
#sentence() #这步是调用函数，可以打印

#形式参数和实参******************************
#def name (i, j):
#    total = i + j
#    print total
#name (1, 2)

    
    























