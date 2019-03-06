#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    # check if the list length is 0 or 1, if empty
    # then technically tis sorted, if theres one item in the list, same
    if (len(items) == 0 or len(items) == 1):
        return True
    # inerate through the list based on positions untill the end of th list
    for i in range(1, len(items)):
        # if the last item is larger than the current one we knwo it isntsorted
        if (items[i - 1] > items[i]):
            return False
    # else return true
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    for pass_num in range(len(items) - 1, 0, -1):
        for i in range(pass_num):
            if items[i] > items[i + 1]:
                temp = items[i]
                items[i] = items[i + 1]
                items[i + 1] = temp


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    for fill_slot in range(len(items) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if items[location] > items[pos_of_max]:
                pos_of_max = location
        temp = items[fill_slot]
        items[fill_slot] = items[pos_of_max]
        items[pos_of_max] = temp


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    for index in range(1, len(items)):
        current_value = items[index]
        position = index
        while position > 0 and items[position - 1] > current_value:
            items[position] = items[position - 1]
            position = position - 1
            items[position] = current_value
