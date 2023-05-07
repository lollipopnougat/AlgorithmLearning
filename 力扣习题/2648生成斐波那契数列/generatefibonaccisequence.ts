function* fibGenerator(): Generator<number, any, number> {
    let [l1, l2] = [0, 1];
    for (let i = 0; i < 51; i++) {
        if (i == 0) {
            yield l1;
        } else if (i == 1) {
            yield l2;
        } else {
            let ne = l1 + l2;
            l1 = l2;
            l2 = ne;
            yield ne;
        }
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */