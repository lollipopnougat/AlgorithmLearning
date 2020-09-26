class TreeNode:
    val = None
    left = None
    right = None

    def __init__(self, value):
        self.val = value


class BinTree:
    node = None
    numlst = None
    tree_str = ''

    def __make_tree(self):
        node = TreeNode(self.numlst[0])
        quque = [node]
        l, i, ne = len(self.numlst), 1, True
        
        while i < l:
            if ne:
                if self.numlst[i]:
                    quque[0].left = TreeNode(self.numlst[i])
                quque.append(quque[0].left)
                ne = False
            else:
                tmp = quque.pop()
                if self.numlst[i]:
                    tmp.right = TreeNode(self.numlst[i])
                quque.append(tmp.right)
                ne = True
            i += 1

        return node

    def __init__(self, nums: list):
        self.numlst = nums
        if len(nums) != 0:
            self.node = self.__make_tree()

    # 前序
    def __DLR(self, node: TreeNode):
        if node != None:
            self.tree_str += ' ' + str(node.val)
            self.__DLR(node.left)
            self.__DLR(node.right)

    # 前序非递归
    def __DLRNR(self, node: TreeNode):
        stack = []
        stack.append(node)
        flag = False  # 是否跳转父节点
        while len(stack) != 0:
            root = stack.pop()
            self.tree_str += ' ' + str(root.val)
            if root.right != None:
                stack.append(root.right) # 注意栈的特点 后进先出
            if root.left != None:
                    stack.append(root.left)
                
    # 中序
    def __LDR(self, node: TreeNode):
        if node != None:
            self.__LDR(node.left)
            self.tree_str += ' ' + str(node.val)
            self.__LDR(node.right)

    # 中序非递归
    def __LDRNR(self, node: TreeNode):
        stack = []
        stack.append(node)
        flag = False  # 是否跳转父节点
        while len(stack) != 0:
            root = stack[-1]
            if root.left != None and not flag:
                stack.append(root.left)
            else:
                self.tree_str += ' ' + str(root.val)
                stack.pop()
                if root.right != None:
                    stack.append(root.right)
                    flag = False
                else:
                    flag = True

    #后序
    def __LRD(self, node: TreeNode):
        if node != None:
            self.__LRD(node.left)
            self.__LRD(node.right)
            self.tree_str += ' ' + str(node.val)

    # 后序非递归 
    def __LRDNR(self, node: TreeNode):
        stack = []
        tmp = []
        stack.append(node)
        while len(stack) != 0:
            root = stack[-1]
            if len(tmp) != 0 and tmp[-1] == root:
                self.tree_str += ' ' + str(root.val)
                tmp.pop()
                stack.pop()
            elif root == None:
                stack.pop()
                continue
            else:
                tmp.append(root)
                stack.append(root.right)
                stack.append(root.left)
    # 层序
    def __level_order(self, node: TreeNode):
        if node == None:
            return []
        que = [node]
        while que:
            p = que.pop(0)
            if p:
                self.tree_str += str(p.val) + ' '
                que.append(p.left)
                que.append(p.right)

    def print_tree(self, show_type: str):
        self.tree_str = ''
        node = self.node
        if show_type == 'DLR':
            self.__DLR(node)
            print('前序遍历(递归): ')
        elif show_type == 'LDR':
            self.__LDR(node)
            print('中序遍历(递归): ')
        elif show_type == 'LRD':
            self.__LRD(node)
            print('后序遍历(递归): ')
        elif show_type == 'LDRNR':
            self.__LDRNR(node)
            print('中序遍历(非递归): ')
        elif show_type == 'DLRNR':
            self.__DLRNR(node)
            print('前序遍历(非递归): ')  
        elif show_type == 'LRDNR':
            self.__LRDNR(node)
            print('后序遍历(非递归): ') 
        elif show_type == 'LEV':
            self.__level_order(node)
            print('层序遍历: ')       
        else:
            self.tree_str = '参数错误'
        print(self.tree_str)

tr = [5,4,8,11,None,13,4,7,2,None,None,5,1]

tree = BinTree(tr)

tree.print_tree('DLR')