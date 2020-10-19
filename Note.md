# 字典
## 由｛｝包围
## 由键-值组成，键-值之间使用“：”连接
## 键-值对之间使用“，”隔开
## 注意：字典中的键是唯一的，值可以不唯一
## 字典里查看值，通过键；列表里查看值，通过索引

```python
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
copy_score = score.copy()
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

