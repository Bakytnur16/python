# python
1. 大小写敏
2. 注释 
> 单行：#注释  
> 多行：'''注释''' 或者""" """

r = raw string，会自动将反斜杠转义

\n 换行new line character 
\t tab 制表符  
\\ 反斜杠（\） 
\' 单引号（'） 
\" 双引号（"） 
\f ASCII 进纸符（FF） 
\n ASCII 换行符（LF） 
\t ASCII 水平制表符（TAB） 
```
print('r\n') # 打印 \n
print('\n') #打印空行
raw_input()
```
3. 多行语句用\
4. Python 可以在同一行中使用多条语句，语句之间使用分号 ;
```
isinstance 函数判断变量的类型
>>> x = 'abc'
>>> y = 123
>>> isinstance(x, str)
True
>>> isinstance(y, str)
False
```
#### print
```

name = 'bob'
a = 'my name is {}'
x = "My name is "
y = "{} {}"
print('my name is {}'.format(name))
print('my name is bob')
print(f'my name is {name}')
print('my name is ', name)
print(a.format(name))
print(x + name)
print(y.format(x,name))

print("""
dfdfjd
fjdifjdifjifj
dfeifjeifj
""")
```
```
map的用法：map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x * x

a = [1,2,3,4,5,6,7,8,9,10]

z = map(f, a)
print(list(z))
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = list(map(str,[1,2,3,4,5,6,7,8,9]))
print(x)
['1', '2', '3', '4', '5', '6', '7', '8', '9']


reduce把一个函数作用在一个序列[x1, x2, x3, …]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce
def add(x, y):
    return x + y

x = reduce(add, [1,9,5,7,9])
print(x)
31

from functools import reduce
def add(x, y):
    return x * 10 + y

x = reduce(add, [1,9,5,7,9])
print(x)
19579

a = ['adam', 'LISA', 'barT']

def UpperW(x):
    x = x[0].upper()+x[1:].lower()
    return x

L2 = list(map(UpperW, a))
print(L2)

from functools import reduce
L = [3, 5, 7, 9]
def prod(L):
    for i in L:
        return reduce(lambda x,y : x * y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

from functools import reduce
def str2float(s):
    def fn(x,y):
        return x*10 + y
    n=s.index('.')
    s1=list(map(int,[x for x in s[:n]]))
    s2 = list(map(int, [x for x in s[n+1:]]))
    return reduce(fn,s1)+reduce(fn,s2)/10**len(s2)
print('str2float(\'123.456\') =', str2float('123.456'))

filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 ==0
print(list(filter(is_odd, [1,2,4,5,6,9,10,15])))
[2, 4, 6, 10]

def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))


def is_palindrome(n):
    if len(str(n)) >1:
        if str(n) == str(n)[::-1]: #字符串颠倒
            return n
output = filter(is_palindrome, range(1, 1000))
print(list(output))

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))
```
## Python3 中有六个标准的数据类型：
None表示空值，它是一个特殊 Python 对象, None的类型是NoneType
### Number（数字）:整数、布尔型、浮点数和复数  
> int (整数), 如 1, 只有一种整数类型 int，表示为长整型。  
> bool (布尔), 如 True. :True 和 False 是 Python 的关键字，用来表示真和假的概念。如果加了引号，它们
就变成了字符串，也就无法实现它们本来的功能了 
> float (浮点数), 如 1.23、3E-2  
> complex (复数), 如 1 + 2j、 1.1 + 2.2j

### String（字符串) *变量[头下标:尾下标:步长]：*  
0 1 2 3 4  
-5 -4 -3 -2 -1  
len(str) 字符串长度
string[0] 字符串索引为0的字母
```
sentence = '我喜欢睡觉。'
a = list(sentence)
b = tuple(sentence)
print(a,b)
['我', '喜', '欢', '睡', '觉', '。'] ('我', '喜', '欢', '睡', '觉', '。')
```
> string: 使用三引号(''' 或 """)可以指定一个多行字符串。  
```
str='1234567890'
print(str[1:7:2]) #打印第二个到第七个之前的每隔一个字符的字符
print(str[:]) #打印所有
``` 
```
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

isalpha() 只包含字母，非空
isalnum() 只包含字母和数字，非空
isdecimal 只包含数字字符，非空
isspace() 只包含空格，制表符和换行，非空
startswith(开始)和 endswith(结束)方法返回 True
join（） ', '.join(['cats', 'rats', 'bats'])
print(' '.join(['my', 'name','is', 'bob'])) 
'My name is Simon'.split()
print(" my name is simon.".split()) # ['my', 'name', 'is', 'simon.']
spam.split('\n')

'Hello'.rjust(10) 向右移
'Hello'.rjust(10) 向左移
'Hello'.center(20） 
'Hello'.center(20, '=')
'Hello'.center(20, '=') 中间
删除 空白的字符串： strip(删除左右两边)、rstrip()和 lstrip()
```
import pyperclip
pyperclip.copy('Hello world!')
pyperclip.paste()
'Hello world!'
```
用 pyperclip 模块拷贝粘贴字符串

```
### List（列表）: *变量[头下标:尾下标]*   
```
list1 = ['absc', 890, 2.23, 'bei']
print(list1[0])

多重赋值： size,color,weight,height = list1 #但是变量的数目和列表的长度必须严格相等
list1[2] = 2001 #更改
list[:] 列表里所有的值
print(squares[-3:]) 输出末尾三个元素
len(list)列表长度
 for i in range(len(list)):
查找：
list.index('book') #返回第一个值为book的元素的*索引*
list.count('b')  在列表中出现的次数
添加：
list.append('Baidu') #元素添加到列表尾
list.insert(序列, obj) 指定位置插入一个元素，原本的元素向后移
删除：
del list[2] del 语句将删除列表中下标处的值
list.remove('book')删除列表中值为 x 的第一个元素
排序：
list.reverse()倒排
list.sort( key=None, reverse=False)排序  #错误：spam = spam.sort()，sort()方法当场对列表排序
使用“ASCII 字符顺序”
sorted() 要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数
spam.sort(key=str.lower) 将列表中所有的表项当成小写

嵌套：
[['a', 'b', 'c'], [1, 2, 3]]
list(seq)

list.extend(seq) 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
list.pop([index=-1])指定位置移除元素 没有指定索引，a.pop()返回最后一个元素
list.clear()移除所有项，非空

复制：
spam =[0,1, 2, 3, 4]
cheese = spam #赋值，传对象的*引用*
cheese[1] = 'hello'
print(spam, cheese)
#打印出来的spam也会更新为hello，因为它和cheese相等

list.copy() 浅复制

import copy
spam =[0,1, 2, 3, 4] 
cheese = copy.copy(spam)
cheese[1] = 42
print(spam, cheese)
#打印出来：[0, 1, 2, 3, 4] [0, 42, 2, 3, 4]

浅复制和深复制
 a = [1,2,3,4,['a','b']]
 c = copy.copy(a)
 d = copy.deepcopy(a)
 a.append(5)
>>> a[4].append('c')
c= [1, 2, 3, 4, ['a', 'b', 'c']]
>>> print 'd=',d
d= [1, 2, 3, 4, ['a', 'b']]
copy.copy对于可变类型，会进行浅拷贝
copy.copy对于不可变类型，不会拷贝，仅仅是指向
```  

### Tuple（元组） 元素不可修改  
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tup2 = (20,) # 一个元素，需要在元素后添加逗号  
元组也可以使用+操作符进行拼接。  
```
tuple[0]
tuple[1:3]
len(tuple)
元组的值*不能*被修改、添加或删除

>>> type(('hello',))
<class 'tuple'> #加逗号是元组
>>> type(('hello'))
<class 'str'> # 不加是字符串

list = ['我', '喜', '欢', '睡', '觉','觉',, '。']
print(tuple(list))
('我', '喜', '欢', '睡', '觉', '觉', '。')

```
### Set（集合）
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

### Dictionary（字典）  
list是有序的对象集合  
dictionary是无序的对象集合。  
dic.values(), dic.keys(), dic.items()
字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。键(key)是唯一的  
镶嵌字典： 
```
all = {'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}}

def total(man, item):
    numB = 0
    for k, v in man.items():
        numB = numB + v.get(item, 0)
    return numB
print(total(all,'pretzels'))
```
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
    
radiansdict.get(key, default=None) : 要取得其值的键，以及如果该键不存在时，返回的备用值。
radiansdict.setdefault(key, default=None) : 你常常需要为字典中某个键设置一个默认值，当该键没有任何值时使用

spam = {'color': 'red', 'age': 42}
a = input()
if a not in spam:
    spam[a] = 'black' 默认值
print(spam)

get() ??
setdefault() ??

str(dict)
type(variable)
radiansdict.clear()
radiansdict.copy()
radiansdict.fromkeys()
radiansdict.get(key, default=None)
key in dict
radiansdict.update(dict2)
pop(key[,default])
popitem()
```
```
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v)+' '+k)
        item_total += v
    print("Total number of items: " + str(item_total))
displayInventory(stuff)
```
> 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；# TypeError
> 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

consequence:
```
n = (20,'str','bob') #tuple  
b = [20,'str','bob'] #list  
s = {20,'str','bob'} #set  
a = {'name': 'bob','age':20,'type':'str'} #dic  
```  

### 算术计算符
运算优先级：pemdas 括号（Parentheses）、指数（Exponents）、乘（Multiplication）、除（Division）、加（Addition）、减（Subtraction）
变量 variable
% 返回除法的余数
// - 向下取接近商的整数
** 指数（最高优先级）

=的作用是将右边的值赋给左边的变量名。==的作用是检查左右两边的值是否相等

### 位运算符
& | ^ ~  << >>

#### 逻辑:and 与 ，or： 或， not：非

### 成员运算符
in /  not in

### 身份运算符
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

### 关键字

and 逻辑 与
assert 确保某东西为真 assert False, "Error!"
as with-as 语句  with X as Y: pass
exec 字符串作为 Python 脚本运行 exec 'print("hello")'
global 全局变量 global X
is 类似于==，判断是否一样
lambda 匿名函数
not 逻辑 非
or 逻辑 或
return 返回值并退出函数
with 将表达式作为一个变量，然后执行代码块
yield 暂停函数，返回到调用函数的代码中

@ 修饰器符 @classmethod


旧版：
%d 十进制整数
%f 浮点实数
%s 字符串格式


## 函数
#### 数学函数：
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
4.  break跳出循环，continue回到开始处，重新对循环条件求值

使用几个if的作用是：不管前面的语句是否通过，下面的if都会被测试，比如：
if我点了汉堡：加汉堡
if我加芝士：加芝士
if加番茄：加番茄
条件语句都会被执行
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
sum = 0
for a in range(0, 101):
    sum += a
print(sum)
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
for ...in ... Iteration
n = (20,'str','bob') #tuple
for x in n:
    if (x == 'bob'):
        print('找到了')
        break
    print('一个一个找吧', x)
else:
    print('不用在找了，没有')
    
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C
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
```
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit og type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = []

for i in range(0,6):
    print(f"adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was:{i}")
```
```
element =[]
ele = []
for i in range(0, 11):
    if i % 2 == 0:
        print(f"{i} is even")
        element.append(i)
    else:
        print(f"{i} == is odd")
        ele.append(i)
print(ele, element)
```
```
i = 0
numbers = []
while i <= 10:
    print(f"加入{i}")
    numbers.append(i)
    i += 1
print(numbers)
```
```
total = 0
for i in range(101):
    total += i
print(total)

for i in range(5, -1, -1):
    print(i, end=',') #5,4,3,2,1,0,
```
#### continue
```
while True:
    print('Whoe are you ?')
    name = input()
    if name != 'Joe':
        continue #除非等于Joe 不然循环；如果程序执行遇到 continue语句，就会马上跳回到循环开始处，重新对循环条件求值
    print('Hello,Joe.What is the passwordd?(It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
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
生成器就是一个迭代器,把一个列表生成式的[]改成()，就创建了一个generator
定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
```
>>> L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>
```

#### 匿名函数
```
a = [x * x for x in range(11) if x % 2 == 0]
print(a)

b = [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']
```

## 函数
一个* 元组或者列表，两个*字典
如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
```
def person(name, age, *, city, job): #city='Beijing'设置默认值
*后面的参数被视为命名关键字参数。
    print(name, age, city, job)
```
```
def spam():
    print(eggs)
eggs = 42 # 全局变量
spam()
print(eggs)

def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101 # 局部变量
    eggs = 0
spam()
```
函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
函数体内部可以用return随时返回函数结果；
```
def add(number):
    tom  = number * 3
    bob = number / 2
    jack = number - 10
    return tom,bob,jack

a = 60
x, y, z = add(a) #函数的特性：函数里的变量是临时的，所以前面用了jack，bob还是tom也好，后面添加的x， y， z变量不受影响。照样计算
print(f"{x} {y} {x}")
```
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

argv 即所谓的参数变量（argument variable）
argv 解包（unpack)
参数变量（argument variable）
导入（import）的特性称为模块：模块（module）

```
import random
for i in range(5):
    print(random.randint(1, 10), end=', ')
```
```
cmd<< python 12.py Zio #take argument
from sys import argv
#python test.py zed
main, user_name = argv
prompt = '> '

print(f"Hi {user_name}m I'm the {main} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer.Nice.
""")
```
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
close：关闭文件。跟你的编辑器中的“文件”→“保存”是一个意思。
read：读取文件的内容。你可以把结果赋给一个变量。
readline：只读取文本文件中的一行。
truncate：清空文件，请小心使用该命令。
write('stuff')：将“stuff”写入文件。
seek(0)：将读写位置移动到文件开头。

最重要的一个是+修饰符，你可以用它来实现'w+'、'r+'和'a+'。这样可以把文件用同时读写的方法打开
r - 只读
rb - 二进制只读
rb+ 文件指针在文件开头
w - 写入
a - 追加 append

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

```
from sys import argv

script, filename = argv

txt = open(filename)
# txt = open(filename)返回的是“文件对象”（file object）
print(f"Here's your file {filename}:")
print(txt.read())
print("Type the filename again: ")
file_again = input('> ')

txt_again = open(file_again)

print(txt_again.read())
```

```
from sys import argv
script, filename = argv
print(f"we are opend{filename}")
target = open(filename, 'w') #定位文件对象
target.truncate() #清除所有内容
print("please enter yout text")
text = (input('enter text')) #写下要输进文件内容
target.write(text) #把内容写进文件里
target.close() #关闭保存

again_filename = input('enter the file name')
a = open(again_filename) #定义文件对象
print(a.read()) #读取内容
```
```
from sys import argv

script, from_file, to_file = argv

in_file = open(from_file) #文件对象
data = in_file.read() # 读取文件内容
out_file = open(to_file, 'w') #文件对象，可写
out_file.write(data) #内容写入第二个文件
print('down')

in_file.close()
out_file.close()
```

#### pickle 模快
python的pickle模块实现了基本的数据序列和反序列化。

#### os 模块
os 模块提供了非常丰富的方法用来处理文件和目录
exists验证对象是否存在
```
# from os.path import exists
# print(f"Does the output file exist? {exists(to_file)}")
```

### 错误和异常
SyntaxError（语法错误）
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
组合（composition）：指一个类可以将别的类作为它的部件构建起来，有点儿像车子和车轮的关系。
属性（attribute）：类的一个属性，它来自于组合，而且通常是一个变量。
self：在类的函数中，self 指代被访问的对象或者实例的一个变量。
是什么（is-a）：用来描述继承关系
有什么（has-a）：用来描述某个东西是由另外一些东西组成的，或者某个东西有某个特征

- class X(Y)：创建一个叫 X 的类，它是 Y 的一种 
- 
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

#### 继承 inheritance
子类（派生类 DerivedClassName）会继承父类（基类 BaseClassName）的属性和方法。
class DerivedClassName(modname.BaseClassName):
*单继承*
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
*多继承*
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
```
def area(a,b,c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
a = float(input('输入三角形第一边长: '))
b = float(input('输入三角形第二边长: '))
c = float(input('输入三角形第三边长: '))
print('三角形的面积是 ',area(a,b,c))
```
```
class robot(object):
    def __init__(self,sound):
        self.s = sound
    def sounds(self):
        print(self.s)

song_bird = robot("jijijijis")
song_cat = robot("miaomiaomaio")

song_bird.sounds()
```
## 正则表达式
re 模块使 Python 语言拥有全部的正则表达式功能。
re.match(pattern, string, flags=0)
```
import re
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
```
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。

re.search(pattern, string, flags=0)
re.sub
re.findall
re.finditer
re.RegexObject
re.compile() 返回 RegexObject 对象。
re.MatchObject
group() 返回被 RE 匹配的字符串。


## CGI
CGI(Common Gateway Interface),通用网关接口,它是一段程序,运行在服务器上如：HTTP服务器，提供同客户端HTML页面的接口。

### 数据库

## 网络编程
Python 提供了两个级别访问的网络服务。：
低级别的网络服务支持基本的 Socket，它提供了标准的 BSD Sockets API，可以访问底层操作系统Socket接口的全部方法。
高级别的网络服务模块 SocketServer， 它提供了服务器中心类，可以简化网络服务器的开发。

Socket又称"套接字"，应用程序通常通过"套接字"向网络发出请求或者应答网络请求，使主机间或者一台计算机上的进程间可以通讯。

## 多线程
## xml解析
## python Json 数据解析
## urllib
Python urllib 库用于操作网页 URL，并对网页的内容进行抓取处理。

DBES——“decode bytes, encode strings”
```
def print_two(*args): #*args 把函数的所有参数都接收进来
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1): #接受了一个参数
    print(f"arg1: {arg1}")

def print_none(): #不接受任何参数
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("Frist!")
print_none()
```
函数的 return 会给调用该函数的代码行一个结果。思路是这样的：函数通过参数接受输
入，通过 return 返回输出。print 和它毫无关系，它只是在终端打印输出而已。

exit(0)可以中止某个程序

flow chart流程图

自顶向下 自底向上

覆盖 
super
super(Child, self).altered()
super()最常见的用法是在基类的__init__函数中使用。 


SciPy:科学，数字  
PyGame：游戏  
Pandas：做数据操作和分析  
Natural Language Tool Kit：用来分析文本，以及实现垃圾邮件过滤和自动聊天机器人这样的软件  
TensorFlow：机器学习和可视化  
Requests：HTTP用户端以及Web知识  
ScraPy：爬取网站内容  
Kivy：创建桌面和移动平台的用户界面  
