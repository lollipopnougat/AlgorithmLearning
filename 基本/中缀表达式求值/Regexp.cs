using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace RegexpTest1
{
    class Program
    {
        static void Main(string[] args)
        {
            string input;// = "1851 1999 1950 1905 2003";
            Regex rx = new Regex(@"(\d+\.?\d*)([+|-|*|/])(\d+\.?\d*)", RegexOptions.Compiled | RegexOptions.IgnoreCase);
            while (true)
            {
                input = Console.ReadLine();
                MatchCollection matches = rx.Matches(input);
                double num1;
                double num2;
                double res;
                char op;
                foreach (Match match in matches)
                {
                    GroupCollection groups = match.Groups;
                    if (match.Groups.Count < 4) throw new Exception("匹配失败");
                    num1 = Convert.ToDouble(match.Groups[1].Value);
                    op = Convert.ToChar(match.Groups[2].Value);
                    num2 = Convert.ToDouble(match.Groups[3].Value);
                    switch(op)
                    {
                        case '+': res = num1 + num2;break;
                        case '-': res = num1 - num2; break;
                        case '*': res = num1 * num2; break;
                        case '/': res = num1 / num2; break;
                        default: throw new Exception("未知错误");
                    }
                    Console.WriteLine($"结果是{res}");
                }
            }
            Console.ReadKey();
        }
    }
}
