"use strict";
function backpack01(goods, capacity) {
    const dp = new Array(goods.length + 1);
    for (let i = 0; i < goods.length + 1; i++) {
        dp[i] = new Array(capacity + 1).fill(0);
    }
    // console.log(dp);
    for (let i = 1; i < goods.length + 1; i++) {
        for (let j = 1; j < capacity + 1; j++) {
            if (j >= goods[i - 1].bulk) {
                dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - goods[i - 1].bulk] + goods[i - 1].value);
            }
            else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }
    return dp[goods.length][capacity];
}
const goods = [
    { bulk: 1, value: 2 },
    { bulk: 2, value: 2 },
    { bulk: 6, value: 5 },
    { bulk: 4, value: 3 },
    { bulk: 5, value: 4 },
];
console.log(backpack01(goods, 8));
function backpack012(goods, capacity) {
    const dp = new Array(capacity + 1).fill(0);
    // console.log(dp);
    for (let i = 0; i < goods.length; i++) {
        for (let j = capacity; j > 0; j--) {
            if (j >= goods[i].bulk) {
                dp[j] = Math.max(dp[j], dp[j - goods[i].bulk] + goods[i].value);
            }
            else {
                dp[j] = dp[j];
            }
        }
    }
    return dp[capacity];
}
function backpack013(goods, capacity) {
    const dp = new Array(capacity + 1).fill(0);
    let sum = goods.reduce((su, v) => v.bulk, 0);
    // console.log(dp);
    for (let i = 0; i < goods.length; i++) {
        sum -= (i > 0 ? goods[i - 1].bulk : 0);
        const bound = Math.max(capacity - sum, goods[i].value);
        for (let j = capacity; j >= bound; j--) {
            if (j >= goods[i].bulk) {
                dp[j] = Math.max(dp[j], dp[j - goods[i].bulk] + goods[i].value);
            }
            else {
                dp[j] = dp[j];
            }
        }
    }
    return dp[capacity];
}
console.log(backpack013(goods, 8));
