// -*- coding=utf-8 -*-
// TSP 完全图下的贪心优化算法
#include <iostream>
#include <string>
using namespace std;
int visited[4] = {0};
int arc[4][4] = {
	{65535, 8, 9, 5},
	{8, 65535, 6, 7},
	{9, 6, 65535, 7},
	{5, 7, 7, 65535}
}; //路径权值
char vexname[4] = {'0', '1', '2', '3'};
int length = 0; //路径长度 
int vexnum = 4, arcnum = 6, root;//顶点数、边数、遍历开始节点 
string path,tmp; //路径字符串 


bool AllVisited() //是否全部访问过 
{
	for (int i = 0; i < vexnum; i++)
		if (visited[i] == 0)
			return false;
	return true;
}

//一趟贪心算法
//每一趟次找最小值，迭代（完全图下肯定能找到回路） 
void AvariceAlgorithm(int v)
{
	path += vexname[v];
	visited[v] = 1;
	if (AllVisited()) //是否是最后一个访问到的节点 
	{
		length += arc[v][root]; //权值表 
		path += vexname[root]; //路径 		 //// 0 1 2 3
	}										//0// ∞ 8 9 5 这一行最小值是5，代表顶点"3"
	else									//1// 8 ∞ 6 7
	{										//2// 9 6 ∞ 7
		int min = 65535, minIndex = 0;		//3// 5 7 7 ∞ 这一行最小值是7(5代表的"0"点访问过了)
		for (int i = 0; i < vexnum; i++)	
		{
			if (arc[v][i] < min && visited[i] == 0)
			{
				min = arc[v][i]; //最小值 
				minIndex = i; //最小值索引值 
			}
		}
		length += min;
		AvariceAlgorithm(minIndex);//递归这趟找到的最小值 
	}
}
void recycle() //循环各个顶点，求最优解 
{
	int len=65535;
	for (int i = 0; i < vexnum; i++)
	{
		root=i;
		path=""; //路径置空
		length=0;  //总权值置0
		for(int i=0;i<vexnum;i++)
		visited[i]=0; //清除访问标记
		AvariceAlgorithm(root);
		{
			len=length;
			tmp=path;
		}
	}
	length=len; //最优权值 
	path=tmp; //最优路径 
} 
int main(int argc, char const *argv[])
{
	recycle(); //调用循环函数 
	cout << "最优权值:" << length << endl << "最优路径:" << endl;
	for (int i = 0; i < path.size(); i++)
	{
		if (i < path.size() - 1)
			cout << path[i] << "-->"; //格式输出路径用 
		else cout << path[i] << endl;
	}
	return 0;
}




