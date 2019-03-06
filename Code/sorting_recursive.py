#!python
from sorting_iterative import *

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list
    index_0_list_1 = 0
    index_0_list_2 = 0
    final_sorted_list = []
    # stops when wither list one of list two is empty
    # runs slightly faster if list 1 comes first so redoing
    # while index_0_list_2 < len(items2) and index_0_list_1 < len(items1) :
    while index_0_list_1 < len(items1) and index_0_list_2 < len(items2):
        # Needs to find the minimum value first before comparisons
        min_list_1 = items1[index_0_list_1]
        min_list_2 = items2[index_0_list_2]
        # if the minumum of list 1 is smaller than the minimum of list two then min 1 is appened,
        # otherwise min 2 is appended, this should continue untill both are sorted
        if min_list_1 < min_list_2:
            final_sorted_list.append(min_list_1)
            index_0_list_1 += 1
        else:
            final_sorted_list.append(min_list_2)
            index_0_list_2 += 1
    # At this pint all of the itmes should be in the right places
    # return final_sorted_list
    # apparently this isnt the casse, forgot to add the items left in the lists as part of the algoritm
    if index_0_list_1 != len(items1):
        final_sorted_list.extend(items1[index_0_list_1:len(items1)])
    else:
        final_sorted_list.extend(items2[index_0_list_2:len(items2)])

    return final_sorted_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order
    # lwft half of the array
    left = items[0:middle]
    # middle half of the array
    middle = int((len(items)) / 2)
    # right half of the array
    right = items[middle:len(items)]
    # playing with multiple combionation to find the best running time
    insertion_sort(left)
    selection_sort(right)
    # combine the two orted arrays
    return merge(left, right)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order
    if len(items) == 1 or len(items) == 0:
        return items
        # no integer division needed
        # middle = len(items)//2

    middle = int((len(items)) / 2)
    # 2 hlaves of the original list
    right = items[middle:len(items)]

    left = items[0:middle]

    merge_sort(left)
    merge_sort(right)
    # not supposed to return somthing so was changed
    items[:] = merge(left, right)


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    pivot_value = items[low]
    left_mark = low + 1
    right_mark = high
    done = False
    while not done:
        while left_mark <= right_mark and \
                items[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while items[right_mark] >= pivot_value and \
                right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = items[left_mark]
            items[left_mark] = items[right_mark]
            items[right_mark] = temp
    temp = items[low]
    items[low] = items[right_mark]
    items[right_mark] = temp
    return right_mark


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    # need to add a case to check for invalid input but not sure how...hmmmm
    # if low wasnt passed in as a parameter, set it to a zero(begiining index forthe partition)
    if low == None:
        low = 0
    # if high is none then for the partition set it to the end of the listposition for the partition
    if high == None:
        high = len(items)
    #
    if low < high:
        pivot = partition(items, low, high)

        quick_sort(items, pivot + 1, high)
        quick_sort(items, low, pivot - 1)

    return items
