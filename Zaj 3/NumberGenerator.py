import numpy as np


def random_ints(minim, maxim, vect_size):
    # Create random array of numbers in range(MIN_INT, MAX_INT)
    random_array = np.random.randint(low=minim, high=maxim, size=vect_size)
    return random_array
