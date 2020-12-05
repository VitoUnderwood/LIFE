# 字典
## 由｛｝包围
## 由键-值组成，键-值之间使用“：”连接
## 键-值对之间使用“，”隔开
## 注意：字典中的键是唯一的，值可以不唯一
## 字典里查看值，通过键；列表里查看值，通过索引

```py
#字典通过键来查找值，不可通过索引
score = {"Tom":90, "Bob":85}
print(score)
print(score["Tom"])
结果
{'Tom': 90, 'Bob': 85}
90
```

## dict() 函数
## 用于创建一个字典
## 可以把元祖或列表转化为字典
## 注意：需要成对才可转换

```python
#元祖转换字典
score1 = (["Bob",75],["Tom",99])
print(dict(score1))
#列表转换字典
score2 = [("Bob",78),("Tom",88)]
print(dict(score2))
结果
{'Bob': 75, 'Tom': 99}
{'Bob': 78, 'Tom': 88}

#字典增加元素
score = {'Bob': 66, 'Tom': 77}
score["Alice"] = 88
print(score)
#替换字典中元素（通过键来查找）
score["Bob"] = 100
print(score) 
结果
{'Bob': 66, 'Tom': 77, 'Alice': 88}
{'Bob': 100, 'Tom': 77, 'Alice': 88}
```

# 字典的基本操作
```python
score = {'Bob': 66, 'Tom': 77, 'Alice': 88}
#len():输出字典中键值对数量
print(len(score))
#输出字典中的值
print(score["Bob"])
#更改字典中的值
score["Alice"] = 100
print(score)
#del:删除字典中对应的键值对
del score["Bob"]
print(score)
#确认字典中是否包含值
if "Tom" in score:
    print(True)
else:
    print(False)
结果
3
66
{'Bob': 66, 'Tom': 77, 'Alice': 100}
{'Tom': 77, 'Alice': 100}
True
```


# 字典的方法
## clear()方法
```python
#clear方法
a = { }
b = a
a["key"] = "value"
print(a)
print(b) 
a = { }
print(a)
print(b) 

a1 = { }
b1 = a1
a1["Bob"] = "100"
print(a1)
print(b1) 
a1.clear()
print(a1)
print(b1) 
结果
{'key': 'value'}
{'key': 'value'}
{}
{'key': 'value'}
{'Bob': '100'}
{'Bob': '100'}
{}
{}
```
## copy()方法
### 浅拷贝：原字典会变；深拷贝：两个独立
### 一级目录：深拷贝，二级目录：浅拷贝
```python
#copy()方法，浅复制
score = {'Tom': 77, 'Alice': ["English",100]}
print(score)
#copy字典
copy_score = score.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
print(copy_score)
#修改copy后的字典值，原字典不受影响
copy_score["Tom"] = 88
print(score)
print(copy_score)
#copy后的新字典增加或删除时，对原字典有影响
copy_score["Bob"] = 60
print(score)
print(copy_score)
#删除
copy_score["Alice"].remove(100)
print(score)
print(copy_score)
del copy_score["Tom"]
print(score)
print(copy_score)
```
结果
```python
{'Tom': 77, 'Alice': ['English', 100]}
{'Tom': 77, 'Alice': ['English', 100]}
{'Tom': 77, 'Alice': ['English', 100]}
{'Tom': 88, 'Alice': ['English', 100]}
{'Tom': 77, 'Alice': ['English', 100]}
{'Tom': 88, 'Alice': ['English', 100], 'Bob': 60}
{'Tom': 77, 'Alice': ['English']}
{'Tom': 88, 'Alice': ['English'], 'Bob': 60}
{'Tom': 77, 'Alice': ['English']}
{'Alice': ['English'], 'Bob': 60}
```

#### deepcopy函数
深度复制，复制后的字典做任何操作，原字典都不会受到影响
注意：使用前需要import调用
```python
#字典中的deepcopy函数
from copy import deepcopy
d = {}
d["names"] = ["Bob","Tom"]
print(d)
#深复制
d1 = deepcopy(d)
print(d1)
#对深复制后的字典，进行任何操作，原字典都不会受到影响
d1["age"] = 12
print(d1)
print(d)
d1["names"].remove("Tom")
print(d1)
print(d)
```
结果
```python
{'names': ['Bob', 'Tom']}
{'names': ['Bob', 'Tom']}
{'names': ['Bob', 'Tom'], 'age': 12}
{'names': ['Bob', 'Tom']}
{'names': ['Bob'], 'age': 12}
{'names': ['Bob', 'Tom']}
```

#### get函数
获取字典项的方法，即使字典中不包含查询键，也不会报错
```python
d = {"name":"Bob"}
print(d)
print(d["name"])    #字典项中存在的键，可直接输出值
#print(d["age"])     #字典项中不存在的键，会报错，使用get函数
print(d.get("age","无此值"))    
```
结果
```python
{'name': 'Bob'}
Bob
无此值
```

#### key方法
将字典的键，以列表的形式返回
```python
scores = {
    "Tom":{
        "Chinese":80,"English":100},
    "Bob":{
        "Chinese":85,"English":95},
    "Alise":{
        "Chinese":77,"English":99},
}
print(scores.keys())
```
结果
```python
dict_keys(['Tom', 'Bob', 'Alise'])
```

#### pop方法
获取指定键的值，并删除该键
```python
scores = {"Chinese":80,"English":100}
score = scores.pop("English")
print(scores)
print(score)
```
结果
```python
{'Chinese': 80}
100
```
#### popitem方法
Python 字典 popitem() 方法返回并删除字典中的最后一对键和值。
如果字典已经为空，却调用了此方法，就报出 KeyError 异常
```python
scores = {"Chinese":80,"English":100,"Math":99}
scores.popitem()
print(scores)
```
结果
```python
{'Chinese': 80, 'English': 100}
```

####  setdefault方法
给字典设置一个值
```python
d = {}
d.setdefault("num",1)
print(d)
```
结果
```python
{'num': 1}
```

####  update方法
利用另一个字典更新现有字典
```python
scores = {"Chinese":80,"English":100}
Math_score = {"Math":99}
scores.update(Math_score)
print(scores)
History_score = {"History":88}
scores.update(History_score)
print(scores)
```
结果
```python
{'Chinese': 80, 'English': 100, 'Math': 99}
{'Chinese': 80, 'English': 100, 'Math': 99, 'History': 88}
```


#### - max()函数
返回给定参数的最大值
```py
print(max(88,99,100))
```
结果
```py
100
```
#### - min()函数
返回给定参数的最小值
```py
print(min(88,99,100))
```
结果
```py
88
```

#### print函数的总结
```py
name = "Tom"
age = 10
print(name, "age is", age)
#变量不能用+号连接，会报错
#print(name + "age is" + age)
```
结果
```py
Tom age is 10
```

#### 导入import
```py
import math #导入整个模块，使用该模块内的函数方式为math.*
from math import pi,cos #导入math模块下pi、cos函数
from math import *  #导入模块下所有函数，慎用该方式
from math as tmath #给导入模块起一个别名
```



#### printh函数的补充，赋值问题
```py
#同时给多个变量赋值
a,b,c = 1,2,3
print(a)
print(b)
print(c)
#同时给多个变量赋同一个值
x = y = z = 2
print(x)
print(y)
print(z)
#给一个变量赋多个值
values = 1,2,3
print(values)
#增量赋值
num = 5
print(num)
num += 1    #num = num + 1
print(num)
num *= 2    #num = num * 2
print(num)
name = "A"
name += "B" #name = name + "B"
print(name)
name *= 2   #name = name * 2
print(name)
```
结果
```py
1
2
3
2
2
2
(1, 2, 3)
5
6
12
AB
ABAB
```



#### 条件中的比较符号
```py
num1 = int(input("输入第一个数："))
num2 = int(input("输入第二个数："))
if num1 > num2 :
    print(num1, " > ", num2)
if num1 < num2 :
    print(num1, " < ", num2)
if num1 == num2 :
    print(num1, " = ", num2)
if num1 != num2 :
    print(num1, " != ", num2)
```
结果
```py
输入第一个数：1
输入第二个数：2
1  <  2
1  !=  2
```


#### if...elif...elif...else
```py
num = int(input("输入一个数："))
if num >= 10:
    print(num, " >=10 ")
elif num >= 5:
    print(" 5<= ", num, " <10 ")
elif num >= 1:
    print(" 1<= ", num, " <5 ")
else:
    print(num, " <=0 ")
```
结果
```py
输入一个数：0
0  <=0
```


#### 多条件
```py
#多条件测试
age = int(input("年龄："))
if age >= 18:
    grade = int(input("年级："))
    if grade >= 12:
        print("OK")
    else:
        print("不行！")
else:
    print("年龄不满18")
```
结果
```py
年龄：18
年级：11
不行！
```


#### and or not
##### and
```py
# and 所有条件都为真
age = int(input("年龄："))
grade = int(input("年级："))
if age >= 18 and grade >= 12:
    print("OK")
else:
    print("不行！")
```
结果
```py
年龄：18
年级：11
不行！
```
##### or
```py
# or 其中一个条件都为真
if age >= 18 or grade >= 12:
    print("OK")
else:
    print("不行！")
```
结果
```py
年龄：18
年级：11
不行！
OK
```
##### not
```py
# not
age = int(input("年龄："))
if not (age < 18):
    grade = int(input("年级："))
    if grade >= 12:
        print("OK")
    else:
        print("不行！")
else:
    print("年龄不满18")
```
结果
```py
年龄：18
年级：11
不行！
```


#### assert 断言
遇到错误会报错
```py
num = 20
assert num < 11
```
结果
```py
    assert num < 11
AssertionError
```

#### while循环
```py
#while 默认条件为真
name = ""
while not name:
    name = input("输入你的名字：")
print("hello %s" % name)
```
结果
```py
输入你的名字：紫星
hello 紫星
```

```py
# while 默认条件为真
# while 判断条件
# demo：计算1到10的和
n = 10
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1到 %d 的和为 %d" %(n, sum))
```
结果
```py
1到 10 的和为 55
```
##### 注意不要进入无线循环
```py
# while 无限循环
n = 1
while n == 1:
    m = int(input("输入一个数："))
    print("数字是%s" %m)
print("end")
```
```py
# while 无限循环
while True:
    m = int(input("输入一个数："))
    print("数字是%s" %m)
print("end") 
```
结果
```py
输入一个数：1
数字是1
输入一个数：11
数字是11
输入一个数：111
数字是111
输入一个数：111
数字是111
输入一个数：1111
数字是1111
输入一个数：
```
##### while与else
```py
n = 0
while n < 5:
    print(n,"小于5")
    n += 1
else:
    print(n,"不小于5")
```
结果
```py
0 小于5
1 小于5
2 小于5
3 小于5
4 小于5
5 不小于5
```
#### for循环
```py
for i in [1,2,3]:
    print(i)

a = {"A":1, "B":2, "C":3}
for x in a:
    print(x, " = ", a[x])
```
结果
```py
1
2
3
A  =  1
B  =  2
C  =  3
```
#### range()函数
range(x,y,z)
x：从x开始，默认为0，可不填
y：计数到b，但不包含b
z：技术间隔，默认为1，可不填
```py
# range函数
for a in range(3):
    print(a)
print("-------------")
for b in range(1,3):
    print(b)
print("-------------")
for c in range(1,10,3):
    print(c)
```
结果
```py
0
1
2
-------------
1
2
-------------
1
4
7
```
#### 并行迭代
```py
# 并行迭代
a = ["Tom", "Bob", "Bela", "Anne","Alice"]
b = [1,2,3,4]
for i  in range(len(b)):
    print(a[i],"的年龄是",b[i],"岁")
```
结果
```py
Tom 的年龄是 1 岁
Bob 的年龄是 2 岁
Bela 的年龄是 3 岁
Anne 的年龄是 4 岁
```
##### zip函数处理并行迭代
返回为一个元祖列表，个数与最短的列表一致
```py
# zip函数处理并行迭代
a = ["Tom", "Bob", "Bela", "Anne","Alice"]
b = [1,2,3,4]
for a,b  in zip(a,b):
    print(a,"的年龄是",b,"岁")
```
结果
```py
Tom 的年龄是 1 岁
Bob 的年龄是 2 岁
Bela 的年龄是 3 岁
Anne 的年龄是 4 岁
```
#### 按索引迭代
```py
a = ["Tom", "Bob", "Bela", "Anne","Alice"]
index = 0
for i in a:
    if "ob" in i :
        a[index] = "Alice"
    index += 1
print(a)
```
结果
```py
['Tom', 'Alice', 'Bela', 'Anne', 'Alice']
```
#### continue
结束本次循环，进入下一个循环
##### 案例一
```py
for i in range(3):
    print("-----")
    print("i = ", i)
    if i == 1:
        continue
    print("hello")
```
结果
```py
-----
i =  0
hello
-----
i =  1
-----
i =  2
hello
```
##### 案例二
```py
for letter in "python":
    if letter == "o":
        continue
    print("letter is:", letter)
```
结果
```py
letter is: p
letter is: y
letter is: t
letter is: h
letter is: n
```

#### break
结束/终止循环
##### 案例一
```py
for i in range(3):
    print("-----")
    print(" i= ",i)
    if i == 1:
        break
    print("hello")
```
结果
```py
-----
 i=  0
hello
-----
 i=  1
```
##### 案例二
```py
names = ["Tom", "Bob", "Bela", "Anne","Alice"]
for name in names:
    if name == "Bela":
        print("Bela byebye")
        break
    print("name is:",name)
else:
    print("no name")
print("Done")
```
结果
```py
name is: Tom
name is: Bob
Bela byebye
Done
```
##### 案例三
```py
for letter in "python":
    if  letter == "o":
        break
    print("The letter is:", letter)
```
结果
```py
The letter is: p
The letter is: r
The letter is: t
The letter is: h
```
##### 案例四
```py
n = 5
while n > 0:
    print("number is:", n)
    n -= 1
    if n == 2:
        break
print("byebye")
```
结果
```py
number is: 5
number is: 4
number is: 3
byebye
```

#### 嵌套与可变循环
循环嵌套不要太多，尽量控制在两层以内
##### 嵌套循环
```py
# 嵌套循环
n = 5
for n in range(5,7):
    for i in range(1,4):
        print(i,"x",n,"=",i*n)
    print("----------")
```
结果
```py
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
----------
1 x 6 = 6
2 x 6 = 12
3 x 6 = 18
----------
```
##### 可变嵌套循环
```py
# 打印星号（*）的个数，由用户输入
stars = int(input("星星个数："))
for i in range(stars):
    print("*",end="")   #end = ""  下一个print直接打印，不换行
```
结果
```py
星星个数：5
*****
```
##### 双重嵌套
```py
# 打印星号（*）的个数行数，由用户输入
lines = int(input("想要多少行："))
stars = int(input("星星个数："))
for line in range(lines):
    for star in range(stars):
        print("*",end="")
    print()
```
结果
```py
想要多少行：2
星星个数：3
***
***
```
##### 三重嵌套
```py
# 打印星号（*）的个数行数块数，由用户输入
blocks = int(input("想要几块："))
lines = int(input("想要多少行："))
stars = int(input("星星个数："))
for block in range(blocks):
    for line in range(lines):
        for star in range(stars):
            print("*",end="")
        print()
    print("--------")
```
结果
```py
想要几块：2
想要多少行：3
星星个数：4
****
****
****
--------
****
****
****
--------
```
#### 
```py

```
结果
```py

```
#### 
```py

```
结果
```py

```
#### 
```py

```
结果
```py

```






