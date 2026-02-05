# TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2  # minutes per layer

# TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time):
    """
    Calculate the bake time remaining.
    
    Args:
        elapsed_bake_time (int): baking time already elapsed.
    
    Returns:
        int: remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

# TODO: Define the 'preparation_time_in_minutes()' function below.
def preparation_time_in_minutes(number_of_layers):
    """
    Calculate the preparation time based on number of layers.
    
    Args:
        number_of_layers (int): number of lasagna layers.
    
    Returns:
        int: total preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME

# TODO: define the 'elapsed_time_in_minutes()' function below.
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