def main(inp):
    # inp = input()
    nums = []
    for i in inp:
        if 48 <= ord(i) <= 57:
            nums.append(ord(i) - 48)
        else:
            nums.append(ord(i) - 55)
    m = max(nums)
    for i in range(m + 1, 17):
        print(int(inp, i) % 1000000007)


main('11')
# main('23')
# main('FF')