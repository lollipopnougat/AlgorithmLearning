/*旅行商问题（Traveling Saleman Problem，TSP）又译为旅行推销员问题、货郎担问题，简称为TSP问题，是最基本的路线问题，该问题是在寻求单一旅行者由起点出发，通过所有给定的需求点之后，最后再回到原点的最小路径成本。字面上的理解是：有一个推销员，要到n个城市推销商品，他要找出一个包含所有n个城市的具有最短路程的环路。
解决TSP问题的思想有回溯法、贪心法、动态规划法等。
如果动态规划法解决TSP问题，可以参考程序代码：
*/
#include <iostream>
#include <list>
using namespace std;

typedef list<int> LISTINT;

LISTINT listAnother;
LISTINT list_result;

int d[6][6] = { { -1, 34, 46, -1, -1, 19 }, { 34, -1, -1, -1, 12, -1 }, { 46, -1, -1, 17, -1, 25 }, { -1, -1, 17, -1, 38, 25 }, { 12, -1, -1, 38, -1, 26 }, { 19, -1, 25, 25, 26, -1 } }; //路径权值
int matrix_length = 6;

int getPath(int n, LISTINT list_org)
{

    LISTINT::iterator i;

    int minValue;
    if (n == 1) {
        i = list_org.begin();
        minValue = d[*i - 1][0];
        if (list_org.size() == matrix_length - 1) {
            list_result = list_org;
        }
    } else {
        int temp;
        i = list_org.begin();
        temp = *i;
        list_org.erase(i);
        i = list_org.begin();
        minValue = d[temp - 1][*(i)-1] + getPath(n - 1, list_org);
        if (list_org.size() == matrix_length - 1) {
            list_result = list_org;
        }

        for (int j = 2; j < n; j++) {
            i = list_org.begin();
            for (int k = 1; k < j; k++) {
                i++;
            }

            int tempvalue = *i;
            list_org.erase(i);
            list_org.push_front(tempvalue);
            i = list_org.begin();
            tempvalue = d[temp - 1][*(i)-1] + getPath(n - 1, list_org);

            if (tempvalue < minValue) {
                if (list_org.size() == matrix_length - 1) {
                    list_result = list_org;
                }
                minValue = tempvalue;
            }
        }
    }
    return minValue;
}
int main(int argc, char* argv[])
{

    LISTINT list_org;
    LISTINT::iterator h;
    list_org.push_front(4);
    list_org.push_front(3);
    list_org.push_front(2);
    list_org.push_front(1);
    cout << "旅行商问题动态规划算法" << endl;
    cout << "路线长度的矩阵表示如下 （-1表示无限大）" << endl;
    for (int j = 0; j < matrix_length; j++) {
        cout << endl;
        for (int k = 0; k < matrix_length; k++) {
            cout << " " << d[j][k];
        }
    }
    cout << endl;

    cout << "计算结果:" << getPath(4, list_org) << endl;
    list_result.push_front(1);
    list_result.push_back(1);
    cout << "要走的路径:---->:";
    for (h = list_result.begin(); h != list_result.end(); ++h)

        cout << *h << " ";

    cout << endl;
    int i;
    cin >> i;
    return 0;
}