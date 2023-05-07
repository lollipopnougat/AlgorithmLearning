/**
 * n拆分为最少的完全平方数数量
 * 数学方法实现
 * @param n 一个整数
 * @returns 最少的完全平方数数量 
 */
function numSquares(n: number): number {
    while(n % 4 == 0) {
        n /= 4;
    }
    if (n % 8 == 7) {
        return 4;
    }
    let a = 0;
    while(a ** 2 <= n) {
        const b = Math.floor(Math.sqrt(n - a ** 2));
        if (a ** 2 + b ** 2 == n) {
            return (a > 0 ? 1 : 0) + (b > 0 ? 1 : 0); 
        }
        a++;
    }
    return 3;
};

// /**
//  * 完全背包
//  * @param n 一个整数
//  * @returns 最少的完全平方数数量 
//  */
// function numSquares2(n: number): number {
//     const sq = Math.sqrt(n);
//     if(sq - Math.floor(sq) == 0) {
//         return 1;
//     }
// };