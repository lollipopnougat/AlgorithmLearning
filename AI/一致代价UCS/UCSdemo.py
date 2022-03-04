import pandas as pd
from pandas import Series, DataFrame
 
# 城市信息：city1 city2 path_cost
_city_info = None
 
# 按照路径消耗进行排序的FIFO,低路径消耗在前面
_frontier_priority = []
 
 
# 节点数据结构
class Node:
    def __init__(self, state, parent, action, path_cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
 
 
def main():
    global _city_info
    import_city_info()
 
    while True:
        src_city = input('输入初始城市\n')
        dst_city = input('输入目的城市\n')
        # result = breadth_first_search(src_city, dst_city)
        result = uniform_cost_search(src_city, dst_city)
        if not result:
            print('从城市: %s 到城市 %s 查找失败' % (src_city, dst_city))
        else:
            print('从城市: %s 到城市 %s 查找成功' % (src_city, dst_city))
            path = []
            while True:
                path.append(result.state)
                if result.parent is None:
                    break
                result = result.parent
            size = len(path)
            for i in range(size):
                if i < size - 1:
                    print('%s->' % path.pop(), end='')
                else:
                    print(path.pop())
 
 
def import_city_info():
    global _city_info
    data = [{'city1': 'Oradea', 'city2': 'Zerind', 'path_cost': 71},
            {'city1': 'Oradea', 'city2': 'Sibiu', 'path_cost': 151},
            {'city1': 'Zerind', 'city2': 'Arad', 'path_cost': 75},
            {'city1': 'Arad', 'city2': 'Sibiu', 'path_cost': 140},
            {'city1': 'Arad', 'city2': 'Timisoara', 'path_cost': 118},
            {'city1': 'Timisoara', 'city2': 'Lugoj', 'path_cost': 111},
            {'city1': 'Lugoj', 'city2': 'Mehadia', 'path_cost': 70},
            {'city1': 'Mehadia', 'city2': 'Drobeta', 'path_cost': 75},
            {'city1': 'Drobeta', 'city2': 'Craiova', 'path_cost': 120},
            {'city1': 'Sibiu', 'city2': 'Fagaras', 'path_cost': 99},
            {'city1': 'Sibiu', 'city2': 'Rimnicu Vilcea', 'path_cost': 80},
            {'city1': 'Rimnicu Vilcea', 'city2': 'Craiova', 'path_cost': 146},
            {'city1': 'Rimnicu Vilcea', 'city2': 'Pitesti', 'path_cost': 97},
            {'city1': 'Craiova', 'city2': 'Pitesti', 'path_cost': 138},
            {'city1': 'Fagaras', 'city2': 'Bucharest', 'path_cost': 211},
            {'city1': 'Pitesti', 'city2': 'Bucharest', 'path_cost': 101},
            {'city1': 'Bucharest', 'city2': 'Giurgiu', 'path_cost': 90},
            {'city1': 'Bucharest', 'city2': 'Urziceni', 'path_cost': 85},
            {'city1': 'Urziceni', 'city2': 'Vaslui', 'path_cost': 142},
            {'city1': 'Urziceni', 'city2': 'Hirsova', 'path_cost': 98},
            {'city1': 'Neamt', 'city2': 'Iasi', 'path_cost': 87},
            {'city1': 'Iasi', 'city2': 'Vaslui', 'path_cost': 92},
            {'city1': 'Hirsova', 'city2': 'Eforie', 'path_cost': 86}]
 
    _city_info = DataFrame(data, columns=['city1', 'city2', 'path_cost'])
    # print(_city_info)
 
 
def breadth_first_search(src_state, dst_state):
    global _city_info
 
    node = Node(src_state, None, None, 0)
    # 目标测试
    if node.state == dst_state:
        return node
    frontier = [node]
    explored = []
 
    while True:
        if len(frontier) == 0:
            return False
        node = frontier.pop(0)
        explored.append(node.state)
        if node.parent is not None:
            print('处理城市节点:%s\t父节点:%s\t路径损失为:%d' % (node.state, node.parent.state, node.path_cost))
        else:
            print('处理城市节点:%s\t父节点:%s\t路径损失为:%d' % (node.state, None, node.path_cost))
 
        # 遍历子节点
        for i in range(len(_city_info)):
            dst_city = ''
            if _city_info['city1'][i] == node.state:
                dst_city = _city_info['city2'][i]
            elif _city_info['city2'][i] == node.state:
                dst_city = _city_info['city1'][i]
            if dst_city == '':
                continue
            child = Node(dst_city, node, 'go', node.path_cost + _city_info['path_cost'][i])
            print('\t孩子节点:%s 路径损失为%d' % (child.state, child.path_cost))
            if child.state not in explored and not is_node_in_frontier(frontier, child):
                # 目标测试
                if child.state == dst_state:
                    print('\t\t 这个孩子节点就是目的城市')
                    return child
                frontier.append(child)
                print('\t\t 添加孩子节点到这个孩子')
 
 
def is_node_in_frontier(frontier, node):
    for x in frontier:
        if node.state == x.state:
            return True
    return False
 
 
def uniform_cost_search(src_state, dst_state):
    global _city_info, _frontier_priority
 
    node = Node(src_state, None, None, 0)
    frontier_priority_add(node)
    explored = []
 
    while True:
        if len(_frontier_priority) == 0:
            return False
        node = _frontier_priority.pop(0)
        if node.parent is not None:
            print('处理城市节点:%s\t父节点:%s\t路径损失为:%d' % (node.state, node.parent.state, node.path_cost))
        else:
            print('处理城市节点:%s\t父节点:%s\t路径损失为:%d' % (node.state, None, node.path_cost))
 
        # 目标测试
        if node.state == dst_state:
            print('\t 目的地已经找到了')
            return node
        explored.append(node.state)
 
        # 遍历子节点
        for i in range(len(_city_info)):
            dst_city = ''
            if _city_info['city1'][i] == node.state:
                dst_city = _city_info['city2'][i]
            elif _city_info['city2'][i] == node.state:
                dst_city = _city_info['city1'][i]
            if dst_city == '':
                continue
            child = Node(dst_city, node, 'go', node.path_cost + _city_info['path_cost'][i])
            print('\t孩子节点:%s 路径损失为:%d' % (child.state, child.path_cost))
 
            if child.state not in explored and not is_node_in_frontier(_frontier_priority, child):
                frontier_priority_add(child)
                print('\t\t 添加孩子到优先队列')
            elif is_node_in_frontier(_frontier_priority, child):
                # 替代为路径消耗少的节点
                frontier_priority_replace_by_priority(child)
 
 
def frontier_priority_add(node):
    """
    :param Node node:
    :return:
    """
    global _frontier_priority
    size = len(_frontier_priority)
    for i in range(size):
        if node.path_cost < _frontier_priority[i].path_cost:
            _frontier_priority.insert(i, node)
            return
    _frontier_priority.append(node)
 
 
def frontier_priority_replace_by_priority(node):
    """
    :param Node node:
    :return:
    """
    global _frontier_priority
    size = len(_frontier_priority)
    for i in range(size):
        if _frontier_priority[i].state == node.state and _frontier_priority[i].path_cost > node.path_cost:
            print('\t\t 替换状态: %s 旧的损失:%d 新的损失:%d' % (node.state, _frontier_priority[i].path_cost,
                                                                      node.path_cost))
            _frontier_priority[i] = node
            return
 
if __name__ == '__main__':
    main()
