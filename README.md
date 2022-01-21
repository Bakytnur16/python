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
