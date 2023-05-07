function countPrimes(n: number): number {
    const p: number[] = new Array(n);
    p.fill(1);
    p[0] = 0;
    p[1] = 0;
    for (let i = 2; i * i < n; i++) {
        if (p[i]) {
            for (let j = i * i; j < n; j += i) {
                p[j] = 0;
            }
        }
    }
    let c = 0;
    for (let i = 2; i < n; i++) {
        if (p[i]) {
            c++;
        }
    }
    return c;
};