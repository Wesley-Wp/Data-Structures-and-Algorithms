class Node(object):
    """节点"""

    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinList(object):
    """单链表"""

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
        while cur is not None:
            print(cur.data, end=" ")
            cur = cur.next
        print(" ")

    def add(self, item):
        """链表头部添加元素     头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

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
        cur = self.__head
        pre = cur
        while cur is not None:
            if cur.data == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
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
