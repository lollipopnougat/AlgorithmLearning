// -*- coding = utf-8 -*-
// 快速排序
// 基于分治策略的排序算法，平均时间复杂度 O(nlog n)
// 相当重要的算法哟

#include <chrono>
#include <cstdlib>
#include <iostream>
using namespace std;

void swap(int& lhs, int& rhs)
{
    int t = lhs;
    lhs = rhs;
    rhs = t;
}

//  基本
int partition(int nums[], int st, int ed)
{
    int i = st, j = ed; //最初基准来自第一个数
    while (i < j) {
        while (i < j && nums[i] <= nums[j]) {
            //cout << "比较 nums[" << i << "]=" << nums[i] << "小于等于nums[" << j << "]=" << nums[j] << endl;
            //cout << "右侧指针 j = " << j << " 即将-1 " << endl;
            j--;
        }

        if (i < j) {
            //cout << "交换nums[" << i << "]=" << nums[i] << "和nums[" << j << "]=" << nums[j] << endl;
            swap(nums[i], nums[j]);
            //cout << "左侧指针 i = " << i << " 即将+1 " << endl;
            i++;
        }
        while (i < j && nums[i] <= nums[j]) {
            //cout << "比较 nums[" << i << "]=" << nums[i] << "小于等于nums[" << j << "]=" << nums[j] << endl;
            //cout << "左侧指针 i = " << i << " 即将+1 " << endl;
            i++;
        }

        if (i < j) {
            //cout << "交换nums[" << i << "]=" << nums[i] << "和nums[" << j << "]=" << nums[j] << endl;
            swap(nums[i], nums[j]);
            //cout << "右侧指针 j = " << j << " 即将-1 " << endl;
            j--;
        }
    }
    //cout << "基准值 nums[" << i << "] = " << nums[i] << endl;
    return i;
}

/* 优化
int part(int s[],int l, int r)
{
    int i = l, j = r;
    int x = s[l]; //s[l]即s[i]就是第一个坑
    while (i < j)
    {
        // 从右向左找小于x的数来填s[i]
        while(i < j && s[j] >= x) 
            j--;  
        if(i < j) 
        {
            s[i] = s[j]; //将s[j]填到s[i]中，s[j]就形成了一个新的坑
            i++;
        }
        // 从左向右找大于或等于x的数来填s[j]
        while(i < j && s[i] < x)
            i++;  
        if(i < j) 
        {
            s[j] = s[i]; //将s[i]填到s[j]中，s[i]就形成了一个新的坑
            j--;
        }
    }
    //退出时，i等于j。将x填到这个坑中。
    s[i] = x;
    return i;
}
*/
//优化版
void QuickSort(int s[], int l, int r)
{
    if (l < r) {
        swap(s[l], s[(l + r) / 2]); //将数组中间的数和第一个数交换 以数组中间的数作参考+
        int i = l, j = r, x = s[l];
        while (i < j) {
            while (i < j && s[j] >= x) // 从右向左找第一个小于x的数
                j--;
            if (i < j)
                s[i++] = s[j];
            while (i < j && s[i] < x) // 从左向右找第一个大于等于x的数
                i++;
            if (i < j)
                s[j--] = s[i];
        }
        s[i] = x;
        QuickSort(s, l, i - 1); // 递归调用
        QuickSort(s, i + 1, r);
    }
}

void QSort(int nums[], int st, int ed)
{
    if (st < ed) {
        int q = partition(nums, st, ed);
        QSort(nums, st, q - 1); //左半段排序
        // cout << "左侧半段排序结果:" << endl;
        // for (int i = 0; i < q; i++)
        //     cout << "nums[" << i << "]=" << nums[i] << " ";
        // cout << endl;

        QSort(nums, q + 1, ed);
        // cout << "右侧半段排序结果:" << endl;
        // for (int i = q; i < ed; i++)
        //     cout << "nums[" << i << "]=" << nums[i] << " ";
        // cout << endl;
    }
}
/*
核心是对输入的子数组进行3步处理
1. 分解 以a[p]为基准将a[p:r]划分为3段，a[p:q-1],a[q],a[q+1:r],
使得a[p:q-1]中任何元素小于等于a[q]，a[q+1:r]中任何元素大于等于a[q],q在划分过程中确定

2. 递归求解 通过递归调用快速排序算法分别对a[p:q-1],a[q+1:r]进行排序

3. 合并 由于此例子在数组中就地排序,因此无需额外合并操作
*/

int main(int argc, char const* argv[])
{
    int num[40] = { 40, 29, 5, 4, 3, 27, 8, 1, 26, 2, 10, 19, 45, 14, 13, 27, 38, 11, 16, 12, 30, 29, 35, 34, 23, 17, 18, 21, 36, 12, 30, 47, 44, 50, 15, 65, 37, 49, 39, 47 };
    int nums[4800] = { 0 };
    for (int i = 0; i < 4800; i++) {
        nums[i] = num[i % 40];
    }
    auto p1 = chrono::high_resolution_clock::now();
    QSort(nums, 0, 4799);
    auto p2 = chrono::high_resolution_clock::now();
    cout << "普通版结果: " << endl;
    for (int i = 0; i < 4800; i++)
        cout << nums[i] << " ";
    cout << endl;
    for (int i = 0; i < 4800; i++) {
        nums[i] = num[i % 40];
    }
    auto p3 = chrono::high_resolution_clock::now();
    QuickSort(nums, 0, 4799);
    auto p4 = chrono::high_resolution_clock::now();
    cout << "优化版结果: " << endl;
    for (int i = 0; i < 4800; i++)
        cout << nums[i] << " ";
    cout << endl;
    auto d1 = chrono::duration_cast<chrono::nanoseconds>(p2 - p1);
    auto d2 = chrono::duration_cast<chrono::nanoseconds>(p4 - p3);
    cout << "快速排序普通版耗时: " << d1.count() << "ns" << endl
         << "快速排序优化版耗时: " << d2.count() << "ns" << endl;
    /* int a[5] = { 8, 1, 4, 7, 2 };
    QSort(a, 0, 4);
    for (int i = 0; i < 5; i++)
        cout << a[i] << " ";
    cout << endl;
    */
    system("pause");
    return 0;
}
