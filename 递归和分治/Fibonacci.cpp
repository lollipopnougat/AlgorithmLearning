// All kinds of fibonacci Algorithms
// 经典递归问题 斐波那契数列 求第n项的值
#include <cstdlib>
#include <iostream>
#include <chrono>
using namespace std;

//  斐波那契数列的递归法实现 时间复杂度O(n^2)
long long FibRec(int t)
{ //FibonacciRecursion
    if (t == 1 || t == 2)
        return 1;
    else
        return FibRec(t - 1) + FibRec(t - 2);
}

//  斐波那契数列的非递归实现 时间复杂度O(n)
long long FibNo(int t)
{ //FibonacciNoRecursion
    if (t == 1 || t == 2)
        return 1;
    else {
        long long num1 = 1;
        long long num2 = 1;
        for (int i = 2; i < t - 1; i++) {
            num2 = num1 + num2;
            num1 = num2 - num1;
        }
        return num1 + num2;
    }
}

//  fibonaccimatrix
//  https://www.cnblogs.com/Tang-tangt/p/9207649.html
//  Created by shunagao on 15/8/31.
//  Copyright © 2015年 shunagao. All rights reserved.
//
class Matrix {
public:
    long n;
    long long** m;
    Matrix(int num)
    {
        m = new long long*[num];
        for (int i = 0; i < num; i++) {
            m[i] = new long long[num];
        }
        n = num;
        clear();
    }
    void clear()
    {
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                m[i][j] = 0;
            }
        }
    }
    void unit()
    {
        clear();
        for (int i = 0; i < n; ++i) {
            m[i][i] = 1;
        }
    }
    Matrix operator=(const Matrix mtx)
    {
        Matrix(mtx.n);
        for (int i = 0; i < mtx.n; ++i) {
            for (int j = 0; j < mtx.n; ++j) {
                m[i][j] = mtx.m[i][j];
            }
        }
        return *this;
    }
    Matrix operator*(const Matrix& mtx)
    {
        Matrix result(mtx.n);
        result.clear();
        for (int i = 0; i < mtx.n; ++i) {
            for (int j = 0; j < mtx.n; ++j) {
                for (int k = 0; k < mtx.n; ++k) {
                    result.m[i][j] += m[i][k] * mtx.m[k][j];
                }
            }
        }
        return result;
    }
};

//  斐波那契数列的矩阵乘法实现 时间复杂度O(log n)
long long FibMat(int t) //fibonacciMatrix
{
    unsigned int num = 2;
    Matrix first(num);
    first.m[0][0] = 1;
    first.m[0][1] = 1;
    first.m[1][0] = 1;
    first.m[1][1] = 0;
    Matrix result(num);
    result.unit();
    int n = t - 2;
    while (n) {
        if (n % 2) {
            result = result * first;
        }
        first = first * first;
        n = n / 2;
    }
    return result.m[0][0] + result.m[0][1];
}

int main(int argc, const char* argv[])
{
    cout << "输入一个大于0的整数: ";
    int num = 0;
    cin >> num;
    auto p1 = chrono::high_resolution_clock::now();
    cout << "递归运算结果: " << FibRec(num) << endl;
    auto p2 = chrono::high_resolution_clock::now();
    cout << "非递归运算结果: " << FibNo(num) << endl;
    auto p3 = chrono::high_resolution_clock::now();
    cout << "矩阵乘法运算结果: " << FibMat(num) << endl;
    auto p4 = chrono::high_resolution_clock::now();
    auto d1 = chrono::duration_cast<chrono::nanoseconds>(p2 - p1);
    auto d2 = chrono::duration_cast<chrono::nanoseconds>(p3 - p2);
    auto d3 = chrono::duration_cast<chrono::nanoseconds>(p4 - p3);
    cout << "递归运算耗时: " << d1.count() << " ns, " << endl
         << "非递归运算耗时: " << d2.count() << " ns, " << endl
         << "矩阵乘法运算耗时: " << d3.count() << " ns" << endl;
    system("pause");
    return 0;
}