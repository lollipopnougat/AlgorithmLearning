# 题目

## 有时间限制的 Promise 对象

### 来源:

[力扣-有时间限制的 Promise 对象](https://leetcode.cn/problems/promise-time-limit/)

### 题目内容

请你编写一个函数，它接收一个异步函数 `fn` 和一个以毫秒为单位的时间 `t`。它应根据限时函数返回一个有 **限时** 效果的函数。

限时函数是与原函数相同的函数，除非它需要 `t` 毫秒以上的时间来完成。如果出现了这种情况，请你返回 `"Time Limit Exceeded"`
拒绝这次函数的调用。注意，它应该返回一个字符串拒绝，而不是一个 `Error` 。



**示例 1：**

    
    
    **输入：**
    fn = async (n) => { 
      await new Promise(res => setTimeout(res, 100)); 
      return n * n; 
    }
    inputs = [5]
    t = 50
    **输出：** {"rejected":"Time Limit Exceeded","time":50}
    **解释：** 提供的函数设置在 100ms 后执行完成，但是设置的超时时间为 50ms，所以在 t=50ms 时拒绝因为达到了超时时间。
    

**示例 2：**

    
    
    **输入：**
    fn = async (n) => { 
      await new Promise(res => setTimeout(res, 100)); 
      return n * n; 
    }
    inputs = [5]
    t = 150
    **输出：** {"resolved":25,"time":100}
    **解释：**
    在 t=100ms 时执行 5*5=25 ，没有达到超时时间。
    

**示例 3：**

    
    
    **输入：**
    fn = async (a, b) => { 
      await new Promise(res => setTimeout(res, 120)); 
      return a + b; 
    }
    inputs = [5,10]
    t = 150
    **输出：** {"resolved":15,"time":120}
    **解释：** 在 t=120ms 时执行 5+10=15，没有达到超时时间。
    

**示例 4：**

    
    
    **输入：**
    fn = async () => { 
      throw "Error";
    }
    inputs = []
    t = 1000
    **输出：** {"rejected":"Error","time":0}
    **解释：**
    此函数始终丢出 Error



**提示：**

  * `0 <= inputs.length <= 10`
  * `0 <= t <= 1000`
  * `fn 返回一个 Promise 对象`

