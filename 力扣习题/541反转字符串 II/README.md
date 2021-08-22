# 题目

## 反转字符串 II

### 来源:

[力扣-反转字符串 II](https://leetcode-cn.com/problems/reverse-string-ii/)

### 题目内容

给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

### 示例 1：

```plaintext
输入：s = "abcdefg", k = 2
输出："bacdfeg"
```

### 示例 2：

```plaintext
输入：s = "abcd", k = 2
输出："bacd"
```

### 提示：

- `1 <= s.length <= 104`
- `s` 仅由小写英文组成
- `1 <= k <= 104`
