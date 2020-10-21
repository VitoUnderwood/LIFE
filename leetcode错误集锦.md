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

## 思维逻辑错误

- 超时：死循环忘记break或者是忘记修改条件变量
- 过多的if嵌套
- 忘记考虑特殊情况
- 尾部idx忘记size()-1

## 常用c++结构

### 队列

```c
queue<TreeNode *> que;
que.emplace(root);
que.size();
que.front();
que.pop();x
```

## 解题思路

分析问题， 是否子问题，动态规划，扩散问题，BFS，遍历所有情况，回溯问题

线性的，双指针，反方向，栈，队列

链表常用操作

- 快慢指针找中点，以及变形倒数k
