def quick_sort(alist, first, last):
    """
    快速排序
    :param alist: 传入需要排序的列表
    :param first: 列表最开始的位置索引
    :param last:  列表最后的位置索引
    :return:
    """
    if first >= last:
        return
    min_value = alist[first]
    low = first
    high = last

    while low < high:
        while low < high and alist[high] >= min_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < min_value:
            low += 1
        alist[high] = alist[low]
    # 从循环退出时，low = high
    alist[low] = min_value
    # 从low左边列表执行快速排序
    quick_sort(alist, first, low - 1)
    # 从low右边列表执行快速排序
    quick_sort(alist, low + 1, last)


if __name__ == '__main__':
    list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(list_data)
    quick_sort(list_data, 0, len(list_data) - 1)
    print(list_data)
