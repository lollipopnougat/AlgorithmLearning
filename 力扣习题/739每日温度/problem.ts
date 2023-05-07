function dailyTemperatures(temperatures: number[]): number[] {
    const stk: number[] = [0];
    const res: number[] = new Array(temperatures.length).fill(0);
    for (let i = 1; i < temperatures.length; i++) {
        while (stk.length > 0 && temperatures[stk[stk.length - 1]] < temperatures[i]) {
            const k = stk.pop();
            res[k] = i - k;
        }
        stk.push(i);
    }
    return res;
};