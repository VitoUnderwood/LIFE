# 错误集锦

## 人为的失误

```py
Line 517: Char 69: runtime error: applying non-zero offset 18446744073709551615 to null pointer (basic_string.h)
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior /usr/bin/../lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/basic_string.h:527:69
```

有可能是控制台输入格式错误

## 思维逻辑错误

- 超时：死循环忘记break或者是忘记修改条件变量
- 过多的if嵌套
- 忘记考虑特殊情况

## 常用c++结构

### 队列

```c
queue<TreeNode *> que;
que.emplace(root);
que.size();
que.front();
que.pop();x
```
