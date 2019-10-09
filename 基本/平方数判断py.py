import math

def psqrt(input):
    if input<0:
        print('错了')
    num = math.sqrt(input)
    tmp = num - int(num)
    if tmp != 0:
        print('不是,最近的是',int(num)**2,'和',(int(num)+1)**2)
    else:
        print('是')

number = int(input('输入数字'))
psqrt(number)
