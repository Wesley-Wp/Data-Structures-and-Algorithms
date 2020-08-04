# -*- coding:utf-8 -*-
"""
# @Time  :2020/8/4 14:14
#@Author :Wesley
#@File   :树的深度和宽度.py
#@IDE    :PyCharm
#@Email  :984@qq.com
"""
import queue


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = None
        self.left = left
        self.right = right


def treeDepth(tree):
    if tree == None:
        return 0
    leftDepth = treeDepth(tree.left)
    rightDepth = treeDepth(tree.right)
    if leftDepth > rightDepth:
        return leftDepth + 1
    if rightDepth >= leftDepth:
        return rightDepth + 1


def treeWidth(tree):
    curwidth = 1
    maxwidth = 0
    q = queue.Queue()
    q.put(tree)
    while not q.empty():
        n = curwidth
        for i in range(n):
            tmp = q.get()
            curwidth -= 1
            if tmp.left:
                q.put(tmp.left)
                curwidth += 1
            if tmp.right:
                q.put(tmp.right)
                curwidth += 1
        if curwidth > maxwidth:
            maxwidth = curwidth
    return maxwidth


if __name__ == '__main__':
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    depth = treeDepth(root)
    width = treeWidth(root)
    print('depth:', depth)
    print('width:', width)


