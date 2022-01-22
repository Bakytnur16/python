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
list.append(obj)
list.count(obj)
list.extend(seq)
list.index(obj)
list.insert(index, obj)
list.pop([index=-1])
list.remove(obj)
list.reverse()
list.sort( key=None, reverse=False)
list.clear()
list.copy()

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
