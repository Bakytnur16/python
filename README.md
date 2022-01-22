# python
1. 大小写敏感
2. 注释
> 单行：#注释  
> 多行：'''注释''' 或者""" """

r = raw string，会自动将反斜杠转义
```
print('r\n') # 打印 \n
print('\n') #打印空行
```
3. 多行语句用\
4. Python 可以在同一行中使用多条语句，语句之间使用分号 ;

### Python3 中有六个标准的数据类型：
1. Number（数字）:整数、布尔型、浮点数和复数  
> int (整数), 如 1, 只有一种整数类型 int，表示为长整型。  
> bool (布尔), 如 True。  
> float (浮点数), 如 1.23、3E-2  
> complex (复数), 如 1 + 2j、 1.1 + 2.2j

2. String（字符串) *变量[头下标:尾下标:步长]：*  
0 1 2 3 4  
-5 -4 -3 -2 -1  
> string: 使用三引号(''' 或 """)可以指定一个多行字符串。  
```
str='1234567890'
print(str[1:7:2]) #打印第二个到第七个之前的每隔一个字符的字符
print(str[:]) #打印所有
```  
3. List（列表）: *变量[头下标:尾下标]*  
```
list = ['absc', 890, 2.23, 'bei']
print(list[0])
更改：
list[2] = 2001
更新增加：
list1.append('Baidu')
删除：
del list[2]
嵌套：
[['a', 'b', 'c'], [1, 2, 3]]
```  

4. Tuple（元组） 元素不可修改  
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tup2 = (20,) # 一个元素，需要在元素后添加逗号  
元组也可以使用+操作符进行拼接。  


5. Set（集合）
基本功能是进行成员关系测试和删除重复元素。
创建一个空集合必须用 set()  
```  
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}  
print(sites)   # 输出集合，重复的元素被自动去掉    
set可以进行集合运算 
创建一个空集合必须用 set()
a = set('abracadabra')  
b = set('alacazam')  
print(a - b)     # a 和 b 的差集  
添加：
s.add( x )
s.update( x )
移除：
s.remove( x )
s.discard( x )
s.pop()  随即删除
```  

6. Dictionary（字典）  
list是有序的对象集合  
dictionary是无序的对象集合。  
字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。键(key)是唯一的  
```
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值

tel = {'jack': 4098, 'sape': 4139}
# t = {x: x**2 for x in (2, 4, 5)}
tel['guido'] = 4127
for x, y in tel.items():
    print(x, y)
    
questions = ['name', 'age', 'gender', 'id']
answers = ['shuak', 18, 'female', '000111']
for x, y in zip(questions, answers):
    print(f'{x} : {y}')
```

> 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；  
> 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

consequence:
```
n = (20,'str','bob') #tuple  
b = [20,'str','bob'] #list  
s = {20,'str','bob'} #set  
a = {'name': 'bob','age':20,'type':'str'} #dic  
```  

#### 算术计算符
% 返回除法的余数
// - 向下取接近商的整数
** 指数（最高优先级）

#### 位运算符
& | ^ ~  << >>

#### 成员运算符
in /  not in

#### 身份运算符
is is not

is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
```
>>> b = a[:]
>>> b is a
False
>>> b == a
True
```

优先级顺序为 NOT、AND、OR

### 函数
#### 数学函数：
import cmath
abs
ceil
exp
fabs
floor
log
log10
max
min
modf
pow
round（x[,n]）
sqrt

随机：
choice
randrange
random
seed
shuffle
uniform

```
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
%s 格式化字符串
%d 格式化整数
%f 格式化浮点数字
 
 d = 'bob'
 print("my name is %s" %(d))
 print(f"my name is {d}") # 作用一样 f-string 
```


#### 字符串函数：
center(width,fillchar)
count(str, beg = 0, end=len(string))
endswith(suffix, beg=0, end=len(string))
isdigit()
isnumeric()
isspace()
join(seq)
len(string)
lstrip()
rfind(str, beg=0,end=len(string))
replace(old, new [, max])
rindex( str, beg=0, end=len(string))

#### 列表
len(list)
list(seq)
list.append(obj) 元素添加到列表尾
list.insert(序列, obj) 指定位置插入一个元素，原本的元素向后移
list.count(obj)  在列表中出现的次数
list.extend(seq) 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.index(obj)返回第一个值为 x 的元素的索引
list.pop([index=-1])指定位置移除元素 没有指定索引，a.pop()返回最后一个元素
list.remove(obj)删除列表中值为 x 的第一个元素
list.reverse()倒排
list.sort( key=None, reverse=False)排序
list.clear()移除所有项
list.copy() 浅复制

#### 字典 
str(dict)
type(variable)
radiansdict.clear()
radiansdict.copy()
radiansdict.fromkeys()
radiansdict.get(key, default=None)
key in dict
radiansdict.setdefault(key, default=None)
radiansdict.update(dict2)
pop(key[,default])
popitem()

#### 集合
copy()
difference()
discard()
intersection()
intersection_update()
isdisjoint()
issubset()
issuperset()
remove()
symmetric_difference()
symmetric_difference_update()	
union()

### 条件语句
1. 每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
2. 使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3.  在Python中没有switch – case语句。  

elif = else if

```
a = 1
while a <= 20:
#如果把a += 1 放在这，会计算到21为止，所以放最后
    if (a % 2 == 0):
        print(a, 'is even')
    else:
        print(a, 'is odd')
    a += 1 # 因为是循环，放在最后可以一直循环计算到20为止；没有这句会一直循环一
```

```
num = int(input("来输入个数字呗： "))
while num < 30:
    if (num % 2 == 0):
        if (num % 3 == 0):
            print(f'{num}能被2和3整除')
        else:
            print(f'{num}只能被2整除')
    elif (num % 3 == 0):
        if (num %2 == 0):
            print(f'{num}能被2和3整除')
        else:
            print(f'{num}只能被3整除')
    else:
        print(f'{num}哪里来的数字头疼')
    num += 1;
```
```
a = int(input('随便来个数字:'));
while a > 0:
    print(a, end=',');
    a -= 3;

```
```
a = int(input('计算从0到这个数的总和:'))
sum = 0
i = 1
while i <= a:
    sum += i
    i += 1
print(f'从0到{a}的和是：{sum}')
```

CTRL+C 来退出当前的无限循环
```
a = int(input('计算从0到这个数的奇数总和:'))
sum = 0
i = 1
while i <= a:
    sum += i
    i += 2
print(f'从0到{a}的和是：{sum}')
```

```
a = int(input('计算从0到这个数的偶数总和:'))
sum = 0
i = 0
while i <= a:
    sum += i
    i += 2
print(f'从0到{a}的和是：{sum}')
```
```
a = int(input('随便来个数字:'));
while a > 0:
    print(a, end=',');
    a -= 1;
else:
    print('负数不在取值范围内')
```
```
n = (20,'str','bob') #tuple
for x in n:
    if (x == 'bob'):
        print('找到了')
        break
    print('一个一个找吧', x)
else:
    print('不用在找了，没有')
```
```
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i,a[i], end=',')
```
```
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n,'等于',x,'*', n//x)
            break
    else:
        print(n,'是质数')
```

## 迭代器
可以记住遍历的位置的对象。
迭代器有两个基本的方法：iter() 和 next()。
```
it = iter(d)
for x in it:
    print(x,end=' ')
    
it = iter(d)
print(next(id))

创建迭代器的类： __iter__() 和 __next__()
StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况
it = iter(d)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
```

## 生成器
生成器就是一个迭代器

## 函数
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
```
def max(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input('输一个数字: '))
b = int(input('输一个数字: '))
print(max(a,b))
```
```
def printInfo(name, age):
    print(f'Hello {name}.Your age is {age}')
    return
a = str(input('请输入您的名字: '))
b = int(input('请输入您的年龄: '))
printInfo(a,b)
```
加了星号 * 的参数会以元组(tuple)的形式导入
加了两个星号 ** 的参数会以字典的形式导入
python 使用 lambda 来创建匿名函数。
sum = lambda arg1, arg2: arg1 + arg2
```
sum = lambda agr1, agr2: agr1 + agr2
print(sum(10, 20))
```
```
def Foo(x):
    if (x==1):
        return 1
    else:
        return x+Foo(x-1)

print(Foo(4))
等于10
```
```
a = [1,2,3]
# b = [2 * x for x in a]
# c = [x + y for x in a for y in b]
# print(c) #等于第一个元素分别乘以b的所有元素直到a的所有元素乘完
```
```
for i in reversed(range(0,11,2)):
    print(i, end=',')
else:
    print('负数不在范围内')

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f, end=',')
```

### 模块
import
from … import 
from modname import * 导入全部模块的内容
内置的函数 dir() 可以找到模块内定义的所有名称

#### 输入和输出
第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
str()： 函数返回一个用户易读的表达形式。
repr()： 产生一个解释器易读的表达形式。

open(filename, mode) mode 打开文件的模式：只读，写入，追加等。
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开模式
buffering: 设置缓冲
encoding: 一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

r - 只读
rb - 二进制只读
rb+ 文件指针在文件开头
w - 写入
a - 追加

f.read()
f.readlines()返回文件中包含的所有行
f.write()
f.tell()
f.seek()
f.close()
f.fileno()
f.isatty()
f.truncate
f.writelines()
f.flush()

#### pickle 模快
python的pickle模块实现了基本的数据序列和反序列化。

#### os 模块
os 模块提供了非常丰富的方法用来处理文件和目录

### 错误和异常
try/except
try: 执行代码
except: 发生异常时执行的代码
else：没有异常时执行的代码
finally: 有没有异常都会执行的代码
```
while True:
    try:
        x = int(input('请输入一个整数： '))
        break
    except ValueError:
        print('您输入的不是整数，请再次尝试')
```
抛出异常： raise
使用raise [Exception [, args [, traceback]]] 触发异常

### 面向对象：
```
class complex:
    def __init__(self,realpart, imagpart):
        self.r  = realpart
        self.i = imagpart
x = complex(3.0, -4.5)
print(x.r, x.i)
```
在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。
```
class people:
    name = ''
    age = 0
    __weight__ = 0
    def __init__(self, n ,a, w):
        self.name = n
        self.age = a
        self.__weight__ = w
    def speak(self):
        print('%s 说： 我今年 %d .' %(self.name,self.age))

p = people('shuak', 10, 20)
p.speak()
```

#### 继承
子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。
class DerivedClassName(modname.BaseClassName):
单继承
```
class people:
    name = ''
    age = 0
    __weight__ = 0
    def __init__(self, n ,a, w):
        self.name = n
        self.age = a
        self.__weight__ = w
    def speak(self):
        print('%s 说： 我今年 %d .' %(self.name,self.age))
class student(people):
    grade = ''
    def __init__(self, n, a, w, g): #调用父类的构函
        people.__init__(self,n, a ,w)
        self.grade = g
    def speak(self):
        print(f'{self.name}说： 我今年{self.age}岁了。我在读{self.grade}年级')

s= student('shuak', 10, 60,3)
s.speak()
```
多继承
```
class DerivedClassName(Base1, Base2, Base3):
class people:
    name = ''
    age = 0
    __weight__ = 0
    def __init__(self, n ,a, w):
        self.name = n
        self.age = a
        self.__weight__ = w
    def speak(self):
        print('%s 说： 我今年 %d .' %(self.name,self.age))
class student(people):
    grade = ''
    def __init__(self, n, a, w, g): #调用父类的构函
        people.__init__(self,n, a ,w)
        self.grade = g
    def speak(self):
        print(f'{self.name}说： 我今年{self.age}岁了。我在读{self.grade}年级')
class speaker():
    topic = ''
    name = ''
    def __init__(self, n, t):
        self.topic = t
        self.name = n
    def speak(self):
        print(f'我是一名演说家，我叫{self.name}, 我演讲的主题是{self.topic}')
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
s= sample('shuak', 25, 80,4, "python")
s.speak()
```
