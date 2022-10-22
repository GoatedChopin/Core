from DataStructures.Heap import Heap


def HeapSort(unsorted_list, reverse=False):
    heap = Heap()
    for element in unsorted_list:
        heap.push(element)
    unsorted_list = [heap.pop() for _ in range(len(unsorted_list))]
    if reverse:
        return unsorted_list
    else:
        return unsorted_list[::-1]


if __name__ == "__main__":
    import random as r

    l = []
    for i in range(1000):
        l.append(r.randint(0, 1000))
    s = sorted(l)
    assert HeapSort(l) == s
