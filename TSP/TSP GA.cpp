//-*- coding=UTF-8 -*-
//TSP遗传算法
/*从遗传两个字，不难想到，这个算法是由生物进化的机理所抽象出来的一种思想。 
对于一个问题，有许多可能的解。 
就拿上述的tsp问题来说吧，每一种遍历顺序都是一个解。所有城市顺序的全排列合在一起就是这个问题的解集。 
我们将每个解都看做一个个体。那么多个个体放在一起就可以构成一个种群。 
大自然每个种群都要经过漫长的自然选择，也就是优胜劣汰，以及繁殖和变异。 
而解所构成的种群也不例外。 
显然，我们可以很明确的对每个个体的优劣性进行评价。本体的条件是总路程最短，根据解得到总路程的大小是很容易的。 
评价过后，对于每个个体的优劣我们都已掌握。 
那么残酷的地方来了，我们要杀死(淘汰)一部分个体。 
当然也不能光杀，温馨的部分也是有的，那就是两两个体交叉繁殖，产生后代。 
除此之外，还要有一点幸运度，那就是变异了，随机的对某些个体进行一些改变。 
上述操作进行完之后，我们已经相当于更新了整个群体。 
然后重复的进行此过程，直到得到满意的(个体)结果。
代码参考：https://blog.csdn.net/to_be_better/article/details/51190617
*/

#include <cstring>
#include <ctime>
#include <iostream>
/*
void *memcpy(void *dest, const void *src, size_t n);
从源src所指的内存地址的起始位置开始拷贝n个字节到目标dest所指的内存地址的起始位置中
主要用于数组间快速拷贝、填充(既可以是整个数组，亦可以是子数组)
注意：会覆盖原有数据
位于 string.h(cstring)
参考：https://baike.baidu.com/item/memcpy
*/
using namespace std;

const int city_num = 10; //城市数量
const int unit_num = 100; //群体规模
int ps = 10; //变异概率
const int genmax = 500; //最大迭代数

//城市间距离映射 最优解权值=10
int length_table[10][10] = {

    { 0, 1, 1272, 2567, 1653, 2097, 1425, 1177, 3947, 1 },

    { 1, 0, 1, 2511, 1633, 2077, 1369, 1157, 3961, 1518 },

    { 1272, 1, 0, 1, 380, 1490, 821, 856, 3660, 385 },

    { 2567, 2511, 1, 0, 1, 2335, 1562, 2165, 3995, 933 },

    { 1653, 1633, 380, 1, 0, 1, 1041, 1135, 3870, 456 },

    { 2097, 2077, 1490, 2335, 1, 0, 1, 920, 2170, 1920 },

    { 1425, 1369, 821, 1562, 1041, 1, 0, 1, 4290, 626 },

    { 1177, 1157, 856, 2165, 1135, 920, 1, 0, 1, 1290 },

    { 3947, 3961, 3660, 3995, 3870, 2170, 4290, 1, 0, 1 },

    { 1, 1518, 385, 993, 456, 1920, 626, 1290, 1, 0 }
};

class Unit //个体
{
public:
    int path[city_num]; //个体的路径信息
    int length; //个体价值
};

class Group //种群
{
public:
    Unit group[unit_num]; //种群个体数
    Unit best; //优良性状个体
    int best_gen; //好的基因

    Group()
    {
        best.length = 0x3f3f3f3f; //关于这个数，详见最后的注释
        best_gen = 0;
        for (int i = 0; i < unit_num; i++) {
            bool flag[city_num] = { false }; //访问标记置空

            for (int j = 0; j < city_num; j++) {
                int t_city = rand() % city_num;
                while (flag[t_city]) //选择未选择过的开始点
                    t_city = rand() % city_num;
                flag[t_city] = true;
                group[i].path[j] = t_city; //加入路径
            }
        }
    }

    //对每个个体进行评估
    void assess()
    {
        for (int k = 0; k < unit_num; k++) {
            int rel = 0;
            for (int i = 1; i < city_num; i++) //计算权值
                rel += length_table[group[k].path[i - 1]][group[k].path[i]];
            rel += length_table[group[k].path[city_num - 1]][group[k].path[0]];
            group[k].length = rel;
        }
    }

    //根据评估结果对个体进行排序
    void unit_sort()
    {
        for (int i = 0; i < unit_num; i++) {
            for (int j = i + 1; j < unit_num; j++) {
                if (group[i].length > group[j].length) {
                    Unit temp;
                    memcpy(&temp, &group[i], sizeof(Unit)); //快速填充数组(无需写循环)
                    memcpy(&group[i], &group[j], sizeof(Unit));
                    memcpy(&group[j], &temp, sizeof(Unit));
                }
            }
        }
    }

    //交叉互换
    //索引值：1 2 3 4 5 6 7 8 9 10
    //父个体：1 2 3 4 9 8 7 6 5 0
    //母个体：7 8 9 0 1 6 5 4 3 2
    //那么随机取两个值，比如：4和6
    //将父个体划分：1 2 3 [4 9] 8 7 6 5 0
    //则，将划分区间内的基因赋给子个体
    //子个体：x x x 4 9 x x x x x
    //再按照母个体的基因顺序赋值给子个体
    //子个体：7 8 0 4 9 1 6 5 3 2
    Unit cross(Unit& father, Unit& mother)
    {
        int l = rand() % city_num; //划分左端
        int r = rand() % city_num; //划分右端
        if (l > r)
            swap(l, r); //左侧大于右侧，则交换

        bool flag[city_num] = { false }; //访问标记
        for (int i = l; i <= r; i++)
            flag[father.path[i]] = true;

        Unit son;
        int pos = 0; //位置中间变量

        for (int i = 0; i < l; i++) //母个体第一部分
        {
            while (flag[mother.path[pos]])
                pos++;
            son.path[i] = mother.path[pos++];
        }
        for (int i = l; i <= r; i++) //父个体的划分部分
            son.path[i] = father.path[i];
        for (int i = r + 1; i < city_num; i++) //母个体剩余部分
        {
            while (flag[mother.path[pos]])
                pos++;
            son.path[i] = mother.path[pos++];
        }

        return son;
    }
    /*突变 倒位
    位置：  1 2 3 4 5 6 7 8 9 10
    个体：  1 2 3 4 9 8 7 6 5 0
    随机选取两个值，比如：4和6
    那么，交换位置4和位置6的基因。
    新个体：1 2 3 8 9 4 7 6 5 0
    */
    void mutation(Unit& t)
    {
        int proport = rand() % 100; //随机取比例

        if (proport > ps) //如果大于突变比率那么不突变
            return;
        int one = rand() % city_num;
        int two = rand() % city_num;
        while (two == one) //如果对应位置相等 那么2再随机选择一个新的位置
            two = rand() % city_num;
        swap(t.path[one], t.path[two]); //交换
    }

    //输出信息
    void print()
    {
        for (int i = 0; i < unit_num; i++) {
            cout << "第" << i << "个个体，路径信息：";
            for (int j = 0; j < city_num; j++)
                cout << group[i].path[j] << " ";

            cout << ";总权值：" << group[i].length << endl;
        }
        cout << "最优个体，路径信息：";
        for (int j = 0; j < city_num; j++)
            cout << group[0].path[j] << " ";

        cout << ";总权值：" << group[0].length << endl;
    }

    //种群进化
    void work()
    {
        for (int i = 0; i < genmax; i++) {
            //如果进化层数大于20，加大变异的概率
            if (i > 20)
                ps *= 3;

            assess(); //评估

            unit_sort(); //根据评估结果排序

            if (best.length > group[0].length) {
                memcpy(&best, &group[0], sizeof(group[0])); //拷贝内存(数组)
                best_gen = i;
            }

            for (int j = 0; j + 2 < unit_num; j += 3) //
                group[j + 2] = cross(group[j], group[j + 1]);

            for (int j = 0; j < city_num; j++) //变异(从1开始，保留最优)
                mutation(group[j]);
        }
    }
};

Unit group[unit_num]; //种群变量
Unit bestone; //记录最短路径
int generation_num; //记录当前达到了第几代

int main()
{
    srand((int)time(0)); //随机数种子，保证每次打开都是随机取值

    for (int i = 0; i < 20; i++) {
        Group g;
        g.work();
        cout << "第" << i + 1 << "次求解。路径：";
        for (int j = 0; j < city_num; j++)
            cout << g.best.path[j] << " ";
        cout << ";总权值：" << g.best.length << "; 第" << g.best_gen << "代" << endl;
    }
    return 0;
}
/*
为什么把 0x3f3f3f3f作为无穷大使用

如果问题中各数据的范围明确，那么无穷大的设定不是问题，在不明确的情况下，
很多程序员都取0x7fffffff作为无穷大，因为这是32-bit int的最大值。
如果这个无穷大只用于一般的比较（比如求最小值时min变量的初值），
那么0x7fffffff确实是一个完美的选择，但是在更多的情况下，0x7fffffff并不是一个好的选择。

很多时候并不只是单纯拿无穷大来作比较，而是会运算后再做比较，
例如在大部分最短路径算法中都会使用的松弛操作：
if (d[u]+w[u][v]<d[v]) d[v]=d[u]+w[u][v];
如果u,v之间没有边，那么w[u][v]=INF，
如果INF取0x7fffffff，那么d[u]+w[u][v]会溢出而变成负数，
松弛操作便出错了，
更一般的说，0x7fffffff不能满足“无穷大加一个有穷的数依然是无穷大”，
它变成了一个很小的负数。
除了要满足加上一个常数依然是无穷大之外，
常量还应该满足“无穷大加无穷大依然是无穷大”，
至少两个无穷大相加不应该出现灾难性的错误，这一点上0x7fffffff依然不能满足
所以需要一个更好的家伙来顶替0x7fffffff，
最严谨的办法当然是对无穷大进行特别处理，
而不是找一个很大很大的常量来代替它（或者说模拟它），
但是这样会让编程过程变得很麻烦。
在目前文献中最精巧的无穷大常量取值是0x3f3f3f3f，
1、 0x3f3f3f3f的十进制是1061109567，也就是10^9级别的（和0x7fffffff一个数量级），
而一般场合下的数据都是小于10^9的，所以它可以作为无穷大使用而不致出现数据大于无穷大的情形
另一方面，由于一般的数据都不会大于10^9，所以当把无穷大加上一个数据时，
它并不会溢出（这就满足了“无穷大加一个有穷的数依然是无穷大”），
事实上0x3f3f3f3f+0x3f3f3f3f=2122219134，这非常大，
但却没有超过32-bit int的表示范围，
所以0x3f3f3f3f还满足了“无穷大加无穷大还是无穷大”的需求。
最后，0x3f3f3f3f还能带来一个意想不到的额外好处：
如果想要将某个数组清零，
通常会使用memset(a,0,sizeof(a))这样的代码来实现（方便而高效），
但是当想将某个数组全部赋值为无穷大时（例如解决图论问题时邻接矩阵的初始化），
就不能使用memset函数而得自己写循环了（写这些不重要的代码真的很痛苦），
这是因为memset是按字节操作的，它能够对数组清零是因为0的每个字节都是0，
现在，如果将无穷大设为0x3f3f3f3f，那么就很容易实现，
0x3f3f3f3f的每个字节都是0x3f，所以要把一段内存全部置为无穷大，
只需要memset(a,0x3f,sizeof(a))即可
参考：https://blog.csdn.net/L_apple8/article/details/52525752
*/