def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for i in range(0, n):
        j = i
        while j > 0:
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
                j -= 1
            else:
                break


if __name__ == '__main__':
    list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(list_data)
    insert_sort(list_data)
    print(list_data)
