using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Calculator
{
    class Program
    {
        static void Main(string[] args)
        {

            Calculator ca = new Calculator();
            Console.WriteLine("命令行简单计算器 V1.0");
            Console.Title = "命令行简单计算器 V1.0";
            while (true)
            {
                Console.Write(">>");
                string input = Console.ReadLine();
                try
                {
                    ca.SetNew(input);
                    Console.WriteLine(ca.GetResult());
                }
                catch (Exception er)
                {
                    Console.WriteLine($"错误! {er.Message}");
                }
            }

        }
    }
    /*
     * 从中缀表达式转后缀

     * 如遇到操作数，直接输出到后缀的队列里。
     * 如果遇到操作符（包括括号），这里再定义一个存放操作符的栈，则:
        i.如果操作符是 ( ,入栈
        ii.如果操作符是 ) ,则把栈里的操作符依次出栈并插入到后缀序列后面，直到遇到一个 ( .
        iii.如果操作符不是 ( 和 ) ,则：
            (1). 如果操作符的优先级比栈顶运算符的优先级高，则入栈
            (2). 如果操作符优先级等于或小于栈顶运算符优先级，则将栈顶运算符出栈并插入到后缀序列后面，出栈后,再比较栈顶元素的优先级，
                重复iii，直到能把此操作符插入，将此操作符入栈。
     * 如果中序队列里的数据已经读取完毕，记录操作符的栈里，还有操作符的话，依次出栈插入到后缀序列的后面
    
    */

    public class Calculator
    {
        private string OrExpress; // 原始表达式
        private bool IsSet = false; // 类是否被设置(为表达式赋了值)

        public Calculator() { }

        public Calculator(string oe)
        {
            OrExpress = oe;
            IsSet = true;
        }

        public void SetNew(string oe)
        {
            ops.Clear();
            nums.Clear();
            OrExpress = oe;
            IsSet = true;
            GC.Collect(); // 强制回收垃圾 GC：C#的自动垃圾回收
        }
        //operator priority level 运算符优先级字典(键值对)
        private Dictionary<char, int> OpPLDictionary = new Dictionary<char, int>()
        {
            { '(', 1 },
            { '+', 2 },
            { '-', 2 },
            { '*', 3 },
            { '/', 3 },
            { ')', 4 }
        };

        private Stack<char> ops = new Stack<char>(); // 操作符 栈
        private Stack<double> nums = new Stack<double>(); // 数字栈

        private bool IsHigherThanTop(char op) 
        {
            if (ops.Count == 0) return true;
            else if (OpPLDictionary[op] > OpPLDictionary[ops.Peek()]) return true;
            else return false;
        }

        private void CalculateOne()
        {
            char tmpOp = ops.Pop();
            double rhs = nums.Pop();
            double lhs = nums.Pop();
            double tmpRes;
            switch (tmpOp)
            {
                case '+': tmpRes = lhs + rhs; break;
                case '-': tmpRes = lhs - rhs; break;
                case '*': tmpRes = lhs * rhs; break;
                case '/': tmpRes = lhs / rhs; break;
                default: throw new Exception("非法运算符");
            }
            nums.Push(tmpRes);
        }

        public double GetResult()
        {
            if (!IsSet) throw new Exception("未初始化表达式");
            IsSet = false;
            string tmpNum = "";
            int tmp;
            double tmpDouble;
            for (int i = 0; i < OrExpress.Length; i++)
            {
                if (int.TryParse(OrExpress[i].ToString(), out tmp) == true || OrExpress[i] == '.') // 字符是否是数字(能否安全转化为int型) 还有点的处理
                {
                    tmpNum += OrExpress[i];
                    if (i == OrExpress.Length - 1) // 如果最后是数字结尾的处理
                    {
                        if (double.TryParse(tmpNum, out tmpDouble) == false) throw new Exception("非法数字!");
                        nums.Push(tmpDouble);
                        tmpNum = "";
                    }
                }
                else //处理符号
                {
                    if (tmpNum != "") // 保存上一个数字
                    {
                        if (double.TryParse(tmpNum, out tmpDouble) == false) throw new Exception("非法数字!");
                        nums.Push(tmpDouble);
                        tmpNum = ""; 
                    }
                    if (OrExpress[i] == '(') ops.Push('('); 
                    else if (OrExpress[i] == ')')
                    {
                        while (ops.Peek() != '(') CalculateOne();
                        ops.Pop();
                    }
                    else if (IsHigherThanTop(OrExpress[i])) ops.Push(OrExpress[i]); // 其他运算符的处理
                    else
                    {
                        while (!IsHigherThanTop(OrExpress[i])) CalculateOne();
                        ops.Push(OrExpress[i]);
                    }
                }
            }
            while (ops.Count != 0) CalculateOne(); // 如果栈此时仍非空 继续计算
            return nums.Peek();
        }
    }
}
