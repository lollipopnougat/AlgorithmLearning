// -*- coding=utf-8 -*-
// TSP 回溯法
#include <iostream>
#include <string>

using namespace std;
const int MAX = 10;

const int city_num = 10; //城市数量

//城市间距离映射 最优解权值=10
int arc[MAX][MAX] = {

    {0, 1, 1272, 2567, 1653, 2097, 1425, 1177, 3947, 1},

    {1, 0, 1, 2511, 1633, 2077, 1369, 1157, 3961, 1518},

    {1272, 1, 0, 1, 380, 1490, 821, 856, 3660, 385},

    {2567, 2511, 1, 0, 1, 2335, 1562, 2165, 3995, 933},

    {1653, 1633, 380, 1, 0, 1, 1041, 1135, 3870, 456},

    {2097, 2077, 1490, 2335, 1, 0, 1, 920, 2170, 1920},

    {1425, 1369, 821, 1562, 1041, 1, 0, 1, 4290, 626},

    {1177, 1157, 856, 2165, 1135, 920, 1, 0, 1, 1290},

    {3947, 3961, 3660, 3995, 3870, 2170, 4290, 1, 0, 1},

    {1, 1518, 385, 993, 456, 1920, 626, 1290, 1, 0}
};


int visited[MAX] = { 0 };
//int arc[MAX][MAX]; //路径权值
int vexname[MAX];
int length = 0; //路径长度
int vexnum = 10, arcnum = 100; //顶点数、边数、遍历开始节点
string path, tmp; //路径字符串

void prin() //输出用
{
    cout << "最优权值:" << length << endl
         << endl
         << "最优路径:";
    for (int i = 0; i < path.size(); i++) {
        if (i < path.size() - 1)
            cout << path[i] << " "; //格式输出路径用
        else
            cout << path[i] << endl;
    }
}

int cl = 0, bestl = 1000, bestx[10], temp;
void swap(int& x, int& y)
{
    temp = x;
    x = y;
    y = temp;
}
void Traveling(int t)
{
    if (t >= vexnum) //到达叶子结点
    {
        if (arc[vexname[vexnum - 1]][0] != 0 && cl + arc[vexname[vexnum - 1]][0] < bestl) //推销员到的最后一个城市与出发的城市之间有路径，且当前总费用比当前最优值小
        {
            for (int j = 0; j < vexnum; j++) //把本次得到的路径顺序，和花费保存下来，不然返回时将被重置
                bestx[j] = vexname[j];
            bestl = cl + arc[vexname[vexnum - 1]][0];
        }
    } else //没有到达叶子结点
    {
        for (int j = t; j < vexnum; j++) //搜索所有与当前所在城市临近的城市
        {
            if (arc[vexname[t - 1]][vexname[j]] != 0 && cl + arc[vexname[t - 1]][vexname[j]] < bestl) //若第t-1个城市与第t个城市之间有路径且可以得到更便宜的路线
            {
                swap(vexname[t], vexname[j]); //保存要去的第t个城市到x[t]中
                cl += arc[vexname[t - 1]][vexname[t]]; //费用增加
                Traveling(t + 1); //搜索下一个城市
                cl -= arc[vexname[t - 1]][vexname[t]]; //还原现场，以便下一次循环
                swap(vexname[t], vexname[j]);
            }
        }
    }
}

int main(int argc, const char** argv)
{
    for (int i = 0; i < vexnum; i++) //初始化 节点名称
        bestx[i] = 0;
    Traveling(1);
    cout << "城市路线： ";
    for (int i = 0; i < vexnum; i++)
        cout << bestx[i] << ' ';
    cout << bestx[0] << endl
         << endl;
    cout << "最小费用： " << bestl << endl
         << endl;
    cl = 0;
    bestl = 1000;
    return 0;
}