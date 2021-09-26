# 题目

## 重建二叉树

### 来源:

[力扣-重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)

### 题目内容

输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。

假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

**示例 1:**

![](./tree.jpg)

    
    
    **Input:** preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    **Output:** [3,9,20,null,null,15,7]
    

**示例 2:**

    
    
    **Input:** preorder = [-1], inorder = [-1]
    **Output:** [-1]
    

**限制：**

`0 <= 节点个数 <= 5000`

**注意** ：本题与主站 105 题重复：<https://leetcode-cn.com/problems/construct-binary-tree-
from-preorder-and-inorder-traversal/>

