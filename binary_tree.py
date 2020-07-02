class Node(object):
    """树的节点"""

    def __init__(self, item):
        self.item = item
        self.left_child = None
        self.right_child = None


class Tree(object):
    """二叉树"""

    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.left_child is None:
                cur_node.left_child = node
                return
            else:
                queue.append(cur_node.left_child)
            if cur_node.right_child is None:
                cur_node.right_child = node
                return
            else:
                queue.append(cur_node.right_child)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.item, end=" ")
            if cur_node.left_child is not None:
                queue.append(cur_node.left_child)

            if cur_node.right_child is not None:
                queue.append(cur_node.right_child)

    def preorder(self, root_node):
        """先序遍历（根左右）"""
        if root_node is None:
            return

        print(root_node.item, end=" ")
        self.preorder(root_node.left_child)
        self.preorder(root_node.right_child)

    def inorder(self, root_node):
        """中序遍历（左根右）"""
        if root_node is None:
            return

        self.inorder(root_node.left_child)
        print(root_node.item, end=" ")
        self.inorder(root_node.right_child)

    def postorder(self, root_node):
        """后序遍历（左右根）"""
        if root_node is None:
            return

        self.postorder(root_node.left_child)
        self.postorder(root_node.right_child)
        print(root_node.item, end=" ")


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print(" ")
    tree.preorder(tree.root)
    print(" ")
    tree.inorder(tree.root)
    print(" ")
    tree.postorder(tree.root)
