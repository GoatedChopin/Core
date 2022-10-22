def MergeSort(array):
    if len(array) > 1:
        m = len(array) // 2
        L = array[:m]
        R = array[m:]

        MergeSort(L)
        MergeSort(R)

        l_index, r_index, arr_index = 0, 0, 0
        while l_index < len(L) and r_index < len(R):
            if L[l_index] <= R[r_index]:
                array[arr_index] = L[l_index]
                l_index += 1
            else:
                array[arr_index] = R[r_index]
                r_index += 1
            arr_index += 1

        while l_index < len(L):
            array[arr_index] = L[l_index]
            l_index += 1
            arr_index += 1
        while r_index < len(R):
            array[arr_index] = R[r_index]
            r_index += 1
            arr_index += 1


if __name__ == "__main__":
    test_array = [5, 3, 2, 8, 1]
    MergeSort(test_array)
    assert test_array == sorted(test_array)
