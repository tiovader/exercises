"""
this module is related to preparation time of a lasagna
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(time: int) -> int:
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''

    return EXPECTED_BAKE_TIME - time


def preparation_time_in_minutes(layers: int) -> int:
    """
    :param layers: int total of layers of lasagna
    :return: int total time of preparation of layers derived from 'PREPARATION_TIME'

    Function that takes the number of layers that will be prepared to lasagna and returns how many minutes it will take to get done
    """

    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """
    :param layers: int total of lasagna's layers
    :param time: int baking time already elapsed
    :return: int total of time elapsed into the prepare of lasagna

    Function that takes as param elapsed time and total of layers and returns the sum of time elapsed in prepare and in oven
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
