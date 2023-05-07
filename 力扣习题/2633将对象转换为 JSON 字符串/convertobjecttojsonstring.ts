function jsonStringify(object: any): string {
    if (object === null) {
        return 'null';
    }
    if (typeof object === 'object') {
        const res: string[] = [];
        if (object instanceof Array) {
            res.push(...object.map(e => jsonStringify(e)));
            return `[${res.join(',')}]`;
        } else {
            Object.keys(object).forEach(k => {
                res.push(`"${k}":${jsonStringify(object[k])}`);
            });
            return `{${res.join(',')}}`;
        }
    } else if (typeof object === 'string') {
        return `"${object}"`;
    } else {
        return object.toString();
    }
};