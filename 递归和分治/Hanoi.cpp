// 经典递归问题 汉诺塔(Hanoi)问题
#include <cstdlib>
#include <iostream>
using namespace std;

//  汉诺塔递归实现
void Hanoi(char a, char b, char c, int n)
{
    if (n == 1)
        cout << a << " --> " << c << endl;
    else {
        Hanoi(a, c, b, n - 1); //n层汉诺塔问题可分解为 n-1层汉诺塔(n-1个盘子从A移到B) + 
        Hanoi(a, b, c, 1); // 1 层汉诺塔 (剩下一个盘子从A移到C) +
        Hanoi(b, a, c, n - 1); // n-1层汉诺塔(B上n-1个盘子移到C上)
    }
}

int main(int argc, const char** argv)
{
    int n;
    cout << "一共有A B C三根柱，\n默认所有盘按大小放在A柱上，\n每次只能移动一个盘，\n小盘必须放在大盘上\n所有盘从A移到C上\n" << endl;
    cout << "输入汉诺塔层数: " << endl;
    cin >> n;
    cout << "所有步骤\n" << endl;
    Hanoi('A', 'B', 'C', n);
    system("pause");
    return 0;
}