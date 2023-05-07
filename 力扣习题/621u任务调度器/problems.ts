function leastInterval(tasks: string[], n: number): number {
    // task, cool-down
    if (n == 0) {
        return tasks.length;
    }
    const taskMap = new Map<string, number>();
    tasks.forEach(e => taskMap.set(e, taskMap.get(e) !== undefined ? taskMap.get(e) as number + 1 : 1));
    const taskList = Array.from(taskMap.keys());
    // taskList.sort((x, y) => taskMap.)
    const coolMap = new Map<string, number>();
    let time = 0;
    const queue: string[] = [tasks[0]];
    const value = taskMap.get(tasks[0]) as number;
    if (value == 1) {
        taskMap.delete(tasks[0]);
    } else {
        taskMap.set(tasks[0], value - 1);
    }
    while (queue.length != 0 && taskMap.size != 0) {
        const task = queue.shift() as string;
        console.log(`执行 ${task}`);
        time++;
        coolMap.set(task, time);
        coolMap.forEach((v, k) => {
            if (time - v >= n) {
                coolMap.delete(k);
            }
        });
        let nextTask: string | undefined = undefined;
        let lastTask!: string;
        let leftTime = 0;
        taskMap.forEach((v, k) => {
            if (!coolMap.has(k)) {
                leftTime = 0;
                nextTask = k;
            } else if (time - (coolMap.get(k) as number) > leftTime) {
                leftTime = time - (coolMap.get(k) as number);
                lastTask = k;
            }
        });
        if (!nextTask) {
            nextTask = lastTask;
            time += leftTime;
        }
        queue.push(nextTask);
        const value = taskMap.get(nextTask) as number;
        if (value == 1) {
            taskMap.delete(nextTask);
        } else {
            taskMap.set(nextTask, value - 1);
        }
    }
    return time;
};


let task1 = ['A', 'A', 'A', 'B', 'B', 'B'];
console.log(leastInterval(task1, 2));

// task1 = ['A', 'A', 'A', 'B', 'B', 'B'];
console.log(leastInterval(task1, 0));

task1 = ['A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'];
console.log(leastInterval(task1, 2));