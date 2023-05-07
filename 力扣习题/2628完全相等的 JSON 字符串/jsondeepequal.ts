function areDeeplyEqual(o1: any, o2: any): boolean {
    if (o1 === null || o2 === null) {
        return JSON.stringify(o1) == JSON.stringify(o2);
    }
    if (typeof o1 === 'object' && typeof o2 === 'object') {
        if (o1 instanceof Array && o2 instanceof Array) {
            if (o1.length != o2.length) {
                return false;
            }
            for (let i = 0; i < o1.length; i++) {
                if (!areDeeplyEqual(o1[i], o2[i])) {
                    return false;
                }
            }
            return true;
        } else if (o1 instanceof Array || o2 instanceof Array) {
            return false;
        }
        const k1s = new Set(Object.keys(o1));
        const k2 = Object.keys(o2);
        if (k2.length != k1s.size) {
            return false;
        }
        let res = true;
        for (let k of k2) {
            if (!k1s.has(k)) {
                return false;
            } else {
                res &&= areDeeplyEqual(o1[k], o2[k]);
                if (!res) {
                    return false;
                }
            }
        }
        return true;
    } else {
        return o1 === o2;
    }
};