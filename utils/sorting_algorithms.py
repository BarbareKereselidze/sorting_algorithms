from typing import List
from utils.helpers import output_result


@output_result
def bubble_sort_algorithm(nums_list: List[float]) -> List[float]:
    """ Sorts a list of numbers using bubble sort algorithm. """

    list_len = len(nums_list) - 1

    for i in range(list_len):
        for ind in range(list_len - i):
            if nums_list[ind] > nums_list[ind + 1]:
                swap = nums_list[ind]
                nums_list[ind] = nums_list[ind + 1]
                nums_list[ind + 1] = swap

    return nums_list


@output_result
def insertion_sort_algorithm(nums_list: List[float]) -> List[float]:
    """ Sorts a list of numbers using insertion sort algorithm. """

    len_of_list = len(nums_list)

    for i in range(1, len_of_list):
        numb1 = nums_list[i]
        ind = i - 1
        while ind >= 0 and numb1 < nums_list[ind]:
            nums_list[ind + 1] = nums_list[ind]
            ind -= 1

        nums_list[ind + 1] = numb1

    return nums_list


@output_result
def quick_sort_algorithm(nums_list: List[float]) -> List[float]:
    """ Sorts a list of numbers using quick sort algorithm. """

    if len(nums_list) <= 1:
        return nums_list

    # choosing the pivot (last element)
    pivot = nums_list[-1]

    smaller_than = []
    mid = []
    larger_than = []

    for x in nums_list:
        if x < pivot:
            smaller_than.append(x)
        elif x > pivot:
            larger_than.append(x)
        else:
            mid.append(pivot)

    return quick_sort_algorithm(smaller_than) + mid + quick_sort_algorithm(larger_than)


@output_result
def selection_sort_algorithm(nums_list: List[float]) -> List[float]:
    """Sorts a list of numbers using selection sort algorithm. """

    for i in range(len(nums_list)):
        min_index = i
        for j in range(i + 1, len(nums_list)):
            if nums_list[j] < nums_list[min_index]:
                min_index = j
        nums_list[i], nums_list[min_index] = nums_list[min_index], nums_list[i]

    return nums_list


@output_result
def merge_sort_algorithm(nums_list: List[float]) -> List[float]:
    """ Sorts a list of numbers using merge sort algorithm. """

    if len(nums_list) <= 1:
        return nums_list

    mid = len(nums_list) // 2
    left_half = merge_sort_algorithm(nums_list[:mid])
    right_half = merge_sort_algorithm(nums_list[mid:])

    return merge(left_half, right_half)


def merge(left: List[float], right: List[float]) -> List[float]:
    """Merges two sorted lists into a single sorted list.

    Args:
        left - left half of the list
        right - right half of the list
    Returns:
        merged - merged and sorted list
    """
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged
