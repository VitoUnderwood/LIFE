# 错误集锦

## 人为的失误

```py
Line 517: Char 69: runtime error: applying non-zero offset 18446744073709551615 to null pointer (basic_string.h)
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior /usr/bin/../lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/basic_string.h:527:69
```

有可能是控制台输入格式错误

```c

AddressSanitizer: heap-use-after-free on address
```

链表的末尾没有设置为nullptr

```c
Line 22: Char 19: runtime error: member access within null pointer of type 'TreeNode' (solution.cpp)
```

使用了空指针，提前进行判断

## 思维逻辑错误

- 超时：死循环忘记break或者是忘记修改条件变量
- 过多的if嵌套
- 忘记考虑特殊情况
- 尾部idx忘记size()-1

## 常用c++结构

### 队列

```c
queue<TreeNode *> que;
que.empty();
que.size();
que.front(); que.back();
que.pop();
que.push();
```

### 栈

```c
stack<string> words
top()
push()
pop()
size()
empty()
```

### 集合

```c
unordered_set<string> set
find() == end()
insert() 插入元素
erase() 删除元素
clear() 清空容器
empty() 判断容器是否为空
size() 返回容器的大小
count()　　　　　
```

### 哈希表

```c
unordered_map<string> hash

insert() 插入元素
erase() 删除元素
clear() 清空容器
empty() 判断容器是否为空
size() 返回容器的大小
find()
count()　　　　　
```

### 向量

```c
（1）a.assign(b.begin(), b.begin()+3); //b为向量，将b的0~2个元素构成的向量赋给a
（2）a.assign(4,2); //是a只含4个元素，且每个元素为2
（3）a.back(); //返回a的最后一个元素
（4）a.front(); //返回a的第一个元素
（5）a[i]; //返回a的第i个元素，当且仅当a[i]存在2013-12-07
（6）a.clear(); //清空a中的元素
（7）a.empty(); //判断a是否为空，空则返回ture,不空则返回false
（8）a.pop_back(); //删除a向量的最后一个元素
（9）a.erase(a.begin()+1,a.begin()+3); //删除a中第1个（从第0个算起）到第2个元素，也就是说删除的元素从a.begin()+1算起（包括它）一直到a.begin()+         3（不包括它）
（10）a.push_back(5); //在a的最后一个向量后插入一个元素，其值为5
（11）a.insert(a.begin()+1,5); //在a的第1个元素（从第0个算起）的位置插入数值5，如a为1,2,3,4，插入元素后为1,5,2,3,4
（12）a.insert(a.begin()+1,3,5); //在a的第1个元素（从第0个算起）的位置插入3个数，其值都为5
（13）a.insert(a.begin()+1,b+3,b+6); //b为数组，在a的第1个元素（从第0个算起）的位置插入b的第3个元素到第5个元素（不包括b+6），如b为1,2,3,4,5,9,8         ，插入元素后为1,4,5,9,2,3,4,5,9,8
（14）a.size(); //返回a中元素的个数；
（15）a.capacity(); //返回a在内存中总共可以容纳的元素个数
（16）a.resize(10); //将a的现有元素个数调至10个，多则删，少则补，其值随机
（17）a.resize(10,2); //将a的现有元素个数调至10个，多则删，少则补，其值为2
（18）a.reserve(100); //将a的容量（capacity）扩充至100，也就是说现在测试a.capacity();的时候返回值是100.这种操作只有在需要给a添加大量数据的时候才         显得有意义，因为这将避免内存多次容量扩充操作（当a的容量不足时电脑会自动扩容，当然这必然降低性能） 
（19）a.swap(b); //b为向量，将a中的元素和b中的元素进行整体性交换
（20）a==b; //b为向量，向量的比较操作还有!=,>=,<=,>,<
```

## 解题思路

分析问题， 是否子问题，动态规划，扩散问题，BFS，遍历所有情况，回溯问题

线性的，双指针，反方向，栈，队列

链表常用操作

- 快慢指针找中点，以及变形倒数k
  
层次遍历和BFS类似，只不过不存在换，所以不用visited记录，也不用记录每一层的数量，比较简单

回溯问题：把问题转化成为树的结构，遍历所有情况寻找正确的路径的过程，使用的是dfs的手法，可以添加剪枝的操作提升速度，在递归调用之前「做选择」
