"use strict";
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
function canFinish(numCourses, prerequisites) {
    const edges = new Map();
    const vis = new Array(numCourses).fill(0);
    const res = [];
    let h = true;
    for (let i = 0; i < numCourses; i++) {
        edges.set(i, []);
    }
    prerequisites.forEach(v => {
        edges.get(v[1]).push(v[0]);
    });
    const dfs = (u) => {
        vis[u] = 1;
        for (let i of edges.get(u)) {
            if (vis[i] == 0) {
                dfs(i);
                if (!h) {
                    return;
                }
            }
            else if (vis[i] == 1) {
                h = false;
                return;
            }
        }
        vis[u] = 2;
        res.unshift(u);
    };
    for (let i = 0; i < numCourses; i++) {
        if (h && !vis[i]) {
            dfs(i);
        }
    }
    if (!h) {
        return false;
    }
    return res.length == numCourses;
}
console.log(canFinish(2, [[1, 0]]));
console.log(canFinish(2, []));
console.log(canFinish(2, [[1, 0], [0, 1]]));
console.log(canFinish(5, [[0, 1], [0, 2], [0, 3], [1, 4], [2, 4], [3, 4]]));
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoicHJvYmxlbXMuanMiLCJzb3VyY2VSb290IjoiIiwic291cmNlcyI6WyJwcm9ibGVtcy50cyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiO0FBQUEsc0JBQXNCO0FBQ3RCLHVCQUF1QjtBQUN2Qix3QkFBd0I7QUFDeEIsSUFBSTtBQUVKLCtFQUErRTtBQUMvRSxzREFBc0Q7QUFDdEQsMENBQTBDO0FBQzFDLGdDQUFnQztBQUNoQyw2Q0FBNkM7QUFDN0MsdUJBQXVCO0FBQ3ZCLDZCQUE2QjtBQUM3Qiw2QkFBNkI7QUFDN0IsYUFBYTtBQUNiLFFBQVE7QUFDUixxQ0FBcUM7QUFDckMsb0NBQW9DO0FBQ3BDLHFDQUFxQztBQUNyQyxRQUFRO0FBQ1IsNkNBQTZDO0FBQzdDLHVCQUF1QjtBQUN2QiwwQkFBMEI7QUFDMUIsdUJBQXVCO0FBQ3ZCLG9DQUFvQztBQUNwQyxnREFBZ0Q7QUFDaEQsZ0NBQWdDO0FBQ2hDLDRDQUE0QztBQUM1QyxxQ0FBcUM7QUFDckMsbUNBQW1DO0FBQ25DLDZCQUE2QjtBQUM3QixvQkFBb0I7QUFDcEIsZ0JBQWdCO0FBQ2hCLDBCQUEwQjtBQUMxQix5QkFBeUI7QUFDekIsZ0JBQWdCO0FBQ2hCLGlDQUFpQztBQUNqQyx5QkFBeUI7QUFDekIsZ0JBQWdCO0FBQ2hCLDJCQUEyQjtBQUMzQixxREFBcUQ7QUFDckQsb0NBQW9DO0FBQ3BDLCtDQUErQztBQUMvQyx5Q0FBeUM7QUFDekMsdUNBQXVDO0FBQ3ZDLGlDQUFpQztBQUNqQyx3QkFBd0I7QUFDeEIsb0JBQW9CO0FBQ3BCLDZDQUE2QztBQUM3QyxtQ0FBbUM7QUFDbkMsb0JBQW9CO0FBQ3BCLGdCQUFnQjtBQUNoQixZQUFZO0FBQ1osd0NBQXdDO0FBQ3hDLDJCQUEyQjtBQUMzQixZQUFZO0FBQ1osUUFBUTtBQUNSLG9CQUFvQjtBQUNwQixLQUFLO0FBRUwsU0FBUyxTQUFTLENBQUMsVUFBa0IsRUFBRSxhQUF5QjtJQUM1RCxNQUFNLEtBQUssR0FBMEIsSUFBSSxHQUFHLEVBQUUsQ0FBQztJQUMv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