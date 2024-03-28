import click

from utils.sorting_algorithms import *
from utils.input_processing import get_nums_list, get_sorting_algorithm


@click.command()
@click.option('--runtime', '-f', is_flag=True, default=True,
              help='Display the execution time of the sorting algorithm.')
def main(runtime):
    # corresponding algorithm numbers to algorithms
    sorting_algorithms = {
        1: bubble_sort_algorithm,
        2: insertion_sort_algorithm,
        3: quick_sort_algorithm,
        4: selection_sort_algorithm,
        5: merge_sort_algorithm
    }

    # getting user input
    input_list = get_nums_list()
    input_algorithm = get_sorting_algorithm(sorting_algorithms)

    # outputting final results to the terminal
    result = input_algorithm(input_list)
    click.echo(f"\nSorted numbers: {result}")

    # import execution time after function run, for the value to be modified correctly
    if runtime:
        from utils.helpers import execution_time
        click.echo(f"function took {execution_time:.6f} seconds to execute.")


if __name__ == "__main__":
    main()


#  6, 19, -7, 9.7, 5, 134, 12, -13, -8.9, -5.1, 6.8
