

class Dueue(object):
    """双端队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """往队头中添加元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """在队列尾部添加元素"""
        return self.__list.append(item)

    def remove_front(self):
        """从队头删除元素"""
        return self.__list.pop()

    def remove_rear(self):
        """从队尾删除元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    Q = Dueue()
    Q.add_front(1)
    Q.add_front(2)
    Q.add_rear(3)
    Q.add_rear(4)
    print(Q.size())
    print(Q.remove_front())
