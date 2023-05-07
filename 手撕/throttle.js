"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.counter = void 0;
const throttle = (fn, delay = 500, immediate = true) => {
    let timeout = null;
    return (...arg) => {
        if (immediate) {
            fn(...arg);
            immediate = false;
        }
        if (timeout) {
            return;
        }
        else {
            timeout = setTimeout(() => {
                fn(...arg);
                timeout = null;
            }, delay);
        }
    };
};
function counter() {
    let c = 0;
    return () => {
        c++;
        console.log(`执行第 ${c} 次`);
    };
}
exports.counter = counter;
const count = counter();
const dcount = throttle(count, 1000, false);
let timeout = setInterval(() => {
    dcount();
}, 500);
setTimeout(() => {
    clearInterval(timeout);
}, 5000);
