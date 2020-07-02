class Node(object):
    """节点"""

    def __init__(self, data):
        self.data = data
        self.next = None


class SingleCycleLinList(object):
    """单向循环链表"""

    def __init__(self, node=None):
        self.__head = node
        if node:
            node.next = node

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur游标，用来移动遍历节点
        if self.is_empty():
            return 0
        cur = self.__head
        # count用来计数
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        if self.is_empty():
            return
        cur = self.__head
        while cur.next is not self.__head:
            print(cur.data, end=" ")
            cur = cur.next
        print(cur.data)

    def add(self, item):
        """链表头部添加元素     头插法"""
        node = Node(item)
        cur = self.__head
        while cur.next is not self.__head:
            cur = cur.next
        node.next = self.__head
        self.__head = node
        cur.next = node
    def append(self, item):
        """链表尾部添加元素     尾插法"""
        # 先构造一个节点
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next is not self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素"""
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < (pos - 1):
                cur = cur.next
                count += 1
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return
        cur = self.__head
        pre = cur
        while cur.next is not self.__head:
            if cur.data == item:
                # 先判断此节点是否是头节点
                if cur == self.__head:
                    # 找尾结点
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间节点
                    pre.next = cur.next
                return 
            else:
                pre = cur
                cur = cur.next
        # 退出循环，cur指向尾结点
        if cur.data == item:
            if cur == self.__head:
                self.__head = None
            else:
            pre.next = cur.next

    def serach(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next is not self.__head:
            if cur.data == item:
                return True
            else:
                cur = cur.next
        if cur.data == item:
            return True
        return False


if __name__ == '__main__':
    single_obj = SingleLinList()
    print(single_obj.is_empty())
    print(single_obj.length())
    single_obj.append(1)
    print(single_obj.is_empty())
    print(single_obj.length())

    single_obj.append(2)
    single_obj.add(8)
    single_obj.append(3)
    single_obj.append(4)
    single_obj.append(5)
    single_obj.append(6)
    single_obj.insert(-1, 9)
    single_obj.travel()
    single_obj.remove(8)
    single_obj.travel()
    single_obj.append(7)
    single_obj.insert(20, 100)
    single_obj.append(200)
    single_obj.travel()
    single_obj.remove(200)
    single_obj.travel()
