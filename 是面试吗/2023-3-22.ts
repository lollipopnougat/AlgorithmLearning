function getIndex(arr: number[], l: number, r: number): number {
    const c = arr[l];
    while (l < r) {
        while (l < r && c <= arr[r]) {
            r--;
        }
        arr[l] = arr[r];
        while (l < r && c >= arr[l]) {
            l++;
        }
        arr[r] = arr[l];
    }
    arr[l] = c;
    return l;
}

function qsort(arr: number[], l = 0, r = arr.length - 1) {
    if (l < r) {
        const ind = getIndex(arr, l, r);
        qsort(arr, l, ind - 1);
        qsort(arr, ind + 1, r);
    }
}

function sqsort(arr: number[], l = 0, r = arr.length - 1) {
    if (l < r) {
        const [ol, or] = [l, r];
        const c = arr[l];
        while (l < r) {
            while (l < r && c <= arr[r]) {
                r--;
            }
            arr[l] = arr[r];
            while (l < r && c >= arr[l]) {
                l++;
            }
            arr[r] = arr[l];
        }
        arr[l] = c;
        sqsort(arr, ol, l - 1);
        sqsort(arr, l + 1, or);
    }
}

const array = [6, 8, 7, 5, 4, 1, 3, 2, 9];

sqsort(array);

console.log(array);
