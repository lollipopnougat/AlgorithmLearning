# -*- coding=utf-8 -*-
# 哈夫曼编码 来源网络，仅供参考学习
# 构建节点类
class TreeNode:
    def __init__(self, data):
        """
        :data is a tuple the first element is value and the second is priority
        :param data:
        """
        self.value = data[0]
        self.priority = data[1]
        self.left_child = None
        self.right_child = None
        self.code = ""


# 创建树节点队列的函数
def create_node_queue(codes):
    queue = []
    for code in codes:
        queue.append(TreeNode(code))
    return queue


# 在队列中间添加新的节点元素并保证优先度从大到小排列
def add_queue(queue, node_new):
    if len(queue) == 0:
        return [node_new]
    for i in range(len(queue)):
        if queue[i].priority >= node_new.priority:
            return queue[:i] + [node_new] + queue[i:]
    return queue + [node_new]


# 节点队列类
class NodeQueue:
    def __init__(self, code):
        self.queue = create_node_queue(code)
        self.size = len(self.queue)

    def add_node(self, node):
        self.queue = add_queue(self.queue, node)
        self.size += 1

    def pop_node(self):
        self.size -= 1
        return self.queue.pop(0)


# 各个字符在字符串中出现的次数 即计算优先度
def frequent_char(string_s):
    store_d = {}
    for c in string_s:
        if c not in store_d:
            store_d[c] = 1
        else:
            store_d[c] += 1
    return sorted(store_d.items(), key=lambda x: x[1])


# 创建Huffman树
def create_huffman_tree(node_queue):
    while node_queue.size != 1:
        node1 = node_queue.pop_node()
        node2 = node_queue.pop_node()
        r_1 = TreeNode([None, node1.priority + node2.priority])
        r_1.left_child = node1
        r_1.right_child = node2
        node_queue.add_node(r_1)
    return node_queue.pop_node()


code_dict1 = {}
code_dict2 = {}


# 由Huffman树得到的Huffman编码表
def huffman_code_dict(head, x):
    # global code_dict, code_list
    if head:
        huffman_code_dict(head.left_child, x + "0")
        head.code += x
        if head.value:
            code_dict2[head.code] = head.value
            code_dict1[head.value] = head.code
        huffman_code_dict(head.right_child, x + "1")


# 字符串编码
def trans_encode(string_s):
    # global code_dict1
    trans_code = ""
    for c in string_s:
        trans_code += code_dict1[c]
    return trans_code


# 字符串解码
def trans_decode(string_s):
    # global code_dict1
    code = ""
    answer = ""
    for c in string_s:
        code += c
        if code in code_dict2:
            answer += code_dict2[code]
            code = ""
    return answer

res = frequent_char('accbbbffffeeeeedddddd')
res2 = NodeQueue(res)
tree = create_huffman_tree(res2)
huffman_code_dict(tree, '')
rr = trans_decode('111010101001001011110111100100100011101010111000011')
print(rr)