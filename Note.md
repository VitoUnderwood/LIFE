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

### print函数的总结
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

### 导入import
```py
import math #导入整个模块，使用该模块内的函数方式为math.*
from math import pi,cos #导入math模块下pi、cos函数
from math import *  #导入模块下所有函数，慎用该方式
from math as tmath #给导入模块起一个别名
```



### printh函数的补充，赋值问题
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














