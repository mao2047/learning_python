EXPECTED_BAKE_TIME = 40
#Time expected of lasagna in oven
PREPARATION_TIME = 2
#each layer of lasagna takes 2 minutes to prepare

def bake_time_remaining(elapsed_bake_time):
    """
    This function returns elapsed cooking time
    It evaluates elapsed_bake_time, if its higher than
    EXPECTED_BAKE_TIME, then the lasagna is burned
    """
    if elapsed_bake_time <= EXPECTED_BAKE_TIME:
        return EXPECTED_BAKE_TIME - elapsed_bake_time
    else:
        return 0

def preparation_time_in_minutes(number_of_layers):
    """
    This function evaluates how much time it takes
    to prepare each layer
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(elapsed_bake_time, number_of_layers):
    """
    This function returns the total time of preparation and oven time
    """
    print(bake_time_remaining(elapsed_bake_time) + preparation_time_in_minutes(number_of_layers))

elapsed_time_in_minutes(1, 3)