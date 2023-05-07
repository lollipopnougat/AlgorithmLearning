# 题目

## 过滤数组中的元素

### 来源:

[力扣-过滤数组中的元素](https://leetcode.cn/problems/filter-elements-from-array/)

### 题目内容

请你编写一个函数，该函数接受一个整数数组参数 `arr` 和一个过滤函数 `fn`，并返回一个过滤后元素数量较少或元素数量相等的新数组。

返回的数组应该只包含通过过滤函数 `fn(arr[i]， i)` 计算后为真值的元素。

请你在不使用内置函数 `Array.filter` 的前提下解决该问题。



**示例 1：**

    
    
    **输入：** arr = [0,10,20,30], fn = function greaterThan10(n) { return n > 10; }
    **输出：** [20,30]
    **解释：**
    const newArray = filter(arr, fn); // [20, 30]
    过滤函数过滤掉不大于 10 的值

**示例 2：**

    
    
    **输入：** arr = [1,2,3], fn = function firstIndex(n, i) { return i === 0; }
    **输出：** [1]
    **解释：**
    过滤函数 fn 也可以接受每个元素的索引
    在这种情况下，过滤函数删除索引不为 0 的元素
    

**示例 3：**

    
    
    **输入：** arr = [-2,-1,0,1,2], fn = function plusOne(n) { return n + 1 }
    **输出：** [-2,0,1,2]
    **解释：**
    像 0 这样的假值应被过滤掉
    



**提示：**

  * `0 <= arr.length <= 1000`
  * `-109 <= arr[i] <= 109`

