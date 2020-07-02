def binary_search(alist, item):
    """
    二分查找（递归方式）
    :param alist: 传入的列表(必须为有序列表)
    :param item: 需要查找的元素
    :return:
    """
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid + 1:], item)
    return False


def binary_search2(alist, item):
    """二分查找（非递归）"""
    n = len(alist)
    first = 0
    last = n - 1

    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20, 100]
    list_data = [17, 20, 26, 31, 44, 54, 55, 77, 93, 100]
    print(list_data)
    print(binary_search(list_data, 4))
    print(binary_search2(list_data, 55))
