// interface EdgeSet {
//     in: Set<number>;
//     out: Set<number>;
// }

// function canFinish(numCourses: number, prerequisites: number[][]): boolean {
//     const edges: EdgeSet[] = new Array(numCourses);
//     const vis: Set<number> = new Set();
//     const stk: number[] = [];
//     for (let i = 0; i < numCourses; i++) {
//         edges[i] = {
//             in: new Set(),
//             out: new Set()
//         };
//     }
//     for (let i of prerequisites) {
//         edges[i[0]].in.add(i[1]);
//         edges[i[1]].out.add(i[0]);
//     }
//     for (let i = 0; i < numCourses; i++) {
//         vis.clear();
//         stk.length = 0;
//         stk.push(i);
//         while (stk.length != 0) {
//             const it = stk.shift() as number;
//             let flag = false;
//             for (let j of edges[it].in) {
//                 if (!vis.has(j)) {
//                     flag = true;
//                     break;
//                 }
//             }
//             if (flag) {
//                 break;
//             }
//             if (vis.has(it)) {
//                 break;
//             }
//             vis.add(it);
//             for (let j = 0; j < numCourses; j++) {
//                 let flag = false;
//                 for (let k of edges[j].in) {
//                     if (!vis.has(k)) {
//                         flag = true;
//                         break;
//                     }
//                 }
//                 if (flag && !vis.has(j)) {
//                     stk.push(j);
//                 }
//             }
//         }
//         if (vis.size == numCourses) {
//             return true;
//         }
//     }
//     return false;
// };

function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // 存储有向图
    const edges: Map<number, number[]> = new Map();
    // 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
    const vis = new Array(numCourses).fill(0);
    const res: number[] = [];
    // 判断有向图中是否有环
    let h = true;
    for(let i = 0; i < numCourses; i++) {
        edges.set(i, []);
    }
    prerequisites.forEach(v => {
        (edges.get(v[1]) as number[]).push(v[0]);
    });
    const dfs = (u: number) => {
        // 将节点标记为「搜索中」
        vis[u] = 1;
        // 搜索其相邻节点
        // 只要发现有环，立刻停止搜索
        for (let i of (edges.get(u) as number[])) {
            // 如果「未搜索」那么搜索相邻节点
            if (vis[i] == 0) {
                dfs(i);
                if (!h) {
                    return;
                }
            // 如果「搜索中」说明找到了环
            } else if(vis[i] == 1) {
                h = false;
                return;
            } 
        }
        // 将节点标记为「已完成」
        vis[u] = 2;
        // 将节点入栈
        res.unshift(u);
    };
    // 每次挑选一个「未搜索」的节点，开始进行深度优先搜索
    for (let i = 0; i < numCourses; i++) {
        if (h && !vis[i]) {
            dfs(i);
        }
    }
    // 环
    if(!h) {
        return false; 
    }
    // 如果没有环，那么就有拓扑排序
    return res.length == numCourses;
}


console.log(canFinish(2, [[1, 0]]));
console.log(canFinish(2, []));
console.log(canFinish(2, [[1, 0], [0, 1]]));
console.log(canFinish(5, [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 4]]));