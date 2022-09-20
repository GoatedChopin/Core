def swap(x, y, array):
    array[x], array[y] = array[y], array[x]


def partition(low, high, array):
    while low < high:
        pivot = low
        pval = array[pivot]
        while low < high and array[low] <= pval:
            low += 1
        while high >= low and array[high] > pval:
            high -= 1
        if low < high:
            swap(low, high, array)
            print(array)
    swap(pivot, high, array)
    return high


def quicksort(l, h, array):
    if l < h:
        j = partition(l, h, array)
        quicksort(l, j, array)
        quicksort(j + 1, h, array)


if __name__ == "__main__":
    import random as r
    test_array = [4, 6, 7, 9, 1]
    quicksort(0, 4, test_array)
    print(test_array)
    for _ in range(100):
        test_array = [r.randint(0, 100) for i in range(11)]
        assert sorted(test_array) == quicksort(0, 9, test_array)
