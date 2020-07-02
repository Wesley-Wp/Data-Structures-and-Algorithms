

class Queue(object):
    """队列"""
    def __init__(self):
        self.__list = []
    def enqueue(self, item):
        """往队列中添加元素"""
        self.__list.append(item)

    def dequeue(self):
        """从队列头部删除一个元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断一个队列是否为空"""
        return self.__list == []

    def size(self):
        """返回队列的大小"""
        return len(self.__list)


if __name__ == '__main__':
    Q = Queue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())