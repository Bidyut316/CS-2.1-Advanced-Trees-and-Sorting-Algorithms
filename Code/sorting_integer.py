#!python
from sorting_iterative import *

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    min, max = min(numbers), max(numbers)
    # YOU HAVE TO USE A +1 FPR THE MAX OTHER WISE THIS WILL NOT SORT CORRECTLY OMG
    count_array = [0] * ((max + 1) - min)
    offset = min

    for i in range(0, len(numbers)):
        curr = numbers[i]
        count_array[curr - offset] += 1
    pos = 0 # indicates a position that will be used to calculatofoe the for loop below!
    for j in range(len(count_array)):  # Represents the index which is the value in input
        for occurence in range(count_array[j]):  # Iterate over how many times you see that specific element
            numbers[pos] = offset + j
            # i = i+ 1
            pos+=1
    return numbers


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    output =[]
    #OMG FORGOT THAT YOU HAVE TO DO INTEGER DIVISION THIS WILL MESS THIS UP....thanks matt!!
    range_num = len(numbers) // num_buckets
    # this works but theres a more pythonic way to do this
    # buckets = list()
    # for i in range(range_num +1):
    #     buckets.append([])
    buckets = [[] for _ in range(range_num + 1)]

    for index, number in enumerate(numbers):
        bucket_index, remainder = divmod(number, range_num)
        if remainder > 0:
            buckets[bucket_index].append(number)
        else:
            buckets[bucket_index - 1].append(number)
    for bucket in buckets:
        selection_sort(bucket)
        output.extend(bucket)
    return output
