function throttle(fn, t) {
    var arg = undefined;
    var timer = null;
    return function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        arg = args;
        if (timer) {
            return;
        }
        else {
            if (args) {
                fn.apply(void 0, args);
                arg = undefined;
            }
            timer = setInterval(function () {
                if (arg) {
                    fn.apply(void 0, arg);
                    arg = undefined;
                }
                else {
                    clearInterval(timer);
                    timer = null;
                }
            }, t);
        }
    };
}
;
var throttled = throttle(console.log, 1000);
throttled("log"); // logged immediately.
throttled("log"); // logged at t=100ms.
throttled("log2"); // logged at t=100ms.
throttled("log"); // logged at t=100ms.
throttled("log4"); // logged at t=100ms.
setTimeout(function () {
    throttled('123');
    throttled('122');
    throttled('121');
}, 1500);
