export { };
declare global {
    interface Array<T> {
        snail(rowsCount: number, colsCount: number): number[][];
    }
}

Array.prototype.snail = function (rowsCount: number, colsCount: number): number[][] {
    if (rowsCount * colsCount != this.length) {
        return [];
    }
    const res: number[][] = new Array(rowsCount);
    for (let i = 0; i < rowsCount; i++) {
        res[i] = new Array(colsCount);
    }
    for (let i = 0; i < rowsCount; i++) {
        for (let j = 0; j < colsCount; j++) {
            if (j % 2 == 0) {
                res[i][j] = this[j * rowsCount + i];
            } else {
                res[rowsCount - i - 1][j] = this[j * rowsCount + i];
            }
        }
    }
    return res;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */