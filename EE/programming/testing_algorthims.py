"""
    The insertion, heap, merge, quick and shell sort are inspired and modified from
    https://gist.github.com/amit-singh-rathore/0b8b8ffbc74fefe36fc09ff64c900cd5#file-sort_all_algo-py
"""

import time
#start = time.time()


class Algorithms:

    # Sorts by putting the smallest number at the 0th index and continuing from there on
    def selection_sort_notes(self, arr):
        length = len(arr)
        for i in range(length):
            min_idx = i
            for j in range(i+1, length):
                if arr[min_idx] > arr[j]:
                    min_idx = j
                    arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr

    # bubble sort
    def bubble_sort(self, arr):
        n = len(arr)

        # Traverse through all array elements
        for i in range(n):

            # Last i elements are already in place
            for j in range(0, n-i-1):

                # traverse the array from 0 to n-i-1
                # Swap if the element found is greater
                # than the next element
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

        return arr

    def insertionSort(self, array):
        for i in range(1, len(array)):
            key = array[i]
            j = i-1
            while array[j] > key and j >= 0:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = key
        return array

    # HEAP_SORT
    def heapify(self, array, n, i):
        largest = i
        # change to left
        l = 2 * i + 1
        # change to right
        r = 2 * i + 2

        if l < n and array[i] < array[l]:
            largest = l

        if r < n and array[largest] < array[r]:
            largest = r

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self.heapify(array, n, largest)

    def heapSort(self, array):
        n = len(array)
        for i in range(n//2, -1, -1):
            self.heapify(array, n, i)
        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
        return array

    # MERGE_SORT
    def merge(self, lst1, lst2):
        lst = []
        i = 0
        j = 0
        while i <= len(lst1)-1 and j <= len(lst2)-1:
            if lst1[i] < lst2[j]:
                lst.append(lst1[i])
                i += 1
            else:
                lst.append(lst2[j])
                j += 1
        if i > len(lst1)-1:
            while(j <= len(lst2)-1):
                lst.append(lst2[j])
                j += 1
        else:
            while(i <= len(lst1)-1):
                lst.append(lst1[i])
                i += 1
        return lst

    def mergeSort(self, nums):
        if len(nums) == 1:
            return nums
        mid = (len(nums)-1) // 2
        lst1 = self.mergeSort(nums[:mid+1])
        lst2 = self.mergeSort(nums[mid+1:])
        result = self.merge(lst1, lst2)
        return result

    # QUICK_SORT
    def quickSort(self, array):
        if len(array) > 1:
            pivot = array.pop()
            grtr_lst, equal_lst, smlr_lst = [], [pivot], []
            for item in array:
                if item == pivot:
                    equal_lst.append(item)
                elif item > pivot:
                    grtr_lst.append(item)
                else:
                    smlr_lst.append(item)
            return (self.quickSort(smlr_lst) + equal_lst + self.quickSort(grtr_lst))
        else:
            return array

    # SHELL_SORT
    def shellSort(self, array):
        n = len(array)
        interval = n // 2
        while interval > 0:
            for i in range(interval, n):
                temp = array[i]
                j = i
                while j >= interval and array[j - interval] > temp:
                    array[j] = array[j - interval]
                    j -= interval

                array[j] = temp
            interval //= 2
        return array


'''
testing = Algorithms()


print(testing.shellSort([3, 5, 6, 4, 2, 1]))
end = time.time()
print(end - start)
'''
