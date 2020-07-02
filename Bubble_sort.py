def bubble_sort(alist):
    """冒泡排序"""
    for i in range(0, len(alist)):
        for j in range(0, len(alist) - 1 - i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]


if __name__ == '__main__':
    list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(list_data)
    bubble_sort(list_data)
    print(list_data)
