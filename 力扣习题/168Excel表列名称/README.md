# 题目

## Excel表列名称

### 来源:

[力扣-Excel表列名称](https://leetcode-cn.com/problems/excel-sheet-column-title/)

### 题目内容

给你一个整数 `columnNumber` ，返回它在 Excel 表中相对应的列名称。

例如：

    
    
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
    

**示例 1：**

    
    
    **输入：** columnNumber = 1
    **输出：** "A"
    

**示例 2：**

    
    
    **输入：** columnNumber = 28
    **输出：** "AB"
    

**示例 3：**

    
    
    **输入：** columnNumber = 701
    **输出：** "ZY"
    

**示例 4：**

    
    
    **输入：** columnNumber = 2147483647
    **输出：** "FXSHRXW"
    

**提示：**

  * `1 <= columnNumber <= 231 - 1`

