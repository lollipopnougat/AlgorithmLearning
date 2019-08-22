# -*- coding: UTF-8 -*-
# 斐波那契数列 yield 实现
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b      
        a, b = b, a + b 
        n = n + 1


if __name__ == "__main__":
    try:
        num = int(input('输入项数: '))
        for n in fab(num): 
            print(n)
    except Exception as er:
        print('错误!' + str(er))
    input()
    