def myformat(val: float) -> str:
    if val == 0:
        return '+0.00'
    if val > 0:
        return f'+{val:.2f}'
    else:
        return f'{val:.2f}'


def main(inps):
    # inps = []
    # for i in range(24):
    #     inps.append(input())
    inp = outp = 0
    outpi = inpi = 0
    for i in range(1, 24, 2):
        his = 0
        tmp = inps[i].split(' ')
        for j in tmp:
            val = float(j.split(':')[1])
            his += val
        if his < outp:
            outp = his
            outpi = i
        elif his > inp:
            inpi = i
            inp = his
        print(f'{inps[i - 1].split(":")[0]}:{myformat(his)}')
    print(f'{inps[outpi - 1].split(":")[0]} {inps[inpi - 1].split(":")[0]}')


inps = [
    'January:2', 
    'clothe:-120.00 teach:+1050.50', 
    'February:1',
    'teach:+550.55', 
    'March:1', 
    'important:+100.50', 
    'April:3',
    'sugol:-88.88 oishii:-99.99 subarashi:+999.98', 
    'May:1', 
    'nomay:-1024.00',
    'June:4', 
    'one:+10.00 two:+20.00 thee:+30.00 four:+40.00', 
    'July:1',
    'important:+100.50', 
    'August:1', 
    'important:+100.50', 
    'September:1',
    'important:+100.50', 
    'October:1', 
    'important:+100.50', 
    'November:1',
    'important:+100.50', 
    'December:1', 
    'important:+100.50'
]

main(inps)