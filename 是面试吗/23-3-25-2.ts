function q2(text: string, a: number, b: number): number {
    if (text.length < a && text.length < b) {
        return -1;
    }
    const dp = new Array<number>(text.length).fill(Infinity); // dp[i]为字符串从0到i满足条件的最小操作数(初值最大值填充)
    const zeros = new Array<number>(text.length).fill(0); // 前i位0的个数
    const ones = new Array<number>(text.length).fill(0); // 1的个数
    if (text[0] == '0') {
        zeros[0] = 1;
    } else {
        ones[0] = 1;
    }
    for (let i = 1; i < text.length; i++) {
        if (text[i] == '0') {
            zeros[i] = zeros[i - 1] + 1;
            ones[i] = ones[i - 1];
        } else {
            zeros[i] = zeros[i - 1];
            ones[i] = ones[i - 1] + 1;
        }
    }
    dp[a - 1] = Math.min(ones[a - 1], dp[a - 1]);
    dp[b - 1] = Math.min(zeros[b - 1], dp[b - 1]);
    for (let i = Math.max(a, b); i < text.length; i++) {
        if (dp[i - a] == Infinity && dp[i - b] == Infinity) {
            dp[i] = Infinity;
            continue;
        }
        if (dp[i - a] != Infinity) {
            dp[i] = Math.min(dp[i - a] + ones[i] - ones[i - a], dp[i]); // 尝试填0
        }
        if (dp[i - b] != Infinity) {
            dp[i] = Math.min(dp[i - b] + zeros[i] - zeros[i - b], dp[i]); // 尝试填1
        }
    }
    return dp[text.length - 1] != Infinity ? dp[text.length - 1] : -1;
}

console.log(q2('0111110000', 5, 5));
console.log(q2('0000011111', 5, 5));
console.log(q2('0001111000', 4, 3));
console.log(q2('0001111000', 4, 2));
console.log(q2('0001111000', 4, 7));
console.log(q2('0111110000', 5, 5));