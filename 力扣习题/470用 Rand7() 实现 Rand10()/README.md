# 题目

## 用 Rand7() 实现 Rand10()

### 来源:

[力扣-用 Rand7() 实现 Rand10()](https://leetcode-cn.com/problems/implement-rand10-using-rand7/)

### 题目内容

已有方法 `rand7` 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 `rand10` 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 `Math.random()` 方法。



**示例 1:**

    
    
    **输入:** 1
    **输出:** [7]
    

**示例 2:**

    
    
    **输入:** 2
    **输出:** [8,4]
    

**示例 3:**

    
    
    **输入:** 3
    **输出:** [8,1,10]
    



**提示:**

  1. `rand7` 已定义。
  2. 传入参数: `n` 表示 `rand10` 的调用次数。



**进阶:**

  1. `rand7()`调用次数的 [期望值](https://en.wikipedia.org/wiki/Expected_value) 是多少 ?
  2. 你能否尽量少调用 `rand7()` ?

