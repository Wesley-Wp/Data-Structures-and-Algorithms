
class Node(object):
    """结点"""
    def __init__(self, data):
        self.data = data
        # 后继
        self.next = None
        # 前驱
        self.prev = None


class DoubleLinkList(object):
    """双链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        cur = self.__head
        # count用来计数
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.data, end=" ")
            cur = cur.next
        print(" ")

    def add(self, item):
        """链表头部添加元素   头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        Node.next.prev = node

    def append(self, item):
        """链表尾部添加元素     尾插法"""
        # 先构造一个节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < pos :
                cur = cur.next
                count += 1
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        while cur is not None:
            if cur.data == item:
                # 判断是否有头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.next.prev = cur.prev
                    cur.prev.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def serach(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while cur is not None:
            if cur.data == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    double_link = DoubleLinkList()
