import click

from utils.helpers import SortingAlgorithmError


def get_nums_list():
    """ Prompt user to enter a list of numbers. """

    try:
        list_of_numbers = click.prompt(text="Enter a list of numbers separated by commas",
                                       type=str)

        nums_list = [float(x) for x in list_of_numbers.split(',')]
        click.echo(f'\nYour list: {nums_list}')

        return nums_list

    except (ValueError, TypeError):
        click.echo("Please enter a valid list of numbers.")
        raise click.Abort()


def get_sorting_algorithm(sorting_algorithms):
    """ Prompt user to choose a sorting algorithm. """

    try:
        click.echo("\nChoose which algorithm you want to use:")

        for key, algorithm in sorting_algorithms.items():
            click.echo(f"{key}. {algorithm.__name__.replace('_', ' ')}")

        sorting_algorithm = click.prompt(text="\nInput choice",
                                         type=int)

        if sorting_algorithm not in sorting_algorithms:
            raise SortingAlgorithmError

        selected_algorithm = sorting_algorithms[sorting_algorithm]
        algorithm_name = selected_algorithm.__name__.replace("_", " ")
        click.echo(f"You chose: {algorithm_name}")

        return selected_algorithm

    except Exception as e:
        click.echo(f"Invalid input, the following error occurred: {e}")
        click.Abort()
