export { };

type F = () => Promise<any>;
function promisePool(functions: F[], n: number): Promise<any> {
    return new Promise(res => {
        const result: any[] = new Array(functions.length);
        let cur = 0;
        const vis: Set<number> = new Set();
        const fine: Set<number> = new Set();
        const run = async () => {
            if (fine.size == functions.length) {
                res(result);
            }
            if (cur < functions.length) {
                while (vis.has(cur)) {
                    cur++;
                }
                if (cur < functions.length) {
                    const mc = cur;
                    vis.add(mc);
                    result[mc] = await functions[mc]();
                    fine.add(mc);
                    run();
                }
            }
        };
        for (let i = 0; i < n; i++) {
            run();
        }
    });
};