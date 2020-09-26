
#include <stdio.h>
#include<conio.h> 
#define COM -1 
#define MAN 1
#define STEP 9 
#define DRAW 0 
#define ROW 3 
#define COL 3
#define MAX_NUM 1000;
COM = -1
MAN = 1
STEP = 9
DRAW = 0
ROW = 3
COL = 3
MAX_NUM = 65535
 
class Move:
    def __init__(self):
        self.x = 0
        self.y = 0
 

 
# 棋盘
board = [([0]*3) for _ in range(3)]
tempBoard = [([0]*3) for _ in range(3)]

# 玩家
player = MAN

# 最好的一步
bestMove = Move()

# 当前深度
currentDepth = 0

# 谁先走
MAN_first = True
 
 
# 判断输赢
def isWin() -> int:
 
    for i in range(3):
        if sum(board[i]) == 3:
            return 1
        elif sum(board[i]) == -3:
            return -1
    
    for j in range(3):
        if board[0][j] + board[1][j] + board[2][j] == 3:
            return 1
        elif board[0][j] + board[1][j] + board[2][j] == -3:
            return -1

    if board[0][0] + board[1][1] + board[2][2] == 3 or board[0][2] + board[1][1] + board[2][0] == 3:
        return 1
    elif board[0][0] + board[1][1] + board[2][2] == -3 or board[0][2] + board[1][1] + board[2][0] == -3:
        return -1
    else:
        return 0
 
# 评估函数
def evaluteMap() -> int:

    flag = True

    if isWin() == COM:
        return MAX_NUM # 如果计算机赢了，返回最大值 
    if isWin() == MAN:
        return -MAX_NUM; # 如果计算机输了，返回最小值 

    count = 0 # 该变量用来表示评估函数的值
    # 将棋盘中的空格填满自己的棋子，既将棋盘数组中的0变为1
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                tempBoard[i][j] = COM
            else:
                tempBoard[i][j] = board[i][j]

    # 电脑一方
    # 计算每一行中有多少行的棋子连成3个的
    for i in range(3):
        count += sum(tempBoard[i]) // 3
    for i in range(3):
        count += (tempBoard[0][i] + tempBoard[1][i] + tempBoard[2][i]) // 3
    count += (tempBoard[0][0] + tempBoard[1][1] + tempBoard[2][2]) // 3
    count += (tempBoard[2][0] + tempBoard[1][1] + tempBoard[0][2]) // 3



    # 将棋盘中的空格填满对方的棋子，既将棋盘数组中的0变为-1
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                tempBoard[i][j] = MAN
            else:
                tempBoard[i][j] = board[i][j]

    # 对方
    # 计算每一行中有多少行的棋子连成3个的
    for i in range(3):
        count += sum(tempBoard[i]) // 3;
    for i in range(3):
        count += (tempBoard[0][i] + tempBoard[1][i] + tempBoard[2][i]) // 3
    count += (tempBoard[0][0] + tempBoard[1][1] + tempBoard[2][2]) // 3
    count += (tempBoard[2][0] + tempBoard[1][1] + tempBoard[0][2]) // 3

    return count

 
 
def makeMove(curMove: Move):
    board[curMove.x][curMove.y] = player
    player = MAN if player == COM else COM

 
def unMakeMove(curMove: Move):
    board[curMove.x][curMove.y] = 0
    player = MAN if player == COM else COM

 
# 得到有空位的集合
def getMoveList(moveList: list) -> int:
    moveCount = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                moveList[moveCount].x = i
                moveList[moveCount].y = j
                moveCount += 1
    return moveCount # 返回一共多少个空的位置 
 
 
def miniMaxsearch(depth: int) -> int:
    value = 0  # 估值 
    bestValue = 0 # 最好的估值
    moveCount = 0
    moveList = [Move()] * 9 # 保存可以下子的位置
    if isWin() == COM or isWin() == MAN:
        return evaluteMap() # 一般是返回极大极小值
    #如果搜索深度耗尽, 返回估值 
    if depth == 0:
        return evaluteMap()
 
 
    #根据不同的玩家 进行赋值 
    if COM == player:
        bestValue = -MAX_NUM
    elif MAN == player:
        bestValue = MAX_NUM
 
    # 一共多少步
    moveCount = getMoveList(moveList)
    for i in range(moveCount):
        curMove = moveList[i]
 
        makeMove(curMove)
        value = miniMaxsearch(depth - 1)
        unMakeMove(curMove)
 
        if player == COM:
            if value > bestValue:
                bestValue = value
                if depth == currentDepth:
                    bestMove = curMove
        elif player == MAN:
            if value < bestValue:
                bestValue = value
                if depth == currentDepth:
                    bestMove = curMove     
    return bestValue

 
 
# 打印棋盘 电脑X  ，玩家O 
def printBoard():
    for i in range(3):
        print("-------------")
        for j in range(3):
            if board[i][j] == COM:
                print("| X ", end='')
            elif board[i][j] == MAN:
                print("| O ", end='')
            else:
                print("|   ", end='')
        print("|")
    print("-------------")
 

def com_play():
    miniMaxsearch(currentDepth)
    board[bestMove.x][bestMove.y] = COM
 
def man_play():
    print("请输入位置坐标  e.g ：（0 0）为左上角 （2，2）为右下角");
    x = int(input())
    y = int(input())
 
    while x < 0 or x > 2 or y < 0 or y > 2:
        print("您输入的坐标错误，请重新输入:x:(0~2) , y:(0~2)")
        x = int(input())
        y = int(input())
    while board[x][y] != 0:
        print("该位置已有棋，请重新输入:")
        x = int(input())
        y = int(input())
 
    board[x][y] = MAN
 
 
 
 
 
 
 
def setFirst():
    print("\n谁先走? y -你先走, n-电脑先走");
    c = input('谁先走? y:你先走, n:电脑先走')
    if c == 'n' or c == 'N':
        MAN_first = False
    print("")
 
 
def main():
    currentDepth = 9
    step = 1
    setFirst()
    printBoard()
    if MAN_first:
        player = MAN
        while step <= STEP:
            man_play()
            printBoard()
            if player == isWin():
                print("您获胜了！！")
                break
            step += 1
            currentDepth -= 1
            if step == 10:
                print("平局 ~~~")
                break
            player = MAN if player == COM else COM
            com_play()
            printBoard()
            if player == isWin():
                print("很遗憾，电脑赢啦！！！")
                break
            step += 1
            currentDepth -= 1
            player = MAN if player == COM else COM
    else:
        player = COM
        while step <= STEP:
            com_play()
            printBoard()
            if player == isWin():
                print("很遗憾，电脑赢啦！！！")
                break
            step += 1
            currentDepth -= 1
            if step == 10:
                print("平局 ~~~")
                break
            player = MAN if player == COM else COM
            man_play()
            printBoard()
            if player == isWin():
                print("您获胜了！！")
                break
            step += 1
            currentDepth -= 1
            player = MAN if player == COM else COM

main()

input()
