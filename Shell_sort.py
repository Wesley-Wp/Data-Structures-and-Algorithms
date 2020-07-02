def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            while j > 0:
                if alist[j] < alist[j - gap]:
                    alist[j], alist[j - gap] = alist[j - gap], alist[j]
                    j -= gap
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(list_data)
    shell_sort(list_data)
    print(list_data)
