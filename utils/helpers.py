import functools
import time
from typing import Callable, List, Tuple


# defining start time and execution time as global variables, for recursive functions
start_time = 0
execution_time = 0


def output_result(sorting_function: Callable) -> Callable:
    @functools.wraps(sorting_function)
    def wrapper(nums_list: List[float]) -> Tuple[float, List[float]]:
        """ Wrapper function that measures the execution time of the sorting function,
            and how much time the function takes to execute.

            If the sorting function is recursive,
            the global variable 'execution_time' is changed to the execution time of the most recent call,
            and 'start_time' is used to retrieve the start time only once for accuracy.

            Args:
                nums_list - list of numbers to be sorted
            Returns:
                result - sorted list of numbers
        """

        global start_time, execution_time

        # set start_time only once, for recursive functions
        if not start_time:
            start_time = time.time()

        result = sorting_function(nums_list)

        end_time = time.time()
        execution_time = end_time - start_time

        return result

    return wrapper


class SortingAlgorithmError(Exception):
    """ Custom exception raised for errors in selecting a sorting algorithm."""

    def __init__(self, message="Invalid sorting algorithm number."):
        self.message = message
        super().__init__(self.message)
