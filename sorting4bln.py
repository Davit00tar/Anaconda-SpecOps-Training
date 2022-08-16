

def merge_sort(data):
    if len(data) > 1:
        left = data[:len(data) // 2]
        right = data[len(data) // 2:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(left):
            data[k] = right[j]
            j += 1
            k += 1
    return data

def sorting(data_file, result):
    # from file to list
    data = open(data_file, "r")
    temp = []
    lst_int = []
    temp = data.read().split('\n')
    for i in temp[: -1]:
        lst_int.append(int(i))
    data.close()

    # sorting
    sorted_lst = merge_sort(lst_int)

    # output
    with open(result, "w") as location:
        for el in sorted_lst:
            location.write(str(el) + '\n')

sorting('4b_rand.txt','testing_this.tx')














