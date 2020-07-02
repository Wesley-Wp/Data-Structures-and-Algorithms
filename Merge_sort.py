def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0      # 新列表左、右的游标
    result = []     # 新的列表，存储排序好的列表
    while left_pointer < len(left_list) and right_pointer < len(right_list):

        if left_list[left_pointer] < right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1

    result += left_list[left_pointer:]
    result += right_list[right_pointer:]

    return result


if __name__ == '__main__':
    list_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(list_data)
    s = merge_sort(list_data)
    print(s)
