// -*- coding = utf-8 -*-
#include<iostream>
#include <algorithm>
#include <cstdlib>
using namespace std;
int main()
{
	int w[5] = { 0 , 2 , 3 , 4 , 5 };			//商品的体积2、3、4、5
	int v[5] = { 0 , 3 , 4 , 5 , 6 };			//商品的价值3、4、5、6
	int bagV = 8;					        //背包大小
	int dp[5][9] = { { 0 } };			        //动态规划表
 
	for (int i = 1; i <= 4; i++) {
		for (int j = 1; j <= bagV; j++) {
			if (j < w[i])
				dp[i][j] = dp[i - 1][j];
			else
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i]);
		}
	}
 
	//动态规划表的输出
	for (int i = 0; i < 5; i++) {
		for (int j = 0; j < 9; j++) {
			cout << dp[i][j] << ' ';
		}
		cout << endl;
	}
    system("pause");
	return 0;
}
