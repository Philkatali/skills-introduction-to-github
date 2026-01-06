"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""



EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # minutes per layer


def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.
    
    Args:
        elapsed_bake_time (int): baking time already elapsed.
    
    Returns:
        int: remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time based on number of layers.
    
    Args:
        number_of_layers (int): number of lasagna layers.
    
    Returns:
        int: total preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calculate the total elapsed time (preparation + baking).
    
    Args:
        number_of_layers (int): number of lasagna layers.
        elapsed_bake_time (int): baking time already elapsed.
    
    Returns:
        int: total elapsed time in minutes.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    return preparation_time + elapsed_bake_time