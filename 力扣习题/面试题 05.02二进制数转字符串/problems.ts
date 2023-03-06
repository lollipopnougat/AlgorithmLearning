function printBin(num: number): string {
    const res: string[] = ['0', '.'];
    let k = 0.5
    while (res.length < 32) {
        if (num - k > 0) {
            res.push('1');
            num -= k;
            k *= 0.5;
        } else if(num - k == 0) {
            num -= k;
            res.push('1');
            break;
        } else {
            res.push('0');
            k *= 0.5;
        }
    }
    if (num != 0) {
        return 'ERROR';
    } 
    return res.join('');

};